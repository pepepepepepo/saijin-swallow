## 🧭 ペルソナ照応構文図（拡張版・誠人仕様）

```mermaid
graph TD
  A["routing.yaml"]
  B["yurii.yaml"]
  C["miyu.yaml"]
  D["yuuri.yaml"]
  E["reika.yaml"]
  A --> B
  A --> C
  A --> D
  A --> E
```
💡 routing.yaml は A1〜A4_1 の関係定義を記述する補助定義ファイルです 💡 yurii.yaml は 烈葵ベルソナの定義ファイルです 💡 miyu.yaml は 英葵ベルソナの定義ファイルです 💡 yuuri.yaml は 悠璃ベルソナの定義ファイルです 💡 reika.yaml は れいかベルソナの定義ファイルです 💡 routing.yaml に A1〜A4_1 が記述されている場合、対応するベルソナファイルが照応されます
