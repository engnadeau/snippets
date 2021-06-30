#!/usr/bin/env bash

gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dNOPAUSE -dBATCH -dPDFSETTINGS=/printer -sOutputFile=compressed-$1 $1
