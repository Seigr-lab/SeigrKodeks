import tkinter as tk
from tkinter import messagebox
from seigr_kodeks.ui.main_window import SeigrKodeksMainWindow
from seigr_kodeks.storage_manager import (
    load_preferences,
    select_storage_path,
    save_preferences,
)
import os


class SeigrKodeksApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SeigrKodeks - Book Creator")
        self.root.geometry("1200x700")

        # Load preferences
        self.preferences = load_preferences()
        self.storage_path = self.preferences.get("storage_path", "")
        if not self.storage_path:
            self.storage_path = select_storage_path()
            if self.storage_path:
                self.preferences["storage_path"] = self.storage_path
                save_preferences(self.preferences)

        # Ensure book storage exists
        self.books_directory = os.path.join(self.storage_path, "SeKo_Books")
        os.makedirs(self.books_directory, exist_ok=True)

        try:
            self.main_window = SeigrKodeksMainWindow(self.root, self.books_directory)
        except Exception as e:
            print(f"⚠ Error: {str(e)}")  # Log error to console
            messagebox.showerror("Error", f"Failed to initialize UI: {str(e)}")
            self.root.quit()  # Ensure Tkinter exits cleanly


if __name__ == "__main__":
    root = tk.Tk()
    app = SeigrKodeksApp(root)
    root.mainloop()
