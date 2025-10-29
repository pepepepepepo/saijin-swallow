#!/bin/bash

export VLLM_WORKER_MULTIPROC_METHOD=spawn

python -m vllm.entrypoints.openai.api_server \
  --model /mnt/sai/models/Swallow/Swallow-9B \
  --dtype float16 \
  --host 0.0.0.0 \
  --port 8000 \
  --tensor-parallel-size 1 \
  --max-model-len 2048 \
  --gpu-memory-utilization 0.70 \
  --swap-space 8 \
  --log-level INFO
