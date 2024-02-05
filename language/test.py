from transformers import AutoConfig, AutoModel, AutoTokenizer
model_id = "CorticalStack/OpenHermes-Mistral-7B-GGUF"

config = AutoConfig.from_pretrained(model_id)
model = AutoModel.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)