flowchart LR
  %% ノード
  AD[Active Directory<br/>サーバー]
  Domino[Domino<br/>サーバー]

  subgraph CoreBlock[ ]
    direction TB
    DB[(NME40DB)]
    Core[MNE移行管理サーバー]
  end

  Client[クライアント]
  ExO[Exchange Online]
  Ex[Exchange]

  %% 接続（ポート表示）
  AD -->|TCP 389| Core
  Domino -->|TCP 1352| Core
  Client -->|TCP 139/445| Core
  Core -->|TCP 1433| DB

  Core -->|TCP 443| ExO
  Core -->|TCP 443| Ex
  Core -->|TCP 80/443| Ex

  %% 体裁少し寄せる
  AD --- Domino
  Client --- Core
  ExO --- Ex
