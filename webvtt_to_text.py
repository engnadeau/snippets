#!/usr/bin/env python3

import logging
from pathlib import Path
from typing import Optional

import fire
import pyperclip
import webvtt


def main(path: str, output: Optional[str] = None, copy: bool = False):
    path = Path(path)
    logging.info(f"Processing: {path.resolve()}")

    captions = webvtt.read(path).captions
    captions = [c.text for c in captions]
    captions = " ".join(captions)

    if output:
        output = Path(output)
        logging.info(f"Writing to output: {output.resolve()}")
        with open(output, "w") as f:
            f.write(captions)

    if copy:
        logging.info("Captions copied to clipboard")
        pyperclip.copy(captions)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(main)
