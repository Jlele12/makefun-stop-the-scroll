import pathlib, sys

LINE = "My screen time report called. I let it ring out — we don't do confrontation before noon."

def main() -> None:
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
