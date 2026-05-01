
from unsloth import FastLanguageModel
from unsloth.chat_templates import train_on_responses_only
import torch
from transformers import TextStreamer
from datasets import load_dataset
from unsloth.chat_templates import standardize_sharegpt
from trl import SFTConfig, SFTTrainer


model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "../oss-20b",
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
    r = 16, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0,
    bias = "none",
    use_gradient_checkpointing = "unsloth",
    random_state = 3407,
    use_rslora = False,
    loftq_config = None,
)

messages = [
    {"role": "user", "content": "怀孕26周今天宝宝一天没动弹了怎么回事？"},
]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt = True,
    return_tensors = "pt",
    return_dict = True,
    reasoning_effort = "low",
).to("cuda")

print("=======")
_ = model.generate(**inputs, max_new_tokens = 256, streamer = TextStreamer(tokenizer))
print("=======")

# def formatting_prompts_func(examples):
#     convos = examples["messages"]
#     texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False) for convo in convos]
#     return { "text" : texts, }
    
def formatting_prompts_func(examples):
   convos = examples["conversations"]
   texts = [tokenizer.apply_chat_template(convo, tokenize = False, add_generation_prompt = False).removeprefix('<bos>') for convo in convos]
   return { "text" : texts, }

dataset = load_dataset('json', data_files='./med-train-dateset.json', split='train')

dataset = standardize_sharegpt(dataset)
dataset = dataset.map(formatting_prompts_func, batched = True,)

print(dataset[0]['text'])

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    args = SFTConfig(
        per_device_train_batch_size = 1,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        # num_train_epochs = 1, # Set this for 1 full training run.
        max_steps = 90,
        learning_rate = 2e-4,
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.001,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
        report_to = "none",
    ),
)

gpt_oss_kwargs = dict(instruction_part = "<|start|>user<|message|>", response_part="<|start|>assistant<|channel|>final<|message|>")

trainer = train_on_responses_only(
    trainer,
    **gpt_oss_kwargs,
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

messages = [
    {"role": "system", "content": "下面是一些描述一些任务的说明。编写适当完成每个请求的响应。"},
    {"role": "user", "content": "怀孕26周今天宝宝一天没动弹了怎么回事？"},
]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt = True,
    return_tensors = "pt",
    return_dict = True,
    reasoning_effort = "low",
).to("cuda")
_ = model.generate(**inputs, max_new_tokens = 64, streamer = TextStreamer(tokenizer))

# model.save_pretrained("finetuned_model")