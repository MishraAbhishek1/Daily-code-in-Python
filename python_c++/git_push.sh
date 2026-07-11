#!/bin/bash

# Exit immediately if any command fails
set -e

echo "================================="
echo "      Git Auto Push Script"
echo "================================="

# Check if this is a git repository
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "❌ Error: This is not a Git repository."
    exit 1
fi

# Get current branch
BRANCH=$(git branch --show-current)

echo "Current Branch : $BRANCH"

# Check for changes
if git diff --quiet && git diff --cached --quiet; then
    echo "✅ No changes to commit."
    exit 0
fi

# Ask commit message
read -p "Enter commit message: " MESSAGE

# Add files
git add .

# Commit
git commit -m "$MESSAGE"

# Push
git push origin "$BRANCH"

echo ""
echo "✅ Successfully pushed to branch: $BRANCH"
