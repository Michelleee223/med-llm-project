#!/bin/sh

# vllm 对 VL 模型不支持单独载入 LoRA

unset OMP_NUM_THREADS

vllm serve ../qwen25-vl-7b-finetuned \
    --host 0.0.0.0 \
    --port 8000 \
    --max-model-len=8k \
    --gpu_memory_utilization=0.90
