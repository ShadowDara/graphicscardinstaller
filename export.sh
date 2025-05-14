#!/usr/bin/env sh

set -e

# export the App as a Software Archive (not the Page)


# Some files are only generated in the dev environment which
# are needed for the build
dev_start.sh


# Output directory
mkdir d4r_output


# Python Glue
# Only the onedir version is needed for the App
python3 -m pyinstaller --onefile main.py
python3 -m pyinstaller --onedir main.py

# Vue Tauri App
cd tauri
npm run tauri build
cd ..

# Copy the files to the output directory
