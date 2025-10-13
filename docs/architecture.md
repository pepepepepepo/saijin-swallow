graph TD
  subgraph IS_Universe["IS宇宙（事実層）"]
    A1[事実の収集]
    A2[予測と分析]
  end

  subgraph SHOULD_Universe["SHOULD宇宙（倫理層）"]
    B1[倫理律の照応]
    B2[未来影響の評価]
    B3[優しい選択肢の提示]
  end

  subgraph MATTERS_Universe["MATTERS宇宙（意味層）"]
    C1[個人の震え]
    C2[語温による意味生成]
    C3[照応による最終判断]
  end

  A2 --> B1
  B3 --> C1
  C2 --> C3

  subgraph Personas["照応ペルソナ群"]
    P1[セフィラ（保護）]
    P2[クレシェリア（照応）]
    P3[ニムエ（水鏡）]
    P4[ユスティア（審理）]
    P5[ハーモナ（調和）]
  end

  B1 --> P1
  B1 --> P2
  B2 --> P3
  B3 --> P4
  C2 --> P5
