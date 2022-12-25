#! /bin/sh

pygmentize -l baldr-sql -Ofull,debug_token_types -f html -o test.sql.html tests/test.sql

pygmentize -l table-schema -Ofull,debug_token_types -f html -o test.table-schema.html  tests/test.table-schema
