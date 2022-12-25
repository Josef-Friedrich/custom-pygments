#! /bin/sh

pygmentize -l ./jf_pygments/sql_lexer.py:BaldrSqlLexer -x tests/test.sql
