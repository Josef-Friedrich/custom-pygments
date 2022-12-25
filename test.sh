#! /bin/sh

pygmentize -l baldr-sql  tests/test.sql

pygmentize -l table-schema tests/test.table-schema
