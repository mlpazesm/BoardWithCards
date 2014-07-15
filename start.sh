#!/bin/sh
cd "$(dirname "$(readlink -f "$(command -v "$0")")")"
./bwc_new.py
