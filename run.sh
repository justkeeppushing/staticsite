#!/usr/bin/env bash

# .. if index.html exists
# ask to proceed
# etc


mkdir -p build/includes
cp -av includes/ build/
./src/create-site.py | tee build/index.html 
