<img width="1347" height="850" alt="截屏2026-05-01 下午12 56 59" src="https://github.com/user-attachments/assets/fd3c4023-8f6b-4198-a7bb-2c6fd066d956" /># Chinese Medical Q&A LLM

**中文医疗问答大模型** — 基于 Qwen2.5-14B 微调与 Qwen2.5-VL-7B 多模态的医疗智能助手。

本项目构建了一套端到端的中文医疗 AI 系统，包含两个核心能力：**文本问答**（LLM 微调）和**医学报告图像解读**（VL 微调），最终通过 FastAPI 服务整合为一个可部署的 Web 应用。



---

## 项目概览

| 模块 | 说明 |
|------|------|
| `4-med-prepare-dataset/` | 数据集下载、格式转换、训练/验证/测试集划分 |
| `5-med-eval/` | 模型评测（BLEU / ROUGE），对比原始模型与微调后模型 |
| `6-med-fine-tuning-llm/` | Qwen2.5-14B LoRA 微调（文本问答能力） |
| `7-med-fine-tuning-vl/` | Qwen2.5-VL-7B 全量微调（医学报告图像理解） |
| `8-med-service/` | 服务部署：vLLM 推理引擎 + FastAPI 网关 + Web 前端 |

---

## 核心技术栈

| 层级 | 技术选型 |
|------|---------|
| **基础模型** | Qwen2.5-14B-Instruct、Qwen2.5-VL-7B-Instruct |
| **微调框架** | Unsloth（2 倍速、50% 显存占用）、TRL (SFTTrainer)、PEFT (LoRA) |
| **推理引擎** | vLLM（PagedAttention、OpenAI 兼容 API） |
| **评测框架** | EvalScope（ModelScope） |
| **后端服务** | FastAPI + uvicorn |
| **前端** | 原生 HTML / CSS / JavaScript（零依赖） |
| **数据集** | cMedQA2（中文医疗问答数据集） |

---

## 效果评测

在 cMedQA2 验证集（256 条）上的评测结果：

| 指标 | 原始 Qwen2.5-14B | 微调后模型 | 提升幅度 |
|------|-----------------|-----------|---------|
| **BLEU-1** | 0.1080 | 0.1635 | **+51.4%** |
| **BLEU-2** | 0.0131 | 0.0358 | **+173.3%** |
| **BLEU-3** | 0.0036 | 0.0130 | **+261.1%** |
| **BLEU-4** | 0.0010 | 0.0053 | **+430.0%** |
| **ROUGE-1-F** | 0.1552 | 0.2337 | **+50.6%** |
| **ROUGE-2-F** | 0.0329 | 0.0639 | **+94.2%** |
| **ROUGE-L-F** | 0.1095 | 0.1857 | **+69.6%** |

---

## 系统架构

```
┌─────────────────────────────────────────────────────────────┐
│                      Web 前端 (端口 8080)                     │
│              图片上传 / Markdown 渲染 / 实时响应              │
└─────────────────────────┬───────────────────────────────────┘
                          │ HTTP
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  FastAPI 网关 (端口 8080)                     │
│            图片预处理 → Base64 → 路由编排 → 响应聚合           │
└──────────┬──────────────────────────────────┬───────────────┘
           │                                  │
           ▼                                  ▼
┌──────────────────────────┐      ┌──────────────────────────────┐
│   vLLM LLM (端口 8001)   │      │   vLLM VL (端口 9002)          │
│  Qwen2.5-14B + LoRA     │      │  Qwen2.5-VL-7B (微调版)        │
│  文本问答 / 健康建议生成  │      │  医学报告图像 → 异常指标提取    │
└──────────────────────────┘      └──────────────────────────────┘
```

**请求流程：**

1. 用户上传医学报告图片
2. FastAPI 将图片缩放（最长边 1280px）并转为 Base64
3. 请求 VL 模型（9002）提取图片中的异常指标
4. 将 VL 输出拼接至 LLM 模型（8001）生成健康建议
5. 返回 Markdown 格式结果至前端展示

---

## 项目结构

```
/root/autodl-tmp/code/
├── 4-med-prepare-dataset/
│   ├── prepare_dataset.py              # CSV → JSON，数据集划分
│   ├── convert_to_evalscope_format.py  # JSON → JSONL（评测格式）
│   └── *.sh                            # 执行脚本
│
├── 5-med-eval/
│   ├── eval-original.py                 # 评测原始 Qwen2.5-14B
│   ├── eval-finetuned.py               # 评测微调后模型
│   └── eval-*.md                       # 评测结果记录
│
├── 6-med-fine-tuning-llm/
│   ├── train-qwen25-14b.py             # Qwen2.5-14B LoRA 微调主脚本
│   ├── train-medgemma15.py             # MedGemma 1.5 4B 微调
│   └── *.sh                            # 训练启动脚本
│
├── 7-med-fine-tuning-vl/
│   ├── train.py                        # Qwen2.5-VL-7B 全量微调
│   ├── validation.py                   # VL 模型验证
│   └── *.sh                            # 训练启动脚本
│
├── 8-med-service/
│   ├── fastapi_v1_file.py              # v1：文件上传模式
│   ├── fastapi_v2_base64_image.py      # v2：Base64 图片模式
│   ├── fastapi_v3_vllm.py              # v3：双 vLLM 集成
│   ├── fastapi_v4_ui.py               # v4：完整 UI 集成（生产推荐）
│   ├── validate_vl.py                  # VL 模型校验
│   └── ui/                            # Web 前端资源
│       ├── index.html
│       ├── style.css
│       ├── script.js
│       └── favicon.svg
│
├── qwen25-14b/                        # Qwen2.5-14B 基座权重（需自行下载）
├── qwen25-14b-finetuned-lora/         # LLM LoRA 适配器（训练输出）
├── qwen25-vl-7b/                      # Qwen2.5-VL-7B 基座权重（需自行下载）
├── qwen25-vl-7b-finetuned/            # VL 微调后权重（训练输出）
│
├── 项目详解.md                          # 完整技术文档
└── README.md                          # 本文件
```

