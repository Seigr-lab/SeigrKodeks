import os
import shutil
from tkinter import filedialog, messagebox


def ensure_media_folder(book_path):
    """Ensure the media directory exists within the book's folder."""
    media_dir = os.path.join(book_path, "media")
    os.makedirs(media_dir, exist_ok=True)
    return media_dir


def insert_media(book_path, media_type, file_types):
    """Allow user to select a media file and move it to the book's media directory."""
    if not book_path:
        messagebox.showwarning("Warning", "No book selected.")
        return None  # No book path selected

    file_path = filedialog.askopenfilename(
        title=f"Select {media_type} File",
        filetypes=[(f"{media_type} Files", file_types)],
    )

    if not file_path:
        return None  # User canceled selection

    media_dir = ensure_media_folder(book_path)

    file_name = os.path.basename(file_path)
    dest_path = os.path.join(media_dir, file_name)

    if not os.path.exists(dest_path):
        shutil.copy(file_path, dest_path)

    # Return the appropriate Markdown syntax
    if media_type == "Image":
        markdown_syntax = f"![Alt Text](media/{file_name})"
    elif media_type == "Audio":
        markdown_syntax = f"<audio controls><source src='media/{file_name}' type='audio/mpeg'></audio>"
    elif media_type == "Video":
        markdown_syntax = (
            f"<video controls><source src='media/{file_name}' type='video/mp4'></video>"
        )
    else:
        markdown_syntax = None

    return markdown_syntax


def delete_media(book_path, file_name):
    """Delete a media file from the book's media directory."""
    media_path = os.path.join(book_path, "media", file_name)

    if os.path.exists(media_path):
        os.remove(media_path)
        messagebox.showinfo("Success", f"Deleted: {file_name}")
    else:
        messagebox.showwarning("Warning", f"File not found: {file_name}")


def insert_image(book_path):
    """Handles image insertion and returns the markdown syntax."""
    return insert_media(book_path, "Image", "*.png;*.jpg;*.jpeg;*.gif")


def insert_audio(book_path):
    """Handles audio insertion and returns the markdown syntax."""
    return insert_media(book_path, "Audio", "*.mp3;*.wav")


def insert_video(book_path):
    """Handles video insertion and returns the markdown syntax."""
    return insert_media(book_path, "Video", "*.mp4;*.webm;*.ogg")
