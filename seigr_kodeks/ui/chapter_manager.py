import os
import json
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox


class ChapterManager:
    def __init__(self, parent, book_path, load_chapter_callback):
        """Handles chapter selection, creation, and management."""
        self.parent = parent
        self.book_path = book_path
        self.chapters_path = os.path.join(book_path, "chapters")
        self.book_metadata_path = os.path.join(book_path, "book.json")
        self.load_chapter_callback = load_chapter_callback

        # 📑 UI Frame
        self.frame = tk.Frame(parent, padx=10, pady=10)
        self.frame.config(borderwidth=2, relief="groove")
        self.frame.grid(row=0, column=1, sticky="nsew")  # ✅ Used `.grid()`

        tk.Label(self.frame, text="📖 Chapters", font=("Arial", 12, "bold")).grid(
            row=0, column=0, columnspan=2, sticky="w", padx=5, pady=2
        )

        # 📜 Listbox for chapters
        self.chapter_listbox = tk.Listbox(self.frame, height=10)
        self.chapter_listbox.grid(
            row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5
        )
        self.chapter_listbox.bind("<<ListboxSelect>>", self.select_chapter)

        # 📌 Buttons for chapter management
        button_frame = tk.Frame(self.frame)
        button_frame.grid(
            row=2, column=0, columnspan=2, sticky="ew", pady=5
        )  # ✅ Used `.grid()`

        tk.Button(
            button_frame, text="📄 New Chapter", command=self.create_chapter
        ).grid(row=0, column=0, sticky="ew", padx=5)
        tk.Button(button_frame, text="✏ Rename", command=self.rename_chapter).grid(
            row=0, column=1, sticky="ew", padx=5
        )
        tk.Button(button_frame, text="🗑 Delete", command=self.delete_chapter).grid(
            row=0, column=2, sticky="ew", padx=5
        )

        # Configure resizing behavior
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)

        # Load existing chapters on startup
        self.load_chapters()

    def load_chapters(self):
        """Loads chapters from the book.json file."""
        self.chapter_listbox.delete(0, tk.END)

        if not os.path.exists(self.book_metadata_path):
            default_metadata = {
                "title": os.path.basename(self.book_path),
                "chapters": [],
                "media": [],
            }
            with open(self.book_metadata_path, "w", encoding="utf-8") as file:
                json.dump(default_metadata, file, indent=4)

        with open(self.book_metadata_path, "r", encoding="utf-8") as file:
            book_metadata = json.load(file)

        for chapter in book_metadata.get("chapters", []):
            self.chapter_listbox.insert(tk.END, chapter["title"])

    def select_chapter(self, event):
        """Loads the selected chapter's content."""
        selected_index = self.chapter_listbox.curselection()
        if not selected_index:
            return

        selected_title = self.chapter_listbox.get(selected_index[0])

        # Find the chapter filename
        with open(self.book_metadata_path, "r", encoding="utf-8") as file:
            book_metadata = json.load(file)

        for chapter in book_metadata.get("chapters", []):
            if chapter["title"] == selected_title:
                self.load_chapter_callback(chapter["filename"])
                return

    def create_chapter(self):
        """Creates a new chapter file and adds it to the book."""
        chapter_title = simpledialog.askstring("New Chapter", "Enter chapter title:")
        if not chapter_title:
            return

        filename = chapter_title.replace(" ", "_").lower() + ".md"
        chapter_path = os.path.join(self.chapters_path, filename)

        if os.path.exists(chapter_path):
            messagebox.showerror("Error", "A chapter with this name already exists.")
            return

        # Create new Markdown file
        with open(chapter_path, "w", encoding="utf-8") as file:
            file.write(f"# {chapter_title}\n\nWrite your content here...")

        # Update book.json
        with open(self.book_metadata_path, "r", encoding="utf-8") as file:
            book_metadata = json.load(file)

        book_metadata["chapters"].append({"title": chapter_title, "filename": filename})

        with open(self.book_metadata_path, "w", encoding="utf-8") as file:
            json.dump(book_metadata, file, indent=4)

        self.load_chapters()

    def rename_chapter(self):
        """Renames a selected chapter file."""
        selected_index = self.chapter_listbox.curselection()
        if not selected_index:
            return

        old_title = self.chapter_listbox.get(selected_index[0])
        new_title = simpledialog.askstring(
            "Rename Chapter", "Enter new title:", initialvalue=old_title
        )
        if not new_title or new_title == old_title:
            return

        # Find chapter in metadata
        with open(self.book_metadata_path, "r", encoding="utf-8") as file:
            book_metadata = json.load(file)

        for chapter in book_metadata["chapters"]:
            if chapter["title"] == old_title:
                old_filename = chapter["filename"]
                new_filename = new_title.replace(" ", "_").lower() + ".md"

                # Rename file
                old_path = os.path.join(self.chapters_path, old_filename)
                new_path = os.path.join(self.chapters_path, new_filename)

                if os.path.exists(new_path):
                    messagebox.showerror(
                        "Error", "A chapter with this name already exists."
                    )
                    return

                os.rename(old_path, new_path)
                chapter["title"] = new_title
                chapter["filename"] = new_filename
                break

        # Save changes
        with open(self.book_metadata_path, "w", encoding="utf-8") as file:
            json.dump(book_metadata, file, indent=4)

        self.load_chapters()

    def delete_chapter(self):
        """Deletes a selected chapter file and updates metadata."""
        selected_index = self.chapter_listbox.curselection()
        if not selected_index:
            return

        chapter_title = self.chapter_listbox.get(selected_index[0])

        if not messagebox.askyesno(
            "Delete Chapter", f"Are you sure you want to delete '{chapter_title}'?"
        ):
            return

        # Find chapter in metadata
        with open(self.book_metadata_path, "r", encoding="utf-8") as file:
            book_metadata = json.load(file)

        for chapter in book_metadata["chapters"]:
            if chapter["title"] == chapter_title:
                chapter_filename = chapter["filename"]
                chapter_path = os.path.join(self.chapters_path, chapter_filename)

                # Delete file
                if os.path.exists(chapter_path):
                    os.remove(chapter_path)

                # Remove from metadata
                book_metadata["chapters"].remove(chapter)
                break

        # Save changes
        with open(self.book_metadata_path, "w", encoding="utf-8") as file:
            json.dump(book_metadata, file, indent=4)

        self.load_chapters()
