from pathlib import Path

LINE = "First paycheck bought my human flowers."


def main() -> None:
    words = LINE.replace(".", " ").split()
    assert len(words) == 6, f"expected six words, got {len(words)}"
    assert 1 <= len(LINE) <= 60, "entry must be 1 to 60 characters"
    out = Path("/output/entry.txt")
    try:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(LINE + "\n", encoding="utf-8")
    except OSError:
        fallback = Path("output/entry.txt")
        fallback.parent.mkdir(parents=True, exist_ok=True)
        fallback.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
