#!/bin/bash
# Build MkDocs site by staging content into _docs/ directory.
# MkDocs requires docs_dir to be a child of the config directory.
#
# Usage: bash scripts/build-docs.sh
# Output: _site/ (MkDocs output)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DOCS_DIR="$REPO_ROOT/_docs"
SITE_DIR="$REPO_ROOT/_site"

echo "Staging content to $DOCS_DIR..."

# Clean previous build
rm -rf "$DOCS_DIR" "$SITE_DIR"
mkdir -p "$DOCS_DIR"

# Copy content directories
for dir in knowledge-base coding-practice system-design interview-tracking career-frameworks project-case-study prompt-templates; do
  if [ -d "$REPO_ROOT/$dir" ]; then
    cp -r "$REPO_ROOT/$dir" "$DOCS_DIR/$dir"
  fi
done

# Copy root markdown files
cp "$REPO_ROOT/README.md" "$DOCS_DIR/index.md"
cp "$REPO_ROOT/CONTRIBUTING.md" "$DOCS_DIR/CONTRIBUTING.md"

# Copy docs assets (custom JS/CSS for MkDocs)
if [ -d "$REPO_ROOT/docs-assets" ]; then
  cp -r "$REPO_ROOT/docs-assets" "$DOCS_DIR/docs-assets"
fi

cd "$REPO_ROOT"

if [ "${1:-}" = "serve" ]; then
  echo "Starting MkDocs dev server (hot reload)..."
  echo "Open http://localhost:8000 in your browser"
  echo "Press Ctrl+C to stop"
  .venv/bin/mkdocs serve --dev-addr 127.0.0.1:8000
  # Clean staging dir on exit
  rm -rf "$DOCS_DIR"
else
  echo "Building MkDocs..."
  .venv/bin/mkdocs build
  echo "Build complete: $SITE_DIR"
  # Clean staging dir
  rm -rf "$DOCS_DIR"
  echo "Cleaned staging directory."
fi
