import os
import markdown
from bs4 import BeautifulSoup


class MarkdownParser:
    def __init__(self, book_path):
        self.book_path = book_path
        self.chapters_dir = os.path.join(book_path, "chapters")

    def read_markdown_file(self, filename):
        """Reads a Markdown file and returns its content."""
        filepath = os.path.join(self.chapters_dir, filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Markdown file not found: {filepath}")

        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()

    def convert_to_html(self, markdown_text):
        """Converts Markdown text to HTML with additional processing."""
        return markdown.markdown(
            markdown_text,
            extensions=[
                "fenced_code",
                "tables",
                "toc",
                "sane_lists",
                "nl2br",
                "attr_list",
            ],
        )

    def extract_metadata(self, markdown_text):
        """Extracts metadata such as title, headings, images, and links."""
        html_content = self.convert_to_html(markdown_text)
        soup = BeautifulSoup(html_content, "html.parser")

        title = soup.find("h1").text if soup.find("h1") else "Untitled"
        headings = {h.name: h.text for h in soup.find_all(["h1", "h2", "h3", "h4"])}
        images = [img["src"] for img in soup.find_all("img") if "src" in img.attrs]
        links = [a["href"] for a in soup.find_all("a") if "href" in a.attrs]

        return {"title": title, "headings": headings, "images": images, "links": links}

    def parse_markdown_file(self, filename):
        """Reads and processes a Markdown file, returning parsed metadata and HTML."""
        markdown_text = self.read_markdown_file(filename)
        metadata = self.extract_metadata(markdown_text)
        html = self.convert_to_html(markdown_text)

        return {"metadata": metadata, "html": html}


if __name__ == "__main__":
    # Example usage
    book_directory = "path/to/book"  # Adjust based on actual project directory
    parser = MarkdownParser(book_directory)

    test_filename = "example.md"  # Place a sample file in `chapters/`
    try:
        result = parser.parse_markdown_file(test_filename)
        print("Title:", result["metadata"]["title"])
        print("Headings:", result["metadata"]["headings"])
        print("Images:", result["metadata"]["images"])
        print("Links:", result["metadata"]["links"])
        print("HTML Output (Preview):\n", result["html"][:500])
    except FileNotFoundError as e:
        print(e)
