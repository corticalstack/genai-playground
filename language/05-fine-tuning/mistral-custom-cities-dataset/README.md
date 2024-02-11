conda create --name genaiplayground python=3.9
conda install cudatoolkit xformers bitsandbytes pytorch pytorch-cuda=11.8   -c pytorch -c nvidia -c xformers -c conda-forge -y
export BNB_CUDA_VERSION=118
python -m bitsandbytes

pip install triton
conda install conda-forge::git-lfs
