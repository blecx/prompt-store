from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
if len(sys.argv) < 3:
    print('Usage: python scripts/create_section.py <folder> <filename>')
    raise SystemExit(1)

folder = root / 'report' / sys.argv[1]
folder.mkdir(parents=True, exist_ok=True)
path = folder / sys.argv[2]
if path.exists():
    print(f'File already exists: {path}')
    raise SystemExit(1)

path.write_text('# <New Section Title>\n\n<Add content here>\n', encoding='utf-8')
print(f'Created {path}')
