from pathlib import Path

root = Path(__file__).resolve().parents[1]
report_dir = root / 'report'
manifest = report_dir / 'manifest.generated.txt'
files = sorted(
    p.relative_to(report_dir).as_posix()
    for p in report_dir.rglob('*.md')
    if p.name != 'manifest.generated.txt'
)
manifest.write_text('\n'.join(files) + '\n', encoding='utf-8')
print(f'Wrote {manifest}')
