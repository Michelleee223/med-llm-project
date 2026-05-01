#!/bin/sh

curl http://127.0.0.1:8001/v1/models

curl http://127.0.0.1:8001/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mylora",
    "messages": [{"role": "user", "content": "你好,我肚子疼"}],
    "max_tokens": 256
  }'
