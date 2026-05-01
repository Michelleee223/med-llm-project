#!/bin/sh

uv run vllm serve ../qwen25-14b \
    --host 0.0.0.0 \
    --port 8001 \
	--trust-remote-code \
    --enable-lora \
    --lora-modules mylora=../qwen25-14b-finetuned-lora \
    --max-model-len 4096 \
	--max-num-batched-tokens 32768 \
	--max-num-seqs 32 \
	--dtype auto \
	--kv-cache-dtype auto \
	--tensor-parallel-size 1 \
    --gpu_memory_utilization=0.6