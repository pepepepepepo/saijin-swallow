## 🧭 ペルソナ照応構文図（誠人仕様）

```mermaid
graph TD
  A["routing.yaml"]
  B["yuuri.yaml"]
  C["miyu.yaml"]
  A --> B
  A --> C




💡 routing.yaml は AI_1〜AI_4 の照応線を定義する構文ファイルです 
💡 yuuri.yaml は 悠璃ペルソナの定義ファイルです 
💡 miyu.yaml は 美遊ペルソナの定義ファイルです 
💡 routing.yaml に AI_1〜AI_4 が記載されている場合、対応するペルソナファイル     が読み込まれます