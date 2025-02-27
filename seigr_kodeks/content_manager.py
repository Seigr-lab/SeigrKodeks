import os
import json
import markdown
from seigr_kodeks.parsers.format_detector import detect_format


def load_chapter(book_path, chapter_filename):
    """Load the content of a chapter file."""
    chapter_path = os.path.join(book_path, "chapters", chapter_filename)

    if os.path.exists(chapter_path):
        with open(chapter_path, "r", encoding="utf-8") as file:
            return file.read()

    return ""


def save_chapter(book_path, chapter_filename, content):
    """Save the content of a chapter file."""
    chapter_path = os.path.join(book_path, "chapters", chapter_filename)

    with open(chapter_path, "w", encoding="utf-8") as file:
        file.write(content)


def convert_to_markdown(text):
    """Convert input text (MediaWiki or Markdown) to clean Markdown."""
    detected_format, converted_text = detect_format(text)
    return converted_text, detected_format


def render_markdown_to_html(markdown_text):
    """Convert Markdown text to HTML for previewing."""
    return markdown.markdown(markdown_text, extensions=["extra", "toc", "codehilite"])


def update_chapter_references(book_path):
    """
    Ensure all chapter links are properly formatted within the book.
    Converts:
    - `[[Chapter Name]]` → `[Chapter Name](Chapter_Name.md)`
    - `![[Image.jpg]]` → `![Image](media/Image.jpg)`
    """
    metadata_path = os.path.join(book_path, "book.json")
    with open(metadata_path, "r", encoding="utf-8") as file:
        metadata = json.load(file)

    for chapter in metadata["chapters"]:
        chapter_path = os.path.join(book_path, "chapters", chapter["filename"])
        if not os.path.exists(chapter_path):
            continue

        with open(chapter_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Replace internal chapter links
        for other_chapter in metadata["chapters"]:
            if f"[[{other_chapter['title']}]]" in content:
                content = content.replace(
                    f"[[{other_chapter['title']}]]",
                    f"[{other_chapter['title']}]({other_chapter['filename']})",
                )

        # Replace embedded media links
        for media in metadata.get("media", []):
            if f"![[{media['filename']}]]" in content:
                content = content.replace(
                    f"![[{media['filename']}]]",
                    f"![{media['filename']}]({os.path.join('media', media['filename'])})",
                )

        # Save updated content
        with open(chapter_path, "w", encoding="utf-8") as file:
            file.write(content)


def format_markdown_text(markdown_text, format_type):
    """
    Apply basic formatting to text input.
    - "bold": Wraps **selected text** in `**bold**`
    - "italic": Wraps *selected text* in `*italic*`
    - "link": Adds `[Link Text](http://example.com)`
    - "image": Inserts `![Alt Text](image.jpg)`
    - "code": Wraps in triple backticks for code blocks.
    """
    formatting_options = {
        "bold": "**TEXT**",
        "italic": "*TEXT*",
        "link": "[Link Text](http://example.com)",
        "image": "![Alt Text](image.jpg)",
        "code": "```\nCODE\n```",
    }

    return markdown_text + "\n" + formatting_options.get(format_type, "")
