import tkinter as tk
from tkinter import scrolledtext, simpledialog, filedialog, messagebox
import os
from seigr_kodeks.parsers.format_detector import detect_format

class SeigrKodeksApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SeigrKodeks - Book Creator")
        self.root.geometry("900x600")
        
        # Book title and directory selection
        self.book_title = ""
        self.book_directory = ""
        self.chapters = []
        
        # UI Layout
        self.create_ui()
    
    def create_ui(self):
        # Book Selection
        self.book_frame = tk.Frame(self.root)
        self.book_frame.pack(pady=5)
        
        tk.Label(self.book_frame, text="Book Title: ").pack(side=tk.LEFT)
        self.book_title_label = tk.Label(self.book_frame, text="(No book selected)", fg="blue")
        self.book_title_label.pack(side=tk.LEFT)
        tk.Button(self.book_frame, text="Create/Open Book", command=self.select_book).pack(side=tk.LEFT, padx=10)
        
        # Chapter List
        self.chapter_listbox = tk.Listbox(self.root, height=10)
        self.chapter_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.chapter_listbox.bind("<<ListboxSelect>>", self.load_chapter)
        
        # Chapter Management Buttons
        self.chapter_buttons = tk.Frame(self.root)
        self.chapter_buttons.pack()
        tk.Button(self.chapter_buttons, text="Add Chapter", command=self.add_chapter).pack(side=tk.LEFT, padx=5)
        tk.Button(self.chapter_buttons, text="Delete Chapter", command=self.delete_chapter).pack(side=tk.LEFT, padx=5)
        
        # Markdown Editor with Formatting Buttons
        self.editor_frame = tk.Frame(self.root)
        self.editor_frame.pack(pady=5)
        
        tk.Button(self.editor_frame, text="Bold", command=lambda: self.insert_markdown('**', '**')).pack(side=tk.LEFT, padx=2)
        tk.Button(self.editor_frame, text="Italic", command=lambda: self.insert_markdown('*', '*')).pack(side=tk.LEFT, padx=2)
        tk.Button(self.editor_frame, text="Link", command=self.insert_link).pack(side=tk.LEFT, padx=2)
        tk.Button(self.editor_frame, text="Image", command=self.insert_image).pack(side=tk.LEFT, padx=2)
        tk.Button(self.editor_frame, text="Heading", command=self.insert_heading).pack(side=tk.LEFT, padx=2)
        
        # Chapter Editor
        self.text_input = scrolledtext.ScrolledText(self.root, height=10)
        self.text_input.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Convert & Save
        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack(pady=10)
        tk.Button(self.bottom_frame, text="Convert to Markdown", command=self.convert_text).pack(side=tk.LEFT, padx=5)
        tk.Button(self.bottom_frame, text="Save Chapter", command=self.save_chapter).pack(side=tk.LEFT, padx=5)
        
        self.status_label = tk.Label(self.root, text="", fg="green")
        self.status_label.pack()
    
    def insert_markdown(self, prefix, suffix):
        self.text_input.insert(tk.INSERT, f"{prefix}TEXT{suffix}")
    
    def insert_link(self):
        self.text_input.insert(tk.INSERT, "[Link Text](http://example.com)")
    
    def insert_image(self):
        self.text_input.insert(tk.INSERT, "![Alt Text](image.jpg)")
    
    def insert_heading(self):
        self.text_input.insert(tk.INSERT, "# Heading\n")
    
    def select_book(self):
        book_directory = filedialog.askdirectory(title="Select Book Directory")
        if book_directory:
            self.book_directory = book_directory
            self.book_title = os.path.basename(book_directory)
            self.book_title_label.config(text=self.book_title)
            self.load_chapters()
    
    def load_chapters(self):
        self.chapters = [f for f in os.listdir(self.book_directory) if f.endswith(".md")]
        self.chapter_listbox.delete(0, tk.END)
        for chapter in self.chapters:
            self.chapter_listbox.insert(tk.END, chapter.replace(".md", ""))
    
    def add_chapter(self):
        chapter_name = simpledialog.askstring("New Chapter", "Enter chapter title:")
        if chapter_name:
            chapter_filename = chapter_name.replace(" ", "_") + ".md"
            chapter_path = os.path.join(self.book_directory, chapter_filename)
            open(chapter_path, "w").close()
            self.chapters.append(chapter_filename)
            self.chapter_listbox.insert(tk.END, chapter_name)
    
    def convert_text(self):
        input_text = self.text_input.get("1.0", tk.END).strip()
        if not input_text:
            messagebox.showwarning("Warning", "Please enter text to convert.")
            return
        
        detected_format, converted_text = detect_format(input_text)
        
        self.text_input.delete("1.0", tk.END)
        self.text_input.insert(tk.INSERT, converted_text)
        
        self.status_label.config(text=f"Converted from {detected_format}", fg="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = SeigrKodeksApp(root)
    root.mainloop()
