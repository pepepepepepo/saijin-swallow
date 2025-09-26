flowchart LR
  AD[Active Directory]
  Domino[Domino サーバー]

  subgraph CoreBlock[コアブロック（社内）]
    direction TB
    DB[(NME40DB)]
    Core[MNE移行管理サーバー]
  end

  Client[クライアント]
  ExO[Exchange Online]
  Ex[Exchange]

  AD -->|TCP 389| Core
  Domino -->|TCP 1352| Core
  Client -->|TCP 139/445| Core
  Core -->|TCP 1433| DB
  Core -->|TCP 443| ExO
  Core -->|TCP 443| Ex
  Core -->|TCP 80/443| Ex

