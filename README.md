# example_project

Demo project showing encoding issues that enc-doctor can fix.

Files with issues:
- src/engine.py    — mojibake (corrupt box drawing characters)
- config/settings.ini — BOM + CRLF line endings
- data/users.csv   — null bytes
- src/utils.py     — CRLF line endings
