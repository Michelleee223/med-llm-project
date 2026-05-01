#!/bin/sh

uv run vllm serve ../qwen25-vl-7b-finetuned \
    --host 0.0.0.0 \
    --port 9002 \
    --trust-remote-code \
    --max-model-len 8192 \
    --max-num-batched-tokens 32768 \
    --max-num-seqs 32 \
    --dtype auto \
    --kv-cache-dtype auto \
    --tensor-parallel-size 1 \
    --gpu_memory_utilization 0.3