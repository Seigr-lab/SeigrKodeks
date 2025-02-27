import re


def mediawiki_to_markdown(text):
    """Converts MediaWiki syntax to Markdown."""

    # Convert headings (== Heading == to # Heading)
    text = re.sub(r"==([^=]+)==", r"# \1", text)
    text = re.sub(r"===([^=]+)===", r"## \1", text)
    text = re.sub(r"====([^=]+)====", r"### \1", text)

    # Convert bold ('''bold''' → **bold**)
    text = re.sub(r"'''''(.*?)'''''", r"***\1***", text)  # Bold + Italic
    text = re.sub(r"'''(.*?)'''", r"**\1**", text)  # Bold

    # Convert italics (''italic'' → *italic*)
    text = re.sub(r"''(.*?)''", r"*\1*", text)

    # Convert MediaWiki links ([[Page|Text]] → [Text](Page))
    text = re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", r"[\2](\1)", text)  # Named link
    text = re.sub(r"\[\[([^\]]+)\]\]", r"[\1](\1)", text)  # Direct link

    # Convert lists (* or # to Markdown format)
    text = re.sub(r"\n\* ", "\n- ", text)  # Unordered list
    text = re.sub(r"\n# ", "\n1. ", text)  # Ordered list

    return text


# Example usage
if __name__ == "__main__":
    sample_mediawiki = """
    == Heading ==
    '''Bold Text'''
    ''Italic Text''
    [[Page|Link Text]]
    * Item 1
    # Numbered Item 1
    """

    print("Converted Markdown:")
    print(mediawiki_to_markdown(sample_mediawiki))
