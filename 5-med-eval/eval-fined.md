root@autodl-container-94szt5h5u4-5ecd3acd:~/autodl-tmp/code/5-med-eval# sh  5-eval-finetuned-qwen.sh

libgomp: Invalid value for environment variable OMP_NUM_THREADS
2026-04-29 14:33:28 - evalscope - INFO: Args: Task config is provided with TaskConfig type.
2026-04-29 14:33:28 - evalscope - INFO: Running with native backend
2026-04-29 14:33:28 - evalscope - INFO: Dump task config to ./outputs/20260429_143328/configs/task_config_9dfde9.yaml
2026-04-29 14:33:28 - evalscope - INFO: {
    "model": "my-lora",
    "model_id": "my-lora",
    "model_args": {},
    "model_task": "text_generation",
    "chat_template": null,
    "datasets": [
        "general_qa"
    ],
    "dataset_args": {
        "general_qa": {
            "name": "general_qa",
            "dataset_id": "qa",
            "output_types": [
                "generation"
            ],
            "subset_list": [
                "med"
            ],
            "default_subset": "default",
            "few_shot_num": 0,
            "few_shot_random": false,
            "train_split": null,
            "eval_split": "test",
            "prompt_template": "请回答问题\n{question}",
            "few_shot_prompt_template": null,
            "system_prompt": null,
            "query_template": null,
            "pretty_name": "General-QA",
            "description": "A general question answering dataset for custom evaluation. For detailed instructions on how to use this benchmark, please refer to the [User Guide](https://evalscope.readthedocs.io/en/latest/advanced_guides/custom_dataset/llm.html#qa).",
            "tags": [
                "QA",
                "Custom"
            ],
            "filters": null,
            "metric_list": [
                "BLEU",
                "Rouge"
            ],
            "aggregation": "mean",
            "shuffle": false,
            "shuffle_choices": false,
            "force_redownload": false,
            "review_timeout": null,
            "extra_params": {},
            "sandbox_config": {}
        }
    },
    "dataset_dir": "/root/.cache/modelscope/hub/datasets",
    "dataset_hub": "modelscope",
    "repeats": 1,
    "generation_config": {
        "batch_size": 1,
        "temperature": 0.0
    },
    "eval_type": "openai_api",
    "eval_backend": "Native",
    "eval_config": null,
    "limit": 256,
    "eval_batch_size": 1,
    "use_cache": null,
    "rerun_review": false,
    "work_dir": "./outputs/20260429_143328",
    "no_timestamp": false,
    "ignore_errors": false,
    "debug": false,
    "seed": 42,
    "api_url": "http://127.0.0.1:8000/v1",
    "timeout": null,
    "stream": null,
    "judge_strategy": "auto",
    "judge_worker_num": 1,
    "judge_model_args": {},
    "analysis_report": false,
    "use_sandbox": false,
    "sandbox_type": "docker",
    "sandbox_manager_config": {},
    "evalscope_version": "1.4.1"
}
2026-04-29 14:33:28 - evalscope - INFO: Start loading benchmark dataset: general_qa
2026-04-29 14:33:28 - evalscope - WARNING: No specific dataset file found, loading the first found file: qa/med-dataset-valid.jsonl
Processing records: 100%|████████████████████████████████████| 256/256 [00:00<00:00, 143414.16it/s]
2026-04-29 14:33:28 - evalscope - INFO: Start evaluating 1 subsets of the general_qa: ['med']
2026-04-29 14:33:28 - evalscope - INFO: Evaluating subset: med                                     
2026-04-29 14:33:28 - evalscope - INFO: Getting predictions for subset: med                        
2026-04-29 14:33:28 - evalscope - INFO: Processing 256 samples, if data is large, it may take a while.
2026-04-29 14:33:28 - evalscope - INFO: Loading model for prediction...                            
2026-04-29 14:33:28 - evalscope - INFO: Creating model my-lora with eval_type=openai_api base_url=http://127.0.0.1:8000/v1, config={'retries': 5, 'retry_interval': 10, 'batch_size': 1, 'temperature': 0.0}, model_args={}
2026-04-29 14:33:28 - evalscope - INFO: Model loaded successfully.                                 
2026-04-29 14:34:28 - evalscope - INFO: Predicting[general_qa@med]:   20%| 51/256 [Elapsed: 01:00 < Remaining: 03:55,  1.15s/it]                                                                      
2026-04-29 14:35:28 - evalscope - INFO: Predicting[general_qa@med]:   41%| 104/256 [Elapsed: 02:00 < Remaining: 03:17,  1.30s/it]                                                                     
2026-04-29 14:36:28 - evalscope - INFO: Predicting[general_qa@med]:   46%| 117/256 [Elapsed: 03:00 < Remaining: 01:39,  1.40it/s]                                                                     
2026-04-29 14:37:28 - evalscope - INFO: Predicting[general_qa@med]:   49%| 126/256 [Elapsed: 04:00 < Remaining: 10:33,  4.87s/it]                                                                     
2026-04-29 14:38:28 - evalscope - INFO: Predicting[general_qa@med]:   53%| 135/256 [Elapsed: 05:00 < Remaining: 03:32,  1.75s/it]                                                                     
2026-04-29 14:39:28 - evalscope - INFO: Predicting[general_qa@med]:   57%| 147/256 [Elapsed: 06:00 < Remaining: 06:20,  3.49s/it]                                                                     
2026-04-29 14:40:29 - evalscope - INFO: Predicting[general_qa@med]:   81%| 207/256 [Elapsed: 07:00 < Remaining: 00:41,  1.17it/s]                                                                     
2026-04-29 14:41:17 - evalscope - INFO: Predicting[general_qa@med]:  100%| 256/256 [Elapsed: 07:48 < Remaining: 00:00,  1.24it/s]                                                                     
Predicting[general_qa@med]: 100%|████████████████████████████████| 256/256 [07:48<00:00,  1.83s/it]
2026-04-29 14:41:17 - evalscope - INFO: Finished getting predictions for subset: med.              
2026-04-29 14:41:17 - evalscope - INFO: Getting reviews for subset: med                            
2026-04-29 14:41:17 - evalscope - INFO: Reviewing 256 samples, if data is large, it may take a while.
Evaluating [general_qa]:   0%|                                           | 0/1 [07:48<?, ?subset/s]
libgomp: Invalid value for environment variable OMP_NUM_THREADS            | 0/256 [00:00<?, ?it/s]
Building prefix dict from the default dictionary ...
2026-04-29 14:41:18,452 - jieba - DEBUG: Building prefix dict from the default dictionary ...
Loading model from cache /tmp/jieba.cache
2026-04-29 14:41:18,452 - jieba - DEBUG: Loading model from cache /tmp/jieba.cache
Loading model cost 0.508 seconds.
2026-04-29 14:41:18,960 - jieba - DEBUG: Loading model cost 0.508 seconds.
Prefix dict has been built successfully.
2026-04-29 14:41:18,960 - jieba - DEBUG: Prefix dict has been built successfully.
/root/autodl-tmp/code/5-med-eval/.venv/lib/python3.12/site-packages/nltk/translate/bleu_score.py:577: UserWarning: 
The hypothesis contains 0 counts of 3-gram overlaps.
Therefore the BLEU score evaluates to 0, independently of
how many N-gram overlaps of lower order it contains.
Consider using lower n-gram order or use SmoothingFunction()
  warnings.warn(_msg)
