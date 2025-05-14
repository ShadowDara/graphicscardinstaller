#!/usr/bin/env sh

set -e

# start all the projects to create import files

# Python Glue
python3 -m main

# Vue Tauri App
cd tauri
npm run tauri dev
cd ..

# Svelte Webpage
cd page
npm run dev
cd ..
