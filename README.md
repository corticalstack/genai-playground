# 🚀 GenAI Playground

A comprehensive toolkit and collection of examples for working with Large Language Models (LLMs), from environment setup to advanced fine-tuning, quantization, and evaluation.

## 📚 Description

GenAI Playground provides a structured approach to experimenting with and deploying state-of-the-art language models. This repository contains practical examples and workflows for the entire LLM lifecycle, including environment setup, inference, dataset preparation, fine-tuning, quantization, model merging, and evaluation.

Each section includes Jupyter notebooks with detailed examples and conda environment configurations, making it easy to get started with different aspects of LLM development.

## ✨ Features

- **Environment Setup**: Ready-to-use conda environment configurations for different LLM tasks
- **Batch Inference**: Examples for running inference on LLMs with transformers
- **Inference Engines**: Integration with popular inference engines like VLLM and Ooba
- **Dataset Preparation**: Tools and examples for creating and formatting datasets for LLM training
- **Fine-tuning**:
  - Supervised Fine-Tuning (SFT) examples with various models and datasets
  - Direct Preference Optimization (DPO) implementations
  - Support for efficient fine-tuning methods like QLoRA and Unsloth
- **Quantization**: Examples for quantizing models to various formats (GGUF, GPTQ, AWQ, EXL2)
- **Model Merging**: Techniques for merging models using methods like SLERP, TIES, and DARE
- **Evaluation**: Integration with LLM Evaluation Harness for benchmarking model performance

## 🔧 Prerequisites

- CUDA-capable GPU
- Python 3.11.7
- Git
- Conda package manager

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/corticalstack/genai-playground.git
cd genai-playground
```

### 2. Set up the environment

Choose the appropriate environment based on your task, but see the [environment section README](01-environment/README.md) for more.

## 📚 Resources

- [Hugging Face Transformers Documentation](https://huggingface.co/docs/transformers/index)
- [PEFT Documentation](https://huggingface.co/docs/peft/index)
- [TRL Documentation](https://huggingface.co/docs/trl/index)
- [LLM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
