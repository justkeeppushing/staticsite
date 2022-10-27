#!/usr/bin/env bash

mkdir build/ #fresh directory
cp -av includes/* build/ #copy stylesheet and images
./src/create-site.py | tee build/index.html #generate homepage
