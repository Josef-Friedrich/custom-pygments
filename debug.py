import pygments
from pygments.lexers import get_all_lexers


for lexer in get_all_lexers():
    print(lexer)

from jf_pygments.lexers.sql import BaldrSqlLexer



for token in pygments.lex("SELECT * FROM Person", BaldrSqlLexer()):
    print(token)
