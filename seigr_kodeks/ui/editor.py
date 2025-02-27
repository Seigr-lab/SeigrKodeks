import os
import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkhtmlview import HTMLLabel
import markdown


class MarkdownEditor:
    def __init__(self, parent, book_path):
        """Markdown editor with live preview."""
        self.parent = parent
        self.book_path = book_path
        self.current_chapter = None
        self.chapter_path = None

        # 📝 Frame
        self.frame = tk.Frame(parent, padx=10, pady=10)
        self.frame.config(borderwidth=2, relief="groove")
        self.frame.grid(row=0, column=1, rowspan=2, sticky="nsew")  # ✅ Used `.grid()`

        # 📑 Title Label
        self.title_label = tk.Label(
            self.frame, text="📝 Editor", font=("Arial", 12, "bold")
        )
        self.title_label.grid(
            row=0, column=0, columnspan=2, sticky="w", padx=5, pady=2
        )  # ✅ Used `.grid()`

        # ✍ Markdown Text Editor
        self.text_editor = scrolledtext.ScrolledText(
            self.frame, wrap=tk.WORD, font=("Courier", 12), undo=True
        )
        self.text_editor.grid(
            row=1, column=0, sticky="nsew", padx=5, pady=5
        )  # ✅ Used `.grid()`
        self.text_editor.bind("<KeyRelease>", self.auto_save)

        # 🌍 Live Markdown Preview
        self.preview = HTMLLabel(self.frame, background="white", padx=5, pady=5)
        self.preview.grid(
            row=1, column=1, sticky="nsew", padx=5, pady=5
        )  # ✅ Used `.grid()`

        # 📌 Buttons
        button_frame = tk.Frame(self.frame)
        button_frame.grid(
            row=2, column=0, columnspan=2, sticky="ew", pady=5
        )  # ✅ Used `.grid()`

        tk.Button(button_frame, text="💾 Save", command=self.save_chapter).grid(
            row=0, column=0, sticky="ew", padx=5
        )
        tk.Button(
            button_frame, text="🔄 Refresh Preview", command=self.update_preview
        ).grid(row=0, column=1, sticky="ew", padx=5)

        # Configure resizing behavior
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def load_chapter(self, filename):
        """Loads a chapter into the editor."""
        self.current_chapter = filename
        self.chapter_path = os.path.join(self.book_path, "chapters", filename)

        if not os.path.exists(self.chapter_path):
            messagebox.showerror("Error", "Chapter file not found!")
            return

        with open(self.chapter_path, "r", encoding="utf-8") as file:
            content = file.read()

        self.text_editor.delete("1.0", tk.END)
        self.text_editor.insert(tk.END, content)

        self.update_preview()

    def save_chapter(self):
        """Saves the chapter content to the file."""
        if not self.current_chapter:
            return

        content = self.text_editor.get("1.0", tk.END).strip()

        with open(self.chapter_path, "w", encoding="utf-8") as file:
            file.write(content)

        messagebox.showinfo("Saved", "Chapter saved successfully!")

    def update_preview(self):
        """Updates the live preview of the Markdown."""
        markdown_text = self.text_editor.get("1.0", tk.END).strip()
        html_content = markdown.markdown(
            markdown_text, extensions=["fenced_code", "tables", "toc"]
        )
        self.preview.set_html(html_content)

    def auto_save(self, event=None):
        """Auto-saves the chapter on key release."""
        if self.current_chapter:
            self.save_chapter()
