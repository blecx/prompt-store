from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
pattern = re.compile(r"\{\{[A-Z0-9_]+\}\}")

def scan():
    findings = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in {".git", "__pycache__", "dist"} for part in path.parts):
            continue
        if path.suffix.lower() not in {".md", ".txt", ".py", ".bib", ".yml"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        matches = sorted(set(pattern.findall(text)))
        if matches:
            findings.append((path, matches))
    return findings

def main():
    findings = scan()
    if not findings:
        print("No placeholders found.")
        return
    print("Unresolved placeholders detected:\n")
    for path, matches in findings:
        rel = path.relative_to(ROOT)
        print(f"{rel}:")
        for m in matches:
            print(f"  - {m}")
        print()
    sys.exit(1)

if __name__ == "__main__":
    main()
