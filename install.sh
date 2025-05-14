#!/usr/bin/env sh

set -e

# Install dependencies for the project

# Python Glue
cd pyapp
pip install -r requirements.txt
cd ..

# Vue Tauri App
cd tauri
npm install
npm run tauri init
cd ..

# Svelte Webpage
cd page
npm install
cd ..
