import os
import json
import shutil
from tkinter import filedialog, messagebox


def ensure_book_structure(book_path):
    """Ensure necessary folders and book metadata exist."""
    chapters_dir = os.path.join(book_path, "chapters")
    media_dir = os.path.join(book_path, "media")
    os.makedirs(chapters_dir, exist_ok=True)
    os.makedirs(media_dir, exist_ok=True)

    book_metadata_path = os.path.join(book_path, "book.json")
    if not os.path.exists(book_metadata_path):
        book_metadata = {
            "title": os.path.basename(book_path),
            "chapters": [],
            "media": [],
        }
        save_book_metadata(book_metadata, book_metadata_path)

    return book_metadata_path


def load_book_metadata(book_path):
    """Load the book metadata file."""
    book_metadata_path = ensure_book_structure(book_path)

    with open(book_metadata_path, "r", encoding="utf-8") as file:
        return json.load(file), book_metadata_path


def save_book_metadata(metadata, book_metadata_path):
    """Save book metadata to the JSON file."""
    with open(book_metadata_path, "w", encoding="utf-8") as file:
        json.dump(metadata, file, indent=4)


def add_chapter(book_path, chapter_title):
    """Create a new chapter and update metadata."""
    metadata, book_metadata_path = load_book_metadata(book_path)

    chapter_filename = chapter_title.replace(" ", "_") + ".md"
    chapter_path = os.path.join(book_path, "chapters", chapter_filename)

    if chapter_filename not in [ch["filename"] for ch in metadata["chapters"]]:
        open(chapter_path, "w").close()
        metadata["chapters"].append(
            {"title": chapter_title, "filename": chapter_filename}
        )
        save_book_metadata(metadata, book_metadata_path)
        return chapter_title
    else:
        messagebox.showwarning("Warning", "A chapter with this name already exists.")
        return None


def delete_chapter(book_path, chapter_title):
    """Delete a chapter and update metadata."""
    metadata, book_metadata_path = load_book_metadata(book_path)

    for chapter in metadata["chapters"]:
        if chapter["title"] == chapter_title:
            chapter_path = os.path.join(book_path, "chapters", chapter["filename"])
            if os.path.exists(chapter_path):
                os.remove(chapter_path)
            metadata["chapters"].remove(chapter)
            save_book_metadata(metadata, book_metadata_path)
            return True

    messagebox.showwarning("Warning", "Chapter not found.")
    return False


def rename_chapter(book_path, old_title, new_title):
    """Rename a chapter and update metadata."""
    metadata, book_metadata_path = load_book_metadata(book_path)

    for chapter in metadata["chapters"]:
        if chapter["title"] == old_title:
            old_filename = chapter["filename"]
            new_filename = new_title.replace(" ", "_") + ".md"

            old_path = os.path.join(book_path, "chapters", old_filename)
            new_path = os.path.join(book_path, "chapters", new_filename)

            if os.path.exists(old_path):
                os.rename(old_path, new_path)

            chapter["title"] = new_title
            chapter["filename"] = new_filename
            save_book_metadata(metadata, book_metadata_path)
            return True

    messagebox.showwarning("Warning", "Chapter not found.")
    return False


def reorder_chapters(book_path, old_index, new_index):
    """Reorder chapters within the book metadata."""
    metadata, book_metadata_path = load_book_metadata(book_path)

    if 0 <= old_index < len(metadata["chapters"]) and 0 <= new_index < len(
        metadata["chapters"]
    ):
        chapter = metadata["chapters"].pop(old_index)
        metadata["chapters"].insert(new_index, chapter)
        save_book_metadata(metadata, book_metadata_path)
        return True

    messagebox.showwarning("Warning", "Invalid chapter indices.")
    return False


def organize_files(book_path):
    """Ensure all Markdown and media files are properly placed."""
    ensure_book_structure(book_path)
    metadata, book_metadata_path = load_book_metadata(book_path)

    chapters_dir = os.path.join(book_path, "chapters")
    media_dir = os.path.join(book_path, "media")

    for file in os.listdir(book_path):
        file_path = os.path.join(book_path, file)

        if file.endswith(".md") and file not in [
            ch["filename"] for ch in metadata["chapters"]
        ]:
            shutil.move(file_path, os.path.join(chapters_dir, file))

        elif file.lower().endswith(
            (".png", ".jpg", ".jpeg", ".gif", ".mp3", ".wav", ".mp4", ".webm", ".ogg")
        ):
            if file not in [m["filename"] for m in metadata.get("media", [])]:
                shutil.move(file_path, os.path.join(media_dir, file))
                metadata["media"].append({"type": "Unknown", "filename": file})

    save_book_metadata(metadata, book_metadata_path)
    messagebox.showinfo("Success", "All files have been organized correctly.")
