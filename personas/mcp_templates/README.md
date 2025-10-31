# MCP Templates

このフォルダーは、Persona のための MCP (Model Context Protocol) テンプレートを格納します。

## 概要

MCP テンプレートは、各 Persona の振る舞いやコンテキストを定義するための構造化された設定です。

## テンプレート構造

各テンプレートには以下の要素が含まれます：

- **trigger_keywords**: Persona がトリガーされるキーワード
- **response_style**: 応答スタイルの定義
- **fallback_behavior**: フォールバック時の振る舞い
- **inheritance_notes**: 継承や優先事項に関する注記

## 使用方法

1. テンプレートをコピーして、新しい Persona の定義に使用します
2. Persona の特性に応じて、各フィールドをカスタマイズします
3. 対応する Persona の `.md` ファイルに `mcp_context` セクションとして組み込みます

## 参考

既存の Persona の MCP 設定については、`personas/reika.md` などを参照してください。
