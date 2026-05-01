root@autodl-container-94szt5h5u4-5ecd3acd:~/autodl-tmp/code/5-med-eval# sh 3-eval-original-qwen.sh
2026-04-28 22:56:53 - evalscope - INFO: Args: Task config is provided with TaskConfig type.
2026-04-28 22:56:54 - evalscope - INFO: Running with native backend
2026-04-28 22:56:54 - evalscope - INFO: Dump task config to ./outputs/20260428_225653/configs/task_config_bc0ff9.yaml
2026-04-28 22:56:54 - evalscope - INFO: {
    "model": "../qwen25-14b",
    "model_id": "qwen25-14b",
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
    "work_dir": "./outputs/20260428_225653",
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
2026-04-28 22:56:54 - evalscope - INFO: Start loading benchmark dataset: general_qa
2026-04-28 22:56:54 - evalscope - WARNING: No specific dataset file found, loading the first found file: qa/med-dataset-valid.jsonl
Processing records: 100%|███████████████████████████████████████████████████████████████████| 256/256 [00:00<00:00, 158556.09it/s]
2026-04-28 22:56:54 - evalscope - INFO: Start evaluating 1 subsets of the general_qa: ['med']
2026-04-28 22:56:54 - evalscope - INFO: Evaluating subset: med                                                                    
2026-04-28 22:56:54 - evalscope - INFO: Getting predictions for subset: med                                                       
2026-04-28 22:56:54 - evalscope - INFO: Processing 256 samples, if data is large, it may take a while.                            
2026-04-28 22:56:54 - evalscope - INFO: Loading model for prediction...                                                           
2026-04-28 22:56:54 - evalscope - INFO: Creating model ../qwen25-14b with eval_type=openai_api base_url=http://127.0.0.1:8000/v1, config={'retries': 5, 'retry_interval': 10, 'batch_size': 1, 'temperature': 0.0}, model_args={}                                   
2026-04-28 22:56:54 - evalscope - INFO: Model loaded successfully.                                                                
2026-04-28 22:57:54 - evalscope - INFO: Predicting[general_qa@med]:    2%| 5/256 [Elapsed: 01:00 < Remaining: 39:33,  9.45s/it]   
2026-04-28 22:58:54 - evalscope - INFO: Predicting[general_qa@med]:    7%| 17/256 [Elapsed: 02:00 < Remaining: 21:49,  5.48s/it]  
2026-04-28 22:59:54 - evalscope - INFO: Predicting[general_qa@med]:   12%| 30/256 [Elapsed: 03:00 < Remaining: 17:35,  4.67s/it]  
2026-04-28 23:00:54 - evalscope - INFO: Predicting[general_qa@med]:   17%| 44/256 [Elapsed: 04:00 < Remaining: 16:23,  4.64s/it]  
2026-04-28 23:01:54 - evalscope - INFO: Predicting[general_qa@med]:   22%| 56/256 [Elapsed: 05:00 < Remaining: 16:04,  4.82s/it]  
2026-04-28 23:02:54 - evalscope - INFO: Predicting[general_qa@med]:   28%| 71/256 [Elapsed: 06:00 < Remaining: 12:44,  4.13s/it]  
2026-04-28 23:03:54 - evalscope - INFO: Predicting[general_qa@med]:   33%| 84/256 [Elapsed: 07:00 < Remaining: 11:50,  4.13s/it]  
2026-04-28 23:04:54 - evalscope - INFO: Predicting[general_qa@med]:   38%| 97/256 [Elapsed: 08:00 < Remaining: 11:10,  4.22s/it]  
2026-04-28 23:05:54 - evalscope - INFO: Predicting[general_qa@med]:   43%| 109/256 [Elapsed: 09:00 < Remaining: 10:57,  4.48s/it] 
2026-04-28 23:06:54 - evalscope - INFO: Predicting[general_qa@med]:   47%| 121/256 [Elapsed: 10:00 < Remaining: 11:43,  5.21s/it] 
2026-04-28 23:07:54 - evalscope - INFO: Predicting[general_qa@med]:   52%| 134/256 [Elapsed: 11:00 < Remaining: 10:09,  4.99s/it] 
2026-04-28 23:08:54 - evalscope - INFO: Predicting[general_qa@med]:   58%| 148/256 [Elapsed: 12:00 < Remaining: 08:19,  4.63s/it] 
2026-04-28 23:09:54 - evalscope - INFO: Predicting[general_qa@med]:   62%| 160/256 [Elapsed: 13:00 < Remaining: 08:45,  5.47s/it] 
2026-04-28 23:10:54 - evalscope - INFO: Predicting[general_qa@med]:   68%| 174/256 [Elapsed: 14:00 < Remaining: 06:25,  4.70s/it] 
2026-04-28 23:11:55 - evalscope - INFO: Predicting[general_qa@med]:   72%| 185/256 [Elapsed: 15:00 < Remaining: 06:16,  5.30s/it] 
2026-04-28 23:12:55 - evalscope - INFO: Predicting[general_qa@med]:   77%| 198/256 [Elapsed: 16:00 < Remaining: 04:36,  4.76s/it] 
2026-04-28 23:13:55 - evalscope - INFO: Predicting[general_qa@med]:   81%| 208/256 [Elapsed: 17:00 < Remaining: 05:16,  6.59s/it] 
2026-04-28 23:14:55 - evalscope - INFO: Predicting[general_qa@med]:   86%| 221/256 [Elapsed: 18:01 < Remaining: 02:58,  5.11s/it] 
2026-04-28 23:15:55 - evalscope - INFO: Predicting[general_qa@med]:   91%| 233/256 [Elapsed: 19:01 < Remaining: 01:52,  4.91s/it] 
2026-04-28 23:16:55 - evalscope - INFO: Predicting[general_qa@med]:   96%| 245/256 [Elapsed: 20:01 < Remaining: 01:02,  5.66s/it] 
2026-04-28 23:17:42 - evalscope - INFO: Predicting[general_qa@med]:  100%| 256/256 [Elapsed: 20:48 < Remaining: 00:00,  4.39s/it] 
Predicting[general_qa@med]: 100%|███████████████████████████████████████████████████████████████| 256/256 [20:48<00:00,  4.88s/it]
2026-04-28 23:17:42 - evalscope - INFO: Finished getting predictions for subset: med.                                             
2026-04-28 23:17:42 - evalscope - INFO: Getting reviews for subset: med                                                           
2026-04-28 23:17:42 - evalscope - INFO: Reviewing 256 samples, if data is large, it may take a while.                             
Evaluating [general_qa]:   0%|                                                                          | 0/1 [20:48<?, ?subset/s/root/autodl-tmp/code/5-med-eval/.venv/lib/python3.12/site-packages/jieba/__init__.py:44: SyntaxWarning: invalid escape sequence '\.'
  re_han_default = re.compile("([\u4E00-\u9FD5a-zA-Z0-9+#&\._%\-]+)", re.U)
/root/autodl-tmp/code/5-med-eval/.venv/lib/python3.12/site-packages/jieba/__init__.py:46: SyntaxWarning: invalid escape sequence '\s'
  re_skip_default = re.compile("(\r\n|\s)", re.U)
/root/autodl-tmp/code/5-med-eval/.venv/lib/python3.12/site-packages/jieba/finalseg/__init__.py:78: SyntaxWarning: invalid escape sequence '\.'
  re_skip = re.compile("([a-zA-Z0-9]+(?:\.\d+)?%?)")
Building prefix dict from the default dictionary ...
2026-04-28 23:17:44,424 - jieba - DEBUG: Building prefix dict from the default dictionary ...
Dumping model to file cache /tmp/jieba.cache
2026-04-28 23:17:44,731 - jieba - DEBUG: Dumping model to file cache /tmp/jieba.cache
Loading model cost 0.340 seconds.
2026-04-28 23:17:44,763 - jieba - DEBUG: Loading model cost 0.340 seconds.
Prefix dict has been built successfully.
2026-04-28 23:17:44,763 - jieba - DEBUG: Prefix dict has been built successfully.
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
/root/autodl-tmp/code/5-med-eval/.venv/lib/python3.12/site-packages/rouge_chinese/rouge.py:93: SyntaxWarning: invalid escape sequence '\?'
  para = re.sub('([。！？\?])([^”’])', r"\1\n\2", para)
/root/autodl-tmp/code/5-med-eval/.venv/lib/python3.12/site-packages/rouge_chinese/rouge.py:94: SyntaxWarning: invalid escape sequence '\.'
  para = re.sub('(\.{6})([^”’])', r"\1\n\2", para)
/root/autodl-tmp/code/5-med-eval/.venv/lib/python3.12/site-packages/rouge_chinese/rouge.py:96: SyntaxWarning: invalid escape sequence '\?'
  para = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)
/root/autodl-tmp/code/5-med-eval/.venv/lib/python3.12/site-packages/nltk/translate/bleu_score.py:577: UserWarning: 
The hypothesis contains 0 counts of 2-gram overlaps.
Therefore the BLEU score evaluates to 0, independently of
how many N-gram overlaps of lower order it contains.
Consider using lower n-gram order or use SmoothingFunction()
  warnings.warn(_msg)
2026-04-28 23:17:46 - evalscope - INFO: Reviewing[general_qa@med]:  100%| 256/256 [Elapsed: 00:04 < Remaining: 00:00,  8.85it/s]  
Reviewing[general_qa@med]: 100%|████████████████████████████████████████████████████████████████| 256/256 [00:04<00:00, 58.09it/s]
2026-04-28 23:17:46 - evalscope - INFO: Finished reviewing subset: med. Total reviewed: 256                                       
2026-04-28 23:17:46 - evalscope - INFO: Aggregating scores for subset: med                                                        
2026-04-28 23:17:46 - evalscope - INFO: Evaluating [general_qa] 100%| 1/1 [Elapsed: 20:52 < Remaining: 00:00, 1252.60s/subset]    
Evaluating [general_qa]: 100%|████████████████████████████████████████████████████████████████| 1/1 [20:52<00:00, 1252.60s/subset]
2026-04-28 23:17:46 - evalscope - INFO: Generating report...
2026-04-28 23:17:46 - evalscope - INFO: 
general_qa report table:
+------------+------------+----------------+----------+-------+---------+---------+
| Model      | Dataset    | Metric         | Subset   |   Num |   Score | Cat.0   |
+============+============+================+==========+=======+=========+=========+
| qwen25-14b | general_qa | mean_bleu-1    | med      |   256 |  0.108  | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_bleu-2    | med      |   256 |  0.0131 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_bleu-3    | med      |   256 |  0.0021 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_bleu-4    | med      |   256 |  0.0004 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-1-R | med      |   256 |  0.34   | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-1-P | med      |   256 |  0.1067 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-1-F | med      |   256 |  0.1552 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-2-R | med      |   256 |  0.055  | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-2-P | med      |   256 |  0.0142 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-2-F | med      |   256 |  0.0214 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-L-R | med      |   256 |  0.2905 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-L-P | med      |   256 |  0.0724 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-L-F | med      |   256 |  0.1095 | default |
+------------+------------+----------------+----------+-------+---------+---------+ 

2026-04-28 23:17:46 - evalscope - INFO: Skipping report analysis (`analysis_report=False`).
2026-04-28 23:17:46 - evalscope - INFO: Dump report to: ./outputs/20260428_225653/reports/qwen25-14b/general_qa.json 

2026-04-28 23:17:46 - evalscope - INFO: Benchmark general_qa evaluation finished.
2026-04-28 23:17:46 - evalscope - INFO: Overall report table: 
+------------+------------+----------------+----------+-------+---------+---------+
| Model      | Dataset    | Metric         | Subset   |   Num |   Score | Cat.0   |
+============+============+================+==========+=======+=========+=========+
| qwen25-14b | general_qa | mean_bleu-1    | med      |   256 |  0.108  | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_bleu-2    | med      |   256 |  0.0131 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_bleu-3    | med      |   256 |  0.0021 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_bleu-4    | med      |   256 |  0.0004 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-1-R | med      |   256 |  0.34   | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-1-P | med      |   256 |  0.1067 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-1-F | med      |   256 |  0.1552 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-2-R | med      |   256 |  0.055  | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-2-P | med      |   256 |  0.0142 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-2-F | med      |   256 |  0.0214 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-L-R | med      |   256 |  0.2905 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-L-P | med      |   256 |  0.0724 | default |
+------------+------------+----------------+----------+-------+---------+---------+
| qwen25-14b | general_qa | mean_Rouge-L-F | med      |   256 |  0.1095 | default |
+------------+------------+----------------+----------+-------+---------+---------+ 

2026-04-28 23:17:46 - evalscope - INFO: Finished evaluation for qwen25-14b on ['general_qa']
2026-04-28 23:17:46 - evalscope - INFO: Output directory: ./outputs/20260428_225653