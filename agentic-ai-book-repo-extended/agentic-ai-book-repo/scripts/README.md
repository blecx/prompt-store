# Scripts

## Available utilities

- `build_book.py` — combines files from `manuscript/manifest.txt` into `dist/book-manuscript.md`
- `check_placeholders.py` — finds unresolved placeholders such as `{{BOOK_TITLE}}`
- `create_chapter.py` — creates a new chapter file in a selected manuscript folder
- `export_manifest.py` — exports the current manuscript manifest

## Typical usage

```bash
python scripts/build_book.py
python scripts/check_placeholders.py
```
