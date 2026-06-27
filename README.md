# Task 5: Mental Health Support Chatbot

## Project Overview
This repository contains a lightweight, empathetic conversational AI agent specifically configured for mental health support and emotional wellness guidance. The system integrates a transformer-based causal language model with an interactive user interface to deliver responsive, text-based emotional validation.

## Architectural Design
- **Core Model:** DistilGPT2 (Generative Causal Language Model)
- **Parameters:** ~82 Million (Optimized for local edge deployment and CPU environments)
- **Tokenization:** Pre-trained GPT2 Byte-Pair Encoding (BPE) tokenizer configuration
- **Interface Layer:** Streamlit Web Application Framework
- **Backend Engine:** PyTorch

---

## Technical Workflow Pipeline
1. **Tokenization Strategy:**
   The user prompt is structurally prepared with customized context wrappers (`Context: {prompt} | Response:`) to ensure proper causal context alignment. Sequences are strictly controlled using left-padding mechanics and EOS (End of Sequence) padding token bindings.

2. **Inference Execution Setup:**
   The generation loop employs explicit hyper-parameter controls to optimize conversational diversity while reducing semantic drift:
   - `do_sample=True` enables probabilistic token sampling.
   - `top_k=50` limits the token search space to high-probability candidates.
   - `top_p=0.9` ensures cumulative nucleus threshold filtering for coherent phrasing.

3. **Fallback Architecture:**
   An integrated exception-handling layer maps unexpected generation behaviors to default grounding scripts, preventing runtime application layer crashes during edge cases.

---

## Workspace Setup & Execution

### Prerequisites
Ensure your local environment or active virtual environment (`.venv`) contains the required dependencies:
```bash
pip install torch transformers datasets streamlit accelerate