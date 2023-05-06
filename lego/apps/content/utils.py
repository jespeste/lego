import bleach


def sanitize_html(value, allow_images=True):
    """
    Remove dangerous tags from HTML.
    """
    tags = [
        "p",
        "b",
        "i",
        "u",
        "s",
        "h1",
        "h2",
        "h3",
        "code",
        "pre",
        "blockquote",
        "strong",
        "strike",
        "ul",
        "cite",
        "li",
        "em",
        "hr",
        "div",
        "a",
        "figure",
        "figcaption",
        "input",
        "ol",
        "br",
    ]
    if allow_images:
        tags.append("img")

    safe_content = bleach.clean(
        value,
        tags=tags,
        attributes={
            "div": ["data-type"],
            "a": ["href", "target", "rel"],
            "input": ["type", "disabled", "checked"],
            "img": ["data-file-key"],
        },
        strip=True,
        strip_comments=True,
    )
    return safe_content