/root/autodl-tmp/code/5-med-eval/.venv/lib/python3.12/site-packages/nltk/translate/bleu_score.py:577: UserWarning: 
The hypothesis contains 0 counts of 4-gram overlaps.
Therefore the BLEU score evaluates to 0, independently of
how many N-gram overlaps of lower order it contains.
Consider using lower n-gram order or use SmoothingFunction()
  warnings.warn(_msg)
/root/autodl-tmp/code/5-med-eval/.venv/lib/python3.12/site-packages/nltk/translate/bleu_score.py:577: UserWarning: 
The hypothesis contains 0 counts of 2-gram overlaps.
Therefore the BLEU score evaluates to 0, independently of
how many N-gram overlaps of lower order it contains.
Consider using lower n-gram order or use SmoothingFunction()
  warnings.warn(_msg)
2026-04-29 14:41:19 - evalscope - INFO: Reviewing[general_qa@med]:  100%| 256/256 [Elapsed: 00:02 < Remaining: 00:00,  2.02s/it]                                                                      
Reviewing[general_qa@med]: 100%|████████████████████████████████| 256/256 [00:02<00:00, 104.20it/s]
2026-04-29 14:41:19 - evalscope - INFO: Finished reviewing subset: med. Total reviewed: 256        
2026-04-29 14:41:19 - evalscope - INFO: Aggregating scores for subset: med                         
2026-04-29 14:41:19 - evalscope - INFO: Evaluating [general_qa] 100%| 1/1 [Elapsed: 07:51 < Remaining: 00:00, 471.20s/subset]
Evaluating [general_qa]: 100%|██████████████████████████████████| 1/1 [07:51<00:00, 471.20s/subset]
2026-04-29 14:41:19 - evalscope - INFO: Generating report...
2026-04-29 14:41:19 - evalscope - INFO: 
general_qa report table:
+---------+------------+----------------+----------+-------+---------+---------+
| Model   | Dataset    | Metric         | Subset   |   Num |   Score | Cat.0   |
+=========+============+================+==========+=======+=========+=========+
| my-lora | general_qa | mean_bleu-1    | med      |   256 |  0.1635 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_bleu-2    | med      |   256 |  0.0358 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_bleu-3    | med      |   256 |  0.011  | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_bleu-4    | med      |   256 |  0.0051 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-1-R | med      |   256 |  0.2135 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-1-P | med      |   256 |  0.3054 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-1-F | med      |   256 |  0.2337 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-2-R | med      |   256 |  0.0484 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-2-P | med      |   256 |  0.0729 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-2-F | med      |   256 |  0.0535 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-L-R | med      |   256 |  0.1686 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-L-P | med      |   256 |  0.2586 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-L-F | med      |   256 |  0.1857 | default |
+---------+------------+----------------+----------+-------+---------+---------+ 

