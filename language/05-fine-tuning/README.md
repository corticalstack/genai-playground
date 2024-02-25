### Creation of conda enviroment
conda create --name genaiplayground_tune python=3.11.7

conda activate genaiplayground_tune

conda install cudatoolkit xformers bitsandbytes pytorch pytorch-cuda=12.1 -c pytorch -c nvidia -c xformers -c conda-forge -y
conda install -c conda-forge cudatoolkit-dev

export CUDA_HOME=/home/ubuntu/.conda/envs/genaiplayground_tune

pip install flash-attn --no-build-isolation

conda install -c conda-forge ipywidgets
conda install conda-forge::widgetsnbextension
conda install conda-forge::transformers
pip install chardet
pip install accelerate
pip install "unsloth[conda] @ git+https://github.com/unslothai/unsloth.git"
conda install conda-forge::datasets
conda install conda-forge::git-lfs
conda install conda-forge::wandb


### Example code snippet for formatting OpenHermes-2.5 dataset into alpaca format
alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Response:
{}"""


def formatting_prompts_func(examples):
    convos = examples["conversations"]
    texts = []
    for convo in convos:
        human_dict = convo[0]
        gpt_dict = convo[1]
        instruction = human_dict['value']
        response = gpt_dict['value']
        text = alpaca_prompt.format(instruction, response) + EOS_TOKEN
        texts.append(text)
    return { "text" : texts, }

train_dataset_in_prompt_format = train_dataset.map(format_prompts, batched = True,)