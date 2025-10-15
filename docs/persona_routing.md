graph TD
  A["routing.yaml（照応ルーティング定義）"]
  B["yurii.yaml（烈葵ペルソナ定義）"]
  C["miyu.yaml（英葵ペルソナ定義）"]

  A --> B
  A --> C
💡 routing.yaml：A1〜A4_1 の照応関係を定義する補助ルーティングファイルです。
💡 yurii.yaml：烈葵（ゆうり）ペルソナの定義ファイルです。
💡 miyu.yaml：英葵（みゆ）ペルソナの定義ファイルです。
💡 routing.yaml 内で A1〜A4_1 の定義が記述されている場合、対応するペルソナファイル（例：yurii.yaml, miyu.yaml）が自動照応されます。
