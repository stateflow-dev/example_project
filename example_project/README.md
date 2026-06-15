# Example Project

Project contoh untuk demo encoding-doctor.

## File yang sengaja punya encoding issues:
- src/config.py      → mojibake (latin-1)
- src/database.py    → BOM prefix
- src/utils.py       → CRLF line endings
- data/users.csv     → null bytes
- config/settings.ini → BOM + CRLF

## File yang bersih:
- src/main.py        → clean UTF-8
