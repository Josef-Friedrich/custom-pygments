import re
from pygments.lexers import SqlLexer
from pygments.lexer import RegexLexer, inherit, bygroups
from pygments.token import Name, Keyword, Whitespace, Punctuation, Text


class BaldrSqlLexer(SqlLexer):
    name = "SQL for Baldr project"

    aliases = ["baldr-sql"]

    flags = re.DOTALL

    # def get_tables(lexer, match):
    #     print(match)
    #     table = match.group(0).split(',')
    #     print(table)
    #     for t in table:
    #         table_match = re.match(r'\s*(\w+)(\s+AS\s+(\w+)\s*)?', t)
    #         yield 0, Name.Class, table_match.group(1)
    #         print(table_match)
    #         if table_match.group(3):
    #                 yield 323, Name.Class, table_match.group(3)

    tokens = {
        "root": [
            (r"FROM", Keyword, "table"),
            (r"[a-z_][\w]*(?=\.[a-z_][\w]*)", Name.Class),
            (r"(?<=\w\.)[a-z_][\w]*", Name.Attribute),
            (
                r"(\w+)(\s+)(AS)(\s+)(\w+)",
                bygroups(Name.Class, Whitespace, Keyword, Whitespace, Name.Class),
            ),
            # (r'(?<=FROM).*?(?=(WHERE|ORDER BY|$))', get_tables),
            inherit,
        ],
        # 'tablelist': [
        #     (r'(\w)( AS (\w))?,?', bygroups(Name.Class, Text, Name.Class))
        # ]
        "table": [
            (
                r"(\w+)(\s+)(AS)(\s+)(\w+)",
                bygroups(Name.Class, Whitespace, Keyword, Whitespace, Name.Class),
            ),
            (
                r"(\s*)(\w+)",
                bygroups(Whitespace, Name.Class),
            ),
            (r",", Punctuation, "table"),
            (r"", Text, "#pop"),
        ],
    }

    def get_tokens_unprocessed(self, text: str):
        for item in RegexLexer.get_tokens_unprocessed(self, text):
            # print(item)
            yield item
