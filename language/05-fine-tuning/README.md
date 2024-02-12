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
