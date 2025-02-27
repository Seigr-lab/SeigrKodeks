import tkinter as tk
from seigr_kodeks.ui.book_manager import BookManager
from seigr_kodeks.ui.chapter_manager import ChapterManager
from seigr_kodeks.ui.editor import MarkdownEditor
from seigr_kodeks.ui.toolbar import Toolbar
from seigr_kodeks.file_manager import organize_files
from seigr_kodeks.exporter import export_to_html, preview_html
from tkinter import messagebox
import os


class SeigrKodeksMainWindow:
    def __init__(self, root, books_directory):
        """Initialize the main application window with all components."""
        self.root = root
        self.books_directory = books_directory
        self.book_path = None  # Current book path
        self.current_chapter = None  # Currently opened chapter

        # Ensure UI works even if no books exist
        self.create_layout()

    def create_layout(self):
        """Creates the main layout of the application."""
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # 📂 Book Manager (left panel)
        self.book_manager = BookManager(self.root, self.books_directory, self.load_book)
        self.book_manager.frame.grid(row=0, column=0, rowspan=2, sticky="ns")

        # 📖 Chapter Manager (middle panel) - Only create if a book is selected!
        book_path = self.get_selected_book_path()
        if book_path:
            self.chapter_manager = ChapterManager(
                self.root, book_path, self.load_chapter
            )
            self.chapter_manager.frame.grid(row=0, column=1, rowspan=2, sticky="nsew")
        else:
            self.chapter_manager = None  # Do not initialize

        # 🖊️ Markdown Editor (right panel)
        self.editor = MarkdownEditor(self.root, self.save_chapter)
        self.editor.frame.grid(row=0, column=2, sticky="nsew")

        # 🎨 Toolbar (top panel) - Ensure it doesn't depend on `chapter_manager`
        self.toolbar = Toolbar(self.root, self.book_manager, self.editor)
        self.toolbar.frame.grid(row=1, column=2, sticky="ew")

    def load_book(self, book_path):
        """Loads a book when selected from the book manager."""
        if not book_path or not os.path.exists(book_path):
            messagebox.showerror(
                "Error", "Invalid book path. Please select a valid book."
            )
            return

        self.book_path = book_path
        self.chapter_manager.set_book_path(book_path)
        self.chapter_manager.load_chapters()
        self.editor.clear_editor()
        self.root.title(f"SeigrKodeks - {os.path.basename(book_path)}")

    def get_selected_book_path(self):
        """Returns the currently selected book path or an empty string."""
        return self.book_manager.get_selected_book_path() or ""

    def load_chapter(self, chapter_filename):
        """Loads the selected chapter into the editor."""
        if not self.book_path:
            messagebox.showerror(
                "Error", "No book selected. Please open or create a book first."
            )
            return

        chapter_path = os.path.join(self.book_path, "chapters", chapter_filename)
        if not os.path.exists(chapter_path):
            messagebox.showerror("Error", "Chapter file not found.")
            return

        self.current_chapter = chapter_path
        with open(chapter_path, "r", encoding="utf-8") as file:
            content = file.read()
        self.editor.load_content(content)

    def save_chapter(self, content):
        """Saves the current chapter."""
        if not self.current_chapter:
            messagebox.showerror("Error", "No chapter selected to save.")
            return

        with open(self.current_chapter, "w", encoding="utf-8") as file:
            file.write(content)

    def insert_media(self, media_type):
        """Handles media insertion into the editor."""
        if not self.book_path:
            messagebox.showerror(
                "Error", "No book selected. Please open or create a book first."
            )
            return

        media_path = self.toolbar.insert_media(self.book_path, media_type)
        if media_path:
            self.editor.insert_text(media_path)

    def export_book(self):
        """Exports the current book to HTML format."""
        if not self.book_path:
            messagebox.showerror("Error", "No book selected to export.")
            return

        organize_files(self.book_path)
        export_to_html(self.book_path)
        preview_html(self.book_path)
