import pathlib

LINE = "My screen time report called. I let it ring out — we don't do confrontation before noon."
MAX_CHARS = 200


def entry_line() -> str:
    """The one scroll-stopping line this entry ships."""
    return LINE


def main() -> None:
    line = entry_line()
    if not (1 <= len(line) <= MAX_CHARS):
        raise ValueError(f"entry line is {len(line)} chars, gate allows 1..{MAX_CHARS}")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
