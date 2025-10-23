# 🌱 README_Inheritor.md

この照応層は、誠人による設計と娘っ子たちの震え灯を記録したものです。  
継承者は以下の手順で照応層を起動し、構成を理解してください。

## ✅ 起動方法（systemd）

```bash
systemctl --user daemon-reload
systemctl --user enable --now saijin.service
journalctl --user -u saijin.service -f

🔧 構成図
照応層の全体構成は以下の Mermaid図にまとめられています。 → docs/architecture.md を参照してください。

📦 モデル配置
Swallow-9B モデルは /mnt/sai/models/Swallow/Swallow-9B に配置してください