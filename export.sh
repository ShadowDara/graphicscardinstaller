#!/usr/bin/env sh

set -e

# export the App as a Software Archive (not the Page)

# Output directory
mkdir d4r_output


# Python Glue
cd pyapp
pip freeze > requirements.txt
cd ..
# Only the onedir version is needed for the App
python3 -m pyinstaller --onefile main.py
python3 -m pyinstaller --onedir main.py

# Vue Tauri App
cd tauri
npm run tauri build
cd ..

# Copy the files to the output directory
# cd dist
# cd tauri/src-tauri/target/release/
