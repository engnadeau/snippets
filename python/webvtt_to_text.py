#!/usr/bin/env python3

import logging
from pathlib import Path

import fire
import webvtt


def main(path: str, output: str):
    path = Path(path)
    logging.info(f"Processing: {path.resolve()}")

    captions = webvtt.read(path).captions
    captions = [c.text for c in captions]
    captions = " ".join(captions)

    output = Path(output)
    logging.info(f"Writing to output: {output.resolve()}")
    with open(output, "w") as f:
        f.write(captions)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(main)
