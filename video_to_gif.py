from pathlib import Path
import fire
import logging

logging.basicConfig(level=logging.INFO)


def main(path: Path = Path.cwd(), ftype: str = "mp4") -> None:
    logging.info(f"Processing path: {path.resolve()}")

    paths = list(path.glob(f"*.{ftype}"))
    logging.info(f"Found {len(paths)}")

    for p in paths:
        logging.info(f"Processing {p}")


if __name__ == "__main__":
    fire.Fire(main)
