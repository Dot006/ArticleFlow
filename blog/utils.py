import re

import bleach
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension


ALLOWED_TAGS = [
    "p",
    "br",
    "strong",
    "em",
    "del",
    "blockquote",
    "ul",
    "ol",
    "li",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "a",
    "code",
    "pre",
    "div",
    "table",
    "thead",
    "tbody",
    "tr",
    "th",
    "td",
    "hr",
    "span",
]


ALLOWED_ATTRIBUTES = {
    "a": ["href", "title", "target", "rel"],
    "code": ["class"],
    "pre": ["class"],
    "div": ["class"],
    "span": ["class"],
}


def render_markdown(content):
    html = markdown.markdown(
        content,
        extensions=[
            "extra",
            "fenced_code",
            CodeHiliteExtension(
                css_class="codehilite",
                guess_lang=False,
            ),
        ],
    )

    return bleach.clean(
        html,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        protocols=["http", "https", "mailto"],
    )


def markdown_to_plain_text(content):
    content = re.sub(
        r"```[\s\S]*?```",
        "",
        content,
    )

    html = markdown.markdown(
        content,
        extensions=["extra"],
    )

    text = bleach.clean(
        html,
        tags=[],
        strip=True,
    )

    text = re.sub(r"\s+", " ", text)

    return text.strip()