#!/bin/bash
# download_model.sh
# Saijin-OS: swallow モデル取得スクリプト

TARGET_DIR="${1:-../models/swallow}"
mkdir -p "$TARGET_DIR"

echo ">>> モデル保存先: $TARGET_DIR"

# 例: 認証付きダウンロード
# curl -L -H "Authorization: Bearer $MODEL_TOKEN" \
#   "https://storage.example.com/swallow-9b.safetensors" \
#   -o "$TARGET_DIR/swallow-9b.safetensors"

echo "（注）ここに実際のダウンロードURLを入れてください。"
