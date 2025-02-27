import os
import json
from tkinter import filedialog, messagebox

# Define the preferences file name
PREFS_FILE = os.path.expanduser("~/.seigrkodeks_prefs.json")

def load_preferences():
    """Load user preferences from the preferences JSON file."""
    if os.path.exists(PREFS_FILE):
        try:
            with open(PREFS_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Failed to load preferences file. Resetting preferences.")
            return {"storage_path": "", "recent_books": []}
    return {"storage_path": "", "recent_books": []}

def save_preferences(prefs):
    """Save user preferences to the preferences JSON file."""
    try:
        with open(PREFS_FILE, "w", encoding="utf-8") as file:
            json.dump(prefs, file, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save preferences: {e}")

def select_storage_path():
    """Ask the user to select a storage location for SeigrKodeks books."""
    messagebox.showinfo(
        "Storage Selection",
        "Please select a storage location where all your SeigrKodeks books will be stored."
    )
    
    storage_path = filedialog.askdirectory(title="Select SeigrKodeks Storage Location")
    
    if storage_path:
        prefs = load_preferences()
        prefs["storage_path"] = storage_path
        save_preferences(prefs)
        return storage_path
    else:
        messagebox.showwarning("Warning", "No storage location selected. Defaulting to home directory.")
        return os.path.expanduser("~/SeKo_Books")

def get_storage_path():
    """Retrieve the currently set storage path from preferences."""
    prefs = load_preferences()
    return prefs.get("storage_path", "")

def get_recent_books():
    """Retrieve a list of recently accessed books."""
    prefs = load_preferences()
    return prefs.get("recent_books", [])

def add_recent_book(book_path):
    """Add a book to the list of recently accessed books."""
    prefs = load_preferences()
    
    if book_path not in prefs["recent_books"]:
        prefs["recent_books"].insert(0, book_path)  # Add to the top
        prefs["recent_books"] = prefs["recent_books"][:5]  # Keep only the last 5 books
    
    save_preferences(prefs)
