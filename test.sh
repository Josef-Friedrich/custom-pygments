#! /bin/sh

pygmentize -l ./jf_pygments/lexers/sql.py:BaldrSqlLexer -x tests/test.sql

pygmentize -l baldrsql tests/test.sql
