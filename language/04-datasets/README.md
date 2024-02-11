### Creation of conda enviroment
conda create --name genaiplayground_data python=3.11.7

conda activate genaiplayground_data

conda install cudatoolkit xformers bitsandbytes pytorch pytorch-cuda=11.8 -c pytorch -c nvidia -c xformers -c conda-forge -y

conda install -c conda-forge ipywidgets
conda install conda-forge::widgetsnbextension
conda install conda-forge::transformers
pip install chardet
pip install accelerate
conda install conda-forge::openai
