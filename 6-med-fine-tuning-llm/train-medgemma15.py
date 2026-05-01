
from unsloth import FastModel
from unsloth.chat_templates import get_chat_template
from unsloth.chat_templates import standardize_data_formats
from unsloth.chat_templates import train_on_responses_only
import torch
from transformers import TextStreamer
from datasets import load_dataset
from trl import SFTTrainer, SFTConfig


model, tokenizer = FastModel.from_pretrained(
    model_name = "../medgemma15-4b",
    max_seq_length = 2048,
    load_in_4bit = False, 
    load_in_8bit = False, 
    full_finetuning = False,
    use_gradient_checkpointing = True,
    local_files_only=True,
)

model = FastModel.get_peft_model(
    model,
    finetune_vision_layers     = False,
    finetune_language_layers   = True,
    finetune_attention_modules = False,
    finetune_mlp_modules       = True,
    r = 16, 
    lora_alpha = 16, 
    lora_dropout = 0,
    bias = "none",
    random_state = 3407,
)

tokenizer = get_chat_template(
    tokenizer,
    chat_template = "gemma-3",
)

# dataset = load_dataset("mlabonne/FineTome-100k", split = "train")
dataset = load_dataset('json', data_files='./med-train-dateset.json', split='train')
dataset = standardize_data_formats(dataset)

print(dataset[1])

def formatting_prompts_func(examples):
   convos = examples["conversations"]
   texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False).removeprefix('<bos>') for convo in convos]
   return { "text" : texts, }

dataset = dataset.map(formatting_prompts_func, batched = True)
print(dataset[1]["text"])

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    eval_dataset = None,
    args = SFTConfig(
        dataset_text_field = "text",
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        # num_train_epochs = 1, # Set this for 1 full training run.
        max_steps = 240,
        learning_rate = 2e-4,
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.001,
        lr_scheduler_type = "linear",
        seed = 3407,
        report_to = "none",
    ),
)

trainer = train_on_responses_only(
    trainer,
    instruction_part = "<start_of_turn>user\n",
    response_part = "<start_of_turn>model\n",
)

tokenizer.decode(trainer.train_dataset[100]["input_ids"])
tokenizer.decode([tokenizer.pad_token_id if x == -100 else x for x in trainer.train_dataset[100]["labels"]]).replace(tokenizer.pad_token, " ")

gpu_stats = torch.cuda.get_device_properties(0)
start_gpu_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
max_memory = round(gpu_stats.total_memory / 1024 / 1024 / 1024, 3)
print(f"GPU = {gpu_stats.name}. Max memory = {max_memory} GB.")
print(f"{start_gpu_memory} GB of memory reserved.")

trainer_stats = trainer.train()

used_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
used_memory_for_lora = round(used_memory - start_gpu_memory, 3)
used_percentage = round(used_memory / max_memory * 100, 3)
lora_percentage = round(used_memory_for_lora / max_memory * 100, 3)
print(f"{trainer_stats.metrics['train_runtime']} seconds used for training.")
print(
    f"{round(trainer_stats.metrics['train_runtime']/60, 2)} minutes used for training."
)
print(f"Peak reserved memory = {used_memory} GB.")
print(f"Peak reserved memory for training = {used_memory_for_lora} GB.")
print(f"Peak reserved memory % of max memory = {used_percentage} %.")
print(f"Peak reserved memory for training % of max memory = {lora_percentage} %.")

# tokenizer = get_chat_template(
#     tokenizer,
#     chat_template = "gemma-3",
# )

messages = [{
    "role": "user",
    "content": [{"type" : "text", "text" : "怀孕26周今天宝宝一天没动弹了怎么回事？",}]
}]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt = True, # Must add for generation
    tokenize = True,
    return_tensors = "pt",
    return_dict = True,
)
_ = model.generate(
    **inputs.to("cuda"),
    max_new_tokens = 64,
    temperature = 1.0, top_p = 0.95, top_k = 64,
    streamer = TextStreamer(tokenizer, skip_prompt = True),
)

# model.save_pretrained("medgemma-fine-tuned-lora")
# tokenizer.save_pretrained("gemma-3")