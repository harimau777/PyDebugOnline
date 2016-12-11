#!/bin/bash

echo "Should trace code supplied as a string"
python traceCode.py -s "i = 10\nj = 20\nk = i + j\nprint k"

echo "Should trace code supplied as a file"
python traceCode.py -f testFile.py

echo "Should trace exception"
python traceCode.py -s "i = 10\nj = 20\nk = i + j\nprint k\nfoo"
