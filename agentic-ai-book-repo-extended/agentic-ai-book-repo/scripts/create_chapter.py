from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "chapter-template.md"

def slugify(text: str) -> str:
    text = text.lower().strip()
    allowed = []
    for ch in text:
        if ch.isalnum():
            allowed.append(ch)
        elif ch in {" ", "-", "_"}:
            allowed.append("-")
    slug = "".join(allowed)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part-dir", required=True, help="Example: manuscript/02-part-ii-system-design")
    parser.add_argument("--number", required=True, help="Example: 16")
    parser.add_argument("--title", required=True, help="Example: Agent Interfaces")
    args = parser.parse_args()

    part_dir = ROOT / args.part_dir
    part_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{args.number.zfill(2)}-{slugify(args.title)}.md"
    out = part_dir / filename

    content = TEMPLATE.read_text(encoding="utf-8")
    content = content.replace("{{CHAPTER_NUMBER}}", args.number)
    content = content.replace("{{CHAPTER_TITLE}}", args.title)

    out.write_text(content, encoding="utf-8")
    print(f"Created {out}")

if __name__ == "__main__":
    main()
