## 🧠 サーバー構成図（Swallow-9B）

以下は、vLLMを用いたSwallow-9Bモデルの起動構成と、personaとの紐付けを示す図です。

![vLLM構成図](https://copilot.microsoft.com/th/id/BCO.ab522caf-d3ee-4805-97ac-54edf91bebc9.png)

### 🔧 構成要素

- **ユーザー**：外部クライアントや誠人自身
- **OpenAI API Server (vLLM)**：モデルを灯すエンジン
- **routing.yaml**：personaとモデルの紐付け設定
- **Swallow-9Bモデルフォルダ**：`config.json` と `safetensors` を格納

### 📦 モデルパス例

```bash
python3 -m vllm.entrypoints.openai.api_server \
  --model /mnt/f/saijjin/models/swallow \
  --gpu-memory-utilization 0.60 \
  --max-model-len 2048
