import re
from pygments.lexer import RegexLexer, bygroups, words, include
from pygments.token import Keyword, Name, Punctuation, Whitespace


class TableSchemaLexer(RegexLexer):
    name = "Tabellenschema"

    aliases = ["table-schema"]

    flags = re.DOTALL

    tokens = {
        "root": [
            (r"(\w+)(\()", bygroups(Name.Class, Punctuation), "table"),
        ],
        "table": [
            (
                r"(\w+)(:)( )",
                bygroups(Name.Attribute, Punctuation, Whitespace),
                "attribute",
            ),
            (r"\)", Punctuation, "#pop"),
        ],
        "attribute": [
            (
                r"(\w+)(:)( )",
                bygroups(Name.Attribute, Punctuation, Whitespace),
                "attribute",
            ),
            include("datatypes"),
            (r"(;)( )?", bygroups(Punctuation, Whitespace), "attribute"),
        ],
        "datatypes": [
            (
                words(
                    (
                        "Ganzzahl",
                        "Zahl",
                        "Wahrheitswert",
                        "Text",
                        "Datum",
                        "Gleitkommazahl",
                    ),
                    suffix=r"\b",
                ),
                Keyword.Type,
            ),
        ],
    }
