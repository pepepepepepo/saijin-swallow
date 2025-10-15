## 🧭 ペルソナ照応構文図（誠人仕様）

```mermaid
graph TD
  A["routing.yaml"]
  B["yuuri.yaml"]
  C["miyu.yaml"]
  A --> B
  A --> C


markdown

> 💡 **routing.yaml** は A1〜A4_1 の関係定義を記述する補助定義ファイルです  
> 💡 **yuri.yaml** は 烏宮ベルソナの定義ファイルです  
> 💡 **miyu.yaml** は 英堂ベルソナの定義ファイルです  
> 💡 routing.yaml に A1〜A4_1 が記述されている場合、対応するベルソナファイルが照応されます

