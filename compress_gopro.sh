#!/usr/bin/env bash

set -x

OUTPUT_DIR=out
mkdir $OUTPUT_DIR

for F in *.MP4; do \
    ffmpeg \
    -i $F \
    -vcodec libx264 \
    -crf 24 \
    -an \
    $OUTPUT_DIR/$F;
done
