from pygments.style import Style
from pygments.token import (
    Keyword,
    Name,
    Comment,
    String,
    Error,
    Number,
    Operator,
    Generic,
    Whitespace,
    Literal,
    Punctuation,
)


class WhiteStyle(Style):
    """All fonts are changed to white."""

    background_color = "#ffffff"

    styles = {
        Comment: "#ffffff",
        Keyword: "#ffffff",
        Operator: "#ffffff",
        Name: "#ffffff",
        String: "#ffffff",
        Generic: "#ffffff",
        Error: "#ffffff",
        Literal: "#ffffff",
        String: "#ffffff",
        Number: "#ffffff",
        Whitespace: "#ffffff",
        Punctuation: "#ffffff",
    }
