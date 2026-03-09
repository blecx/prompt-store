from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
pattern = re.compile(r'<[^>]+>')
count = 0
for path in sorted(root.rglob('*.md')):
    if '.git' in path.parts or 'dist' in path.parts:
        continue
    text = path.read_text(encoding='utf-8', errors='ignore')
    matches = pattern.findall(text)
    if matches:
        count += len(matches)
        print(f'\n{path.relative_to(root)}')
        for m in matches[:20]:
            print('  ', m)
print(f'\nTotal placeholders found: {count}')