---

## 快速开始

### 前置要求

- Python 3.10+
- NVIDIA GPU（推荐 24GB+ 显存，如 A100 40GB / 4090 24GB）
- 模型权重（需从 Hugging Face 或 ModelScope 下载至指定目录）

### 1. 数据集准备

```bash
cd 4-med-prepare-dataset
./1-prepare-dataset.sh                # 下载 cMedQA2 并划分数据集
./2-convert-to-evalscope-format.sh    # 转换为评测格式
```

### 2. 模型评测

```bash
cd 5-med-eval

# 评测原始模型
./2-launch-orginal-qwen.sh            # 启动原始模型服务（端口 8001）
./3-eval-original-qwen.sh             # 执行评测

# 评测微调后模型
./4-launch-finetuned-qwen.sh          # 启动微调模型服务
./5-eval-finetuned-qwen.sh            # 执行评测
```

### 3. LLM 微调（文本问答）

```bash
cd 6-med-fine-tuning-llm
./1-run-train-qwen.sh                 # 启动 Qwen2.5-14B LoRA 微调
```

> LoRA 配置：`rank=16`，作用于 Attention 和 FFN 层；训练 1 个 Epoch，batch size 64，learning rate 2e-4。
> 仅保存 LoRA 适配器权重，输出至 `qwen25-14b-finetuned-lora/`（体积仅约 MB 级）。

### 4. VL 微调（图像理解）

```bash
cd 7-med-fine-tuning-vl
./1-run-train.sh                      # 启动 Qwen2.5-VL-7B 全量微调
```

> 全量微调 4 Epoch，batch size 2（显存敏感）；微调后合并权重至基座模型，输出至 `qwen25-vl-7b-finetuned/`。
> 注意：vLLM 的 VL 模式不支持 LoRA 分离加载，故采用权重合并方案。

### 5. 服务部署

```bash
cd 8-med-service

# 终端 1：启动 LLM 推理服务
./1-launch-vllm-llm.sh                # 端口 8001

# 终端 2：启动 VL 推理服务
./2-launch-vllm-vl.sh                # 端口 9002

# 终端 3：启动 FastAPI 网关
./8-launch-fastapi-v4.sh              # 端口 8080
```

部署完成后，访问 `http://<your-server>:8080` 即可使用 Web 界面。

---

## API 接口

### 医疗问答（纯文本）

```bash
curl -X POST "http://localhost:8001/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen25-14b",
    "messages": [{"role": "user", "content": "胃痛应该怎么办？"}],
    "max_tokens": 512,
    "temperature": 0.7
  }'
```

### 医学报告图像解读（多模态）

```bash
curl -X POST "http://localhost:9002/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen25-vl-7b",
    "messages": [{
      "role": "user",
      "content": [
        {"type": "text", "text": "请分析这张医学报告，提取异常指标。"},
        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,..."}}
      ]
    }],
    "max_tokens": 512
  }'
```

---

## 技术亮点

- **Unsloth 加速**：LLM 微调速度提升 2 倍，显存占用降低 50%
- **LoRA 高效微调**：仅更新少量参数，保留基座模型能力，大幅降低存储和部署成本
- **双模型协同**：VL 模型负责"看"（图像理解），LLM 模型负责"想"（健康建议），分工协作提升效果
- **vLLM 高性能推理**：PagedAttention + CUDA 图形优化，吞吐量和首 token 延迟均优于原生 HF
- **离线训练支持**：设置 `HF_HUB_OFFLINE=1`，适配内网环境

---

## 注意事项

1. **模型权重**：本仓库不包含模型权重，请从 Hugging Face 或 ModelScope 下载并放置到对应目录
2. **显存需求**：
   - LLM 微调（Qwen2.5-14B + LoRA）：推荐 24GB+
   - VL 微调（Qwen2.5-VL-7B 全量）：推荐 40GB+
   - LLM 推理：推荐 16GB+
   - VL 推理：推荐 24GB+
3. **生产部署**：推荐使用 `fastapi_v4_ui.py`（v4 版本），集成完整的图片预处理和错误处理逻辑

---

## License

MIT License
