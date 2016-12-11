#!/bin/bash

echo "Should display help"
python traceCode -h

echo "Should trace code supplied as a string"
$code="i = 10\nj = 20\nk = i + j\nprint k"
python traceCode -s $code

echo "Should trace code supplied as a file"
$file="testFile.py"
python traceCode -f $file