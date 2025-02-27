import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
from seigr_kodeks.storage_manager import (
    select_storage_path,
    load_preferences,
    save_preferences,
)
from seigr_kodeks.file_manager import organize_files
from seigr_kodeks.media_manager import insert_image, insert_audio, insert_video
from seigr_kodeks.exporter import export_to_html, preview_html
import os
import json


class SeigrKodeksApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SeigrKodeks - Book Creator")
        self.root.geometry("900x600")

        # Load user preferences
        self.preferences = load_preferences()
        self.storage_path = self.preferences.get("storage_path", "")
        if not self.storage_path:
            self.storage_path = select_storage_path()
            if self.storage_path:
                self.preferences["storage_path"] = self.storage_path
                save_preferences(self.preferences)

        # Ensure SeKo_Books directory exists
        self.books_directory = os.path.join(self.storage_path, "SeKo_Books")
        os.makedirs(self.books_directory, exist_ok=True)

        self.book_path = ""
        self.book_metadata = {}

        # UI Layout
        self.create_ui()
        self.load_recent_books()

    def create_ui(self):
        """Create the UI components for the application."""
        # Book Selection
        self.book_frame = tk.Frame(self.root)
        self.book_frame.pack(pady=5)

        tk.Label(
            self.book_frame, text="Select a book to work on, or create a new one:"
        ).pack(side=tk.LEFT)
        self.book_title_label = tk.Label(
            self.book_frame, text="(No book selected)", fg="blue"
        )
        self.book_title_label.pack(side=tk.LEFT)
        tk.Button(
            self.book_frame, text="Create/Open Book", command=self.select_book
        ).pack(side=tk.LEFT, padx=10)

        # Recent Books List
        self.recent_books_listbox = tk.Listbox(self.root, height=5)
        self.recent_books_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.recent_books_listbox.bind("<<ListboxSelect>>", self.open_recent_book)

        # File Management Buttons
        self.file_buttons = tk.Frame(self.root)
        self.file_buttons.pack(pady=5)
        tk.Button(
            self.file_buttons,
            text="📷 Add Image",
            command=lambda: insert_image(self.book_path),
        ).pack(side=tk.LEFT, padx=2)
        tk.Button(
            self.file_buttons,
            text="🎵 Add Audio",
            command=lambda: insert_audio(self.book_path),
        ).pack(side=tk.LEFT, padx=2)
        tk.Button(
            self.file_buttons,
            text="🎬 Add Video",
            command=lambda: insert_video(self.book_path),
        ).pack(side=tk.LEFT, padx=2)
        tk.Button(
            self.file_buttons,
            text="📂 Organize Files",
            command=lambda: organize_files(self.book_path),
        ).pack(side=tk.LEFT, padx=2)

        # Export & Preview Buttons
        self.export_buttons = tk.Frame(self.root)
        self.export_buttons.pack(pady=5)
        tk.Button(
            self.export_buttons,
            text="📖 Preview HTML",
            command=lambda: preview_html(self.book_path),
        ).pack(side=tk.LEFT, padx=2)
        tk.Button(
            self.export_buttons,
            text="🌍 Export to HTML",
            command=lambda: export_to_html(self.book_path),
        ).pack(side=tk.LEFT, padx=2)

    def select_book(self):
        """Allows user to create or open a book."""
        book_directory = filedialog.askdirectory(
            title="Select or Create a Book Directory", initialdir=self.books_directory
        )
        if book_directory:
            self.book_path = book_directory
            self.book_title_label.config(text=os.path.basename(book_directory))

            # Ensure structured book directories exist
            os.makedirs(os.path.join(self.book_path, "chapters"), exist_ok=True)
            os.makedirs(os.path.join(self.book_path, "media"), exist_ok=True)

            # Load or create book.json
            book_metadata_path = os.path.join(self.book_path, "book.json")
            if os.path.exists(book_metadata_path):
                with open(book_metadata_path, "r", encoding="utf-8") as file:
                    self.book_metadata = json.load(file)
            else:
                self.book_metadata = {
                    "title": os.path.basename(book_directory),
                    "chapters": [],
                    "media": [],
                }
                self.save_book_metadata()

            if book_directory not in self.preferences["recent_books"]:
                self.preferences["recent_books"].insert(0, book_directory)
                self.preferences["recent_books"] = self.preferences["recent_books"][
                    :5
                ]  # Keep last 5 books
                save_preferences(self.preferences)

            self.load_recent_books()

    def load_recent_books(self):
        """Loads the list of recently opened books."""
        self.recent_books_listbox.delete(0, tk.END)
        for book in self.preferences.get("recent_books", []):
            self.recent_books_listbox.insert(tk.END, os.path.basename(book))

    def open_recent_book(self, event):
        """Opens a recently used book."""
        selected = self.recent_books_listbox.curselection()
        if not selected:
            return
        selected_book = self.preferences["recent_books"][selected[0]]
        if os.path.exists(selected_book):
            self.book_path = selected_book
            self.book_title_label.config(text=os.path.basename(selected_book))
        else:
            messagebox.showwarning("Warning", "This book folder no longer exists.")
            del self.preferences["recent_books"][selected[0]]
            save_preferences(self.preferences)
            self.load_recent_books()

    def save_book_metadata(self):
        """Saves the book metadata to book.json."""
        book_metadata_path = os.path.join(self.book_path, "book.json")
        with open(book_metadata_path, "w", encoding="utf-8") as file:
            json.dump(self.book_metadata, file, indent=4)


if __name__ == "__main__":
    root = tk.Tk()
    app = SeigrKodeksApp(root)
    root.mainloop()
