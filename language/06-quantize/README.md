### Creation of conda enviroment
conda create --name genaiplayground_quant python=3.11.7
conda activate genaiplayground_quant

conda install cudatoolkit xformers bitsandbytes pytorch pytorch-cuda=12.1 -c pytorch -c nvidia -c xformers -c conda-forge -y
conda install -c conda-forge cudatoolkit-dev
export CUDA_HOME=/home/ubuntu/.conda/envs/genaiplayground_quant

conda install conda-forge::requests

git clone https://github.com/casper-hansen/AutoAWQ
cd AutoAWQ
pip install -e .

pip install zstandard

conda install -c conda-forge ipywidgets
conda install conda-forge::git-lfs

git clone https://github.com/turboderp/exllamav2
pip install -e exllamav2

pip install -q auto-gptq