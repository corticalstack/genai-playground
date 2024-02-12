### Evaluation Harness
[LLM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness)

### Creation of conda enviroment
conda create --name genaiplayground_eval python=3.11.7
conda activate genaiplayground_eval

git clone https://github.com/EleutherAI/lm-evaluation-harness
cd lm-evaluation-harness/
pip install -e .


###  Running evaluation from the command line 
```
lm_eval --model hf --model_args pretrained=CorticalStack/OpenHermes-Mistral-7B-GPTQ --tasks hellaswag --device cuda:0 --batch_size 8
```

### Example output
hf (pretrained=CorticalStack/travel-mistral-7B-16b-base), gen_kwargs: (None), limit: None, num_fewshot: None, batch_size: 8
|  Tasks  |Version|Filter|n-shot| Metric |Value |   |Stderr|
|---------|------:|------|------|--------|-----:|---|-----:|
|hellaswag|      1|none  |None  |acc     |0.6138|±  |0.0049|
|         |       |none  |None  |acc_norm|0.8067|±  |0.0039|