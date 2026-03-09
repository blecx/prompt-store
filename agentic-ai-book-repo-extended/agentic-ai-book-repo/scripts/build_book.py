from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manuscript" / "manifest.txt"
DIST = ROOT / "dist"
OUTPUT = DIST / "book-manuscript.md"

def load_manifest():
    items = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        items.append(ROOT / line)
    return items

def main():
    DIST.mkdir(parents=True, exist_ok=True)
    parts = []
    for path in load_manifest():
        if not path.exists():
            raise FileNotFoundError(f"Missing manuscript file: {path}")
        parts.append(f"<!-- BEGIN: {path.relative_to(ROOT)} -->\n")
        parts.append(path.read_text(encoding="utf-8").rstrip() + "\n")
        parts.append(f"\n<!-- END: {path.relative_to(ROOT)} -->\n\n")
    OUTPUT.write_text("".join(parts), encoding="utf-8")
    print(f"Wrote combined manuscript to {OUTPUT}")

if __name__ == "__main__":
    main()
