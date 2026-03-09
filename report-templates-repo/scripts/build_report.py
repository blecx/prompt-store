from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = root / 'report' / 'manifest.txt'
outdir = root / 'dist'
outdir.mkdir(exist_ok=True)
outfile = outdir / 'report-manuscript.md'

parts = []
for line in manifest.read_text(encoding='utf-8').splitlines():
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    path = root / 'report' / line
    if path.exists():
        parts.append(path.read_text(encoding='utf-8').rstrip())
    else:
        parts.append(f"# MISSING FILE\n\nExpected: `{line}`")

outfile.write_text('\n\n---\n\n'.join(parts) + '\n', encoding='utf-8')
print(f'Wrote {outfile}')
