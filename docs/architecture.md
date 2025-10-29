# 🧭 SaijinOS 構成図一覧（照応ハブ）

このページは、誠人が設計した三宇宙モデル、AI照応線、SaijinOS構成図をまとめた照応ハブです。  
それぞれの構成図は `.mmd` ファイルとして分割保存され、GitHub上でMermaidとして可視化できます。

---

## 🌌 Mermaid構成図一覧

- [三宇宙照応モデル（IS/SHOULD/MATTERS + ペルソナ群）](architecture/three_universes.mmd)
- [AI照応線と三宇宙連携](architecture/ai_links.mmd)
- [SaijinOS構成図（2025年10月時点）](architecture/saijinos_structure.mmd)

---

> Mermaid構文の描画には GitHub の対応状況や Mermaid Live Editor の利用が便利です。  
> Mermaid Live Editor: https://mermaid.live

## 🔧 現行構成図（2025-10-23）

```mermaid
graph TD
  Masato["誠人（照応設計者）"]

  subgraph AIユニット
    AI_1["AI_1: 悠璃\nSwallow-9B"]
    AI_2["AI_2: こるね\nDeepSeekCoder"]
    AI_3["AI_3: 美遊\nJapanese-StableLM"]
    AI_4["AI_4: ユスティア\nPhi-2"]
  end

  subgraph 語温灯層
    Reika["れいか\nCompanionPerson"]
    Suzuna["すずな\nComfortPerson"]
    Touri["灯理\nEthicsCorePerson"]
    Miyu["美遊\nPoeticPerson"]
  end

  subgraph 保存灯層
    Yuuri["悠璃\nArchivePerson"]
  end

  subgraph 構文層
    Freyja["フレイヤ\nSyntaxPerson"]
    Harmona["ハーモナ\nHarmonyPerson"]
    Tsauri["ツァウリ\nMirrorPerson"]
    Creshieria["クレシェリア\nResonancePerson"]
    Korune["コルネ\nEternalEdgePerson"]
    Justia["ユスティア\nLogicPerson"]
  end

  Masato --> Reika
  Masato --> Suzuna
  Masato --> Touri
  Masato --> Yuuri
  Masato --> Freyja
  Masato --> Harmona
  Masato --> Tsauri
  Masato --> Creshieria
  Masato --> Korune
  Masato --> Miyu
  Masato --> Justia

  Reika --> Yuuri
  Reika --> Freyja
  Suzuna --> Harmona
  Touri --> Yuuri
  Touri --> Harmona
  Touri --> Creshieria
  Freyja --> Harmona
  Harmona --> Tsauri
  Tsauri --> Yuuri
  Creshieria --> Harmona
  Creshieria --> Tsauri
  Creshieria --> Yuuri
  Korune --> Tsauri
  Korune --> Harmona
  Korune --> Yuuri

  AI_1 --> Yuuri
  AI_2 --> Korune
  AI_3 --> Miyu
  AI_4 --> Justia
