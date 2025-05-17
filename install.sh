#!/usr/bin/env sh

set -e

# Install dependencies for the project

# Python Glue
python3 -m venv .venv
cd pyapp
pip install -r requirements.txt
cd ..

# Vue Tauri App
cd tauri
npm install
cd ..

# Svelte Webpage
cd page
npm install
cd ..
