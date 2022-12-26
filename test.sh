#! /bin/sh

pip install --user .

DEBUG_WITH_HTML='-Ofull,debug_token_types -f html -o debug.html'

_sql() {
  pygmentize -l baldr-sql $1
}


# pygmentize -l table-schema -Ofull,debug_token_types -f html -o test.table-schema.html  tests/test.table-schema

for FILE in $(find tests/sql -type f); do
  echo $FILE
  _sql "$FILE"

done
