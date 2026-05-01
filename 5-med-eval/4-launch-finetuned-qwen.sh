#!/bin/sh

vllm serve ../qwen25-14b \
  --host 0.0.0.0 \
  --port 8000 \
  --trust-remote-code \
  --max-model-len 4096 \
  --max-num-batched-tokens 32768 \
  --max-num-seqs 32 \
  --dtype auto \
  --kv-cache-dtype auto \
  --tensor-parallel-size 1 \
  --enable-lora \
  --lora-modules my-lora=../qwen25-14b-finetuned-lora \
  --gpu-memory-utilization 0.90
