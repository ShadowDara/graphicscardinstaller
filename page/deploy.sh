#!/usr/bin/env sh

set -e

# Deploy the Svelte Webpage to Github Pages

npm run build

npm run deploy
