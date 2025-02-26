import os
import markdown
from bs4 import BeautifulSoup

class MarkdownParser:
    def __init__(self, chapters_dir="chapters"):
        self.chapters_dir = chapters_dir
    
    def read_markdown_file(self, filename):
        """Reads a Markdown file and returns its content."""
        filepath = os.path.join(self.chapters_dir, filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Markdown file not found: {filepath}")
        
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    
    def convert_to_html(self, markdown_text):
        """Converts Markdown text to HTML."""
        return markdown.markdown(markdown_text, extensions=["fenced_code", "tables", "toc"])
    
    def extract_metadata(self, markdown_text):
        """Extracts metadata such as title, headings, and images."""
        html_content = self.convert_to_html(markdown_text)
        soup = BeautifulSoup(html_content, "html.parser")
        
        title = soup.find("h1").text if soup.find("h1") else "Untitled"
        headings = [h.text for h in soup.find_all(["h2", "h3", "h4"])]
        images = [img["src"] for img in soup.find_all("img")]
        
        return {
            "title": title,
            "headings": headings,
            "images": images
        }
    
    def parse_markdown_file(self, filename):
        """Reads and processes a Markdown file, returning parsed data."""
        markdown_text = self.read_markdown_file(filename)
        metadata = self.extract_metadata(markdown_text)
        html = self.convert_to_html(markdown_text)
        
        return {
            "metadata": metadata,
            "html": html
        }

if __name__ == "__main__":
    parser = MarkdownParser()
    test_filename = "example.md"  # Place a sample file in `chapters/`
    try:
        result = parser.parse_markdown_file(test_filename)
        print("Title:", result["metadata"]["title"])
        print("Headings:", result["metadata"]["headings"])
        print("Images:", result["metadata"]["images"])
        print("HTML Output:\n", result["html"][:500])  # Preview first 500 chars
    except FileNotFoundError as e:
        print(e)
