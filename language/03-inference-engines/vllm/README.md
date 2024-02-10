## Starting the vllm server
### Activate the conda environment
conda activate vllmenv

### Launch the vllm server
python -m vllm.entrypoints.openai.api_server --port 6090 --model /mnt/samssd/models/llm/TheBloke_OpenHermes-2.5-Mistral-7B-GPTQ