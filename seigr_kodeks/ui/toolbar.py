import tkinter as tk
import os
from tkinter import ttk, filedialog, messagebox
from seigr_kodeks.ui.chapter_manager import ChapterManager
from seigr_kodeks.exporter import export_to_html, preview_html
from seigr_kodeks.media_manager import insert_image, insert_audio, insert_video


class Toolbar:
    def __init__(self, parent, book_manager, editor):
        """Main toolbar with book, chapter, media, and export controls."""
        self.parent = parent
        self.book_manager = book_manager
        self.editor = editor

        # 🛠️ Toolbar Frame (Now using `grid()`)
        self.frame = tk.Frame(parent, padx=5, pady=5, relief=tk.RIDGE, borderwidth=2)
        self.frame.grid(
            row=1, column=0, columnspan=3, sticky="ew"
        )  # ✅ Replaced `.pack()`

        # 📚 Book Management
        self.book_menu = ttk.Menubutton(self.frame, text="📚 Book", direction="below")
        self.book_menu.menu = tk.Menu(self.book_menu, tearoff=False)
        self.book_menu["menu"] = self.book_menu.menu

        self.book_menu.menu.add_command(
            label="📂 Open Book", command=self.book_manager.open_book
        )
        self.book_menu.menu.add_command(
            label="📖 New Book", command=self.book_manager.create_book
        )
        self.book_menu.menu.add_separator()
        self.book_menu.menu.add_command(
            label="💾 Save Book", command=self.book_manager.save_book_metadata
        )
        self.book_menu.grid(
            row=0, column=0, padx=5, pady=2
        )  # ✅ Changed `.pack()` to `.grid()`

        # 🎬 Media Buttons
        tk.Button(
            self.frame,
            text="📷 Image",
            command=lambda: insert_image(self.book_manager.get_selected_book_path()),
        ).grid(row=0, column=1, padx=2)
        tk.Button(
            self.frame,
            text="🎵 Audio",
            command=lambda: insert_audio(self.book_manager.get_selected_book_path()),
        ).grid(row=0, column=2, padx=2)
        tk.Button(
            self.frame,
            text="🎬 Video",
            command=lambda: insert_video(self.book_manager.get_selected_book_path()),
        ).grid(row=0, column=3, padx=2)

        # 🌍 Export & Preview
        tk.Button(
            self.frame,
            text="🔄 Preview",
            command=lambda: preview_html(self.book_manager.get_selected_book_path()),
        ).grid(row=0, column=4, padx=5)
        tk.Button(
            self.frame,
            text="🌍 Export",
            command=lambda: export_to_html(self.book_manager.get_selected_book_path()),
        ).grid(row=0, column=5, padx=5)

    def insert_format(self, text):
        """Insert Markdown formatting into the editor."""
        self.editor.text_editor.insert(tk.INSERT, text)

    def add_chapter(self):
        """Add a new chapter using ChapterManager."""
        chapter_name = filedialog.asksaveasfilename(
            defaultextension=".md", title="Create New Chapter"
        )
        if chapter_name:
            self.chapter_manager.create_chapter()
            self.book_manager.refresh_chapter_list()

    def delete_chapter(self):
        """Delete selected chapter."""
        selected_chapter = self.book_manager.get_selected_chapter()
        if selected_chapter:
            self.chapter_manager.delete_chapter()
            self.book_manager.refresh_chapter_list()

    def rename_chapter(self):
        """Rename selected chapter."""
        selected_chapter = self.book_manager.get_selected_chapter()
        if selected_chapter:
            self.chapter_manager.rename_chapter()
            self.book_manager.refresh_chapter_list()
