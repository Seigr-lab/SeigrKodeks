import re

def detect_format(text):
    """Detect whether the given text is Markdown or MediaWiki syntax."""
    # MediaWiki patterns (e.g., headings, bold, links)
    mediawiki_patterns = [
        r'==[^=]+==',  # MediaWiki headings
        r"'''.+?'''",  # Bold text
        r'\[\[.+?\]\]',  # Internal links
    ]
    
    # Markdown patterns (e.g., headings, links, lists)
    markdown_patterns = [
        r'^#{1,6} ',  # Markdown headings
        r'\*\*.+?\*\*',  # Bold text
        r'\[.+?\]\(.+?\)',  # Links
    ]
    
    # Check for MediaWiki syntax
    for pattern in mediawiki_patterns:
        if re.search(pattern, text):
            return "mediawiki"
    
    # Check for Markdown syntax
    for pattern in markdown_patterns:
        if re.search(pattern, text):
            return "markdown"
    
    return "unknown"  # Default if no format is identified

# Example usage
if __name__ == "__main__":
    sample_mw = "== Heading ==\n'''Bold text'''\n[[Link]]"
    sample_md = "# Heading\n**Bold text**\n[Link](url)"
    
    print("Detected format (MW):", detect_format(sample_mw))
    print("Detected format (MD):", detect_format(sample_md))