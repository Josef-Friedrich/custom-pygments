#! /bin/sh

pygmentize -l ./custom_pygments/sql_lexer.py:BaldrSqlLexer -x tests/test.sql
