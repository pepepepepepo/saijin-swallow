（↑ここに上のREADME全文が入ってるので、そのままコピペしてEnter）

## Quickstart (最短)

```bash
# 依存関係
pip install -r requirements.txt

# （任意）モデルDLスクリプト
bash scripts/download_model.sh    # 実URLを入れて使う場合のみ

# まずは小モデルで動作確認
python scripts/run_inference.py

