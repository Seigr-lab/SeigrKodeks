import re
import sys
import os

# Ensure the parent directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Now import the module
from seigr_kodeks.parsers.mediawiki_to_md import mediawiki_to_markdown


def detect_format(text):
    """Detect whether the given text is Markdown or MediaWiki syntax and convert MediaWiki to Markdown."""
    # MediaWiki patterns (e.g., headings, bold, links)
    mediawiki_patterns = [
        r"==[^=]+==",  # MediaWiki headings
        r"'''.+?'''",  # Bold text
        r"\[\[.+?\]\]",  # Internal links
    ]

    # Markdown patterns (e.g., headings, links, lists)
    markdown_patterns = [
        r"^#{1,6} ",  # Markdown headings
        r"\*\*.+?\*\*",  # Bold text
        r"\[.+?\]\(.+?\)",  # Links
    ]

    # Check for MediaWiki syntax
    for pattern in mediawiki_patterns:
        if re.search(pattern, text):
            return "markdown", mediawiki_to_markdown(
                text
            )  # Convert MediaWiki to Markdown

    # Check for Markdown syntax
    for pattern in markdown_patterns:
        if re.search(pattern, text):
            return "markdown", text  # Already Markdown, return as-is

    return "unknown", text  # Default if no format is identified


# Example usage
if __name__ == "__main__":
    sample_mw = "== Heading ==\n'''Bold text'''\n[[Link]]"
    sample_md = "# Heading\n**Bold text**\n[Link](url)"

    detected_format, converted_text = detect_format(sample_mw)
    print(f"Detected format: {detected_format}\nConverted Text:\n{converted_text}\n")

    detected_format, converted_text = detect_format(sample_md)
    print(f"Detected format: {detected_format}\nConverted Text:\n{converted_text}")