2026-04-29 14:41:19 - evalscope - INFO: Skipping report analysis (`analysis_report=False`).
2026-04-29 14:41:19 - evalscope - INFO: Dump report to: ./outputs/20260429_143328/reports/my-lora/general_qa.json 

2026-04-29 14:41:19 - evalscope - INFO: Benchmark general_qa evaluation finished.
2026-04-29 14:41:19 - evalscope - INFO: Overall report table: 
+---------+------------+----------------+----------+-------+---------+---------+
| Model   | Dataset    | Metric         | Subset   |   Num |   Score | Cat.0   |
+=========+============+================+==========+=======+=========+=========+
| my-lora | general_qa | mean_bleu-1    | med      |   256 |  0.1635 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_bleu-2    | med      |   256 |  0.0358 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_bleu-3    | med      |   256 |  0.011  | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_bleu-4    | med      |   256 |  0.0051 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-1-R | med      |   256 |  0.2135 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-1-P | med      |   256 |  0.3054 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-1-F | med      |   256 |  0.2337 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-2-R | med      |   256 |  0.0484 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-2-P | med      |   256 |  0.0729 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-2-F | med      |   256 |  0.0535 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-L-R | med      |   256 |  0.1686 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-L-P | med      |   256 |  0.2586 | default |
+---------+------------+----------------+----------+-------+---------+---------+
| my-lora | general_qa | mean_Rouge-L-F | med      |   256 |  0.1857 | default |
+---------+------------+----------------+----------+-------+---------+---------+ 

2026-04-29 14:41:19 - evalscope - INFO: Finished evaluation for my-lora on ['general_qa']
2026-04-29 14:41:19 - evalscope - INFO: Output directory: ./outputs/20260429_143328