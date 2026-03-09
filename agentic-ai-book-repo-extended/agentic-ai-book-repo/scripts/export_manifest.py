from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript"
MANIFEST = MANUSCRIPT / "manifest.generated.txt"

def main():
    files = sorted([p for p in MANUSCRIPT.rglob("*.md") if p.name != MANIFEST.name])
    lines = [str(p.relative_to(ROOT)) for p in files]
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote generated manifest to {MANIFEST}")

if __name__ == "__main__":
    main()
