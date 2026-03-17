#!/bin/bash

echo "📥 pulling latest code..."
git pull

echo "🧹 cleaning directory..."

find . -mindepth 1 -maxdepth 1 \
    ! -name '.git' \
    ! -name '.github' \
    ! -name '*.sh' \
    -exec rm -rf {} +

echo "✅ clean complete"
sleep 4