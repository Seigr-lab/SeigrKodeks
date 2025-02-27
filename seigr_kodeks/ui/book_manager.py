import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import json
import os
from seigr_kodeks.storage_manager import load_preferences, save_preferences


class BookManager:
    def __init__(self, parent, books_directory, load_book_callback):
        """Handles book selection, recent books, and book creation."""
        self.parent = parent
        self.books_directory = books_directory
        self.load_book_callback = (
            load_book_callback  # This updates MainWindow's book path
        )

        # 📂 UI Frame
        self.frame = tk.Frame(parent, padx=10, pady=10, borderwidth=2, relief="groove")
        self.frame.grid(row=0, column=0, rowspan=2, sticky="ns")

        tk.Label(self.frame, text="📚 Books", font=("Arial", 12, "bold")).grid(
            row=0, column=0, sticky="w", padx=5, pady=2
        )

        # 📄 Listbox for recent books
        self.book_listbox = tk.Listbox(self.frame, height=8)
        self.book_listbox.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.book_listbox.bind("<<ListboxSelect>>", self.select_book)

        # 📌 Buttons for book management
        button_frame = tk.Frame(self.frame)
        button_frame.grid(row=2, column=0, sticky="ew", pady=5)

        tk.Button(button_frame, text="📂 Open Book", command=self.open_book).grid(
            row=0, column=0, sticky="ew", padx=2
        )
        tk.Button(button_frame, text="➕ Create New", command=self.create_book).grid(
            row=0, column=1, sticky="ew", padx=2
        )

        # Load recent books on startup
        self.preferences = load_preferences()
        self.load_recent_books()

    def load_recent_books(self):
        """Loads the list of recently used books from preferences."""
        self.book_listbox.delete(0, tk.END)
        recent_books = self.preferences.get("recent_books", [])

        valid_books = [book for book in recent_books if os.path.exists(book)]
        self.preferences["recent_books"] = valid_books  # Remove invalid entries

        for book_path in valid_books:
            self.book_listbox.insert(tk.END, os.path.basename(book_path))

        save_preferences(self.preferences)

    def select_book(self, event):
        """Handles book selection from the recent books list."""
        selected_index = self.book_listbox.curselection()
        if not selected_index:
            return

        book_name = self.book_listbox.get(selected_index[0])
        book_path = next(
            (
                path
                for path in self.preferences["recent_books"]
                if os.path.basename(path) == book_name
            ),
            None,
        )

        if book_path and os.path.exists(book_path):
            self.load_book_callback(
                book_path
            )  # Update book path globally in MainWindow
        else:
            messagebox.showwarning("Warning", "This book folder no longer exists.")
            del self.preferences["recent_books"][selected_index[0]]
            save_preferences(self.preferences)
            self.load_recent_books()

    def open_book(self):
        """Opens an existing book directory from the list or prompts the user if none is selected."""
        selected_book_path = self.get_selected_book_path()

        if selected_book_path and os.path.exists(selected_book_path):
            # ✅ A book is already selected, so just open it
            self.load_book_callback(selected_book_path)
        else:
            # 🚨 No book selected → Ask the user for a book directory
            book_directory = filedialog.askdirectory(
                title="Select a Book Directory", initialdir=self.books_directory
            )
            if book_directory:
                self.add_book_to_recent(book_directory)
                self.load_book_callback(book_directory)

    def create_book(self):
        """Creates a new book directory and initializes its structure."""
        book_directory = filedialog.askdirectory(
            title="Select Location for New Book", initialdir=self.books_directory
        )
        if not book_directory:
            return

        book_name = simpledialog.askstring("New Book", "Enter book title:")
        if not book_name:
            return

        new_book_path = os.path.join(book_directory, book_name)
        if os.path.exists(new_book_path):
            messagebox.showerror("Error", "A book with this name already exists.")
            return

        os.makedirs(new_book_path, exist_ok=True)
        os.makedirs(os.path.join(new_book_path, "chapters"), exist_ok=True)
        os.makedirs(os.path.join(new_book_path, "media"), exist_ok=True)

        # Initialize book metadata
        book_metadata = {"title": book_name, "chapters": [], "media": []}
        with open(
            os.path.join(new_book_path, "book.json"), "w", encoding="utf-8"
        ) as file:
            json.dump(book_metadata, file, indent=4)

        self.add_book_to_recent(new_book_path)
        self.load_book_callback(new_book_path)

    def add_book_to_recent(self, book_path):
        """Adds a book to the recent books list and ensures it is saved."""
        if book_path not in self.preferences["recent_books"]:
            self.preferences["recent_books"].insert(0, book_path)
            self.preferences["recent_books"] = self.preferences["recent_books"][
                :5
            ]  # Keep last 5 books
            save_preferences(self.preferences)
        self.load_recent_books()

    def get_selected_book_path(self):
        """Returns the currently selected book path, or None if no book is selected."""
        selected_index = self.book_listbox.curselection()
        if not selected_index:
            return None  # No book selected

        book_name = self.book_listbox.get(selected_index[0])
        book_path = next(
            (
                path
                for path in self.preferences["recent_books"]
                if os.path.basename(path) == book_name
            ),
            None,
        )
        return book_path if book_path and os.path.exists(book_path) else None

    def save_book_metadata(self):
        """Ensures the book metadata (book.json) is correctly saved."""
        selected_book_path = self.get_selected_book_path()
        if not selected_book_path:
            messagebox.showerror("Error", "No book selected to save.")
            return

        book_metadata_path = os.path.join(selected_book_path, "book.json")

        # If book.json does not exist, initialize with empty metadata
        if not os.path.exists(book_metadata_path):
            book_metadata = {
                "title": os.path.basename(selected_book_path),
                "chapters": [],
                "media": [],
            }
        else:
            with open(book_metadata_path, "r", encoding="utf-8") as file:
                try:
                    book_metadata = json.load(file)
                except json.JSONDecodeError:
                    messagebox.showerror(
                        "Error", "Invalid book metadata. Resetting file."
                    )
                    book_metadata = {
                        "title": os.path.basename(selected_book_path),
                        "chapters": [],
                        "media": [],
                    }

        # Save metadata back to file
        with open(book_metadata_path, "w", encoding="utf-8") as file:
            json.dump(book_metadata, file, indent=4)

        messagebox.showinfo("Success", "Book metadata saved successfully!")
