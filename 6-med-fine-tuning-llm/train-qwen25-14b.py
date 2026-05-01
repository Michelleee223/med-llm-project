
from unsloth import FastLanguageModel
from unsloth import apply_chat_template
from unsloth import is_bfloat16_supported
from datasets import load_dataset
from trl import SFTTrainer
from transformers import TrainingArguments
from transformers import TextStreamer
import torch

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "../qwen25-14b",
    dtype = None,
    max_seq_length = 2048,
    load_in_4bit = False, 
    load_in_8bit = False, 
    full_finetuning = False,
    use_gradient_checkpointing = True,
    local_files_only=True,
)

model = FastLanguageModel.get_peft_model(
   model,
   r = 16, 
   target_modules = ["q_proj", "k_proj", "v_proj", "o_proj","gate_proj", "up_proj", "down_proj",],
   lora_alpha = 16,
   lora_dropout = 0, 
   bias = "none",    
   use_gradient_checkpointing = "unsloth", 
   random_state = 3407,
   use_rslora = False, 
   loftq_config = None, 
)

dataset = load_dataset('json', data_files='./med-dataset-train.json', split='train')
chat_template = """你是一个专业的医疗健康顾问，能够提供有关体检指标异常的专业健康建议。

### 指令:
{INPUT}

### 回应:
{OUTPUT}"""

dataset = apply_chat_template(
    dataset,
    tokenizer=tokenizer,
    chat_template=chat_template,
   
)
print(dataset[0])


trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    dataset_text_field = "text",
    max_seq_length = 2048,
    dataset_num_proc = 2,
    packing = False, 
    args = TrainingArguments(
        per_device_train_batch_size = 64,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        # max_steps = 2,
        num_train_epochs = 1,
        learning_rate = 2e-4,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
        report_to = "none", 
    ),
)

trainer_stats = trainer.train()

FastLanguageModel.for_inference(model) 
messages = [                   
    {"role": "user", "content": "我肚子疼"},
]
input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt = True,
    return_tensors = "pt",
).to("cuda")

text_streamer = TextStreamer(tokenizer, skip_prompt = True)
_ = model.generate(input_ids, streamer = text_streamer, max_new_tokens = 1024, pad_token_id = tokenizer.eos_token_id)

model.save_pretrained("../qwen25-14b-finetuned-lora")
