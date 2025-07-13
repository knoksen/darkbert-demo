# DarkBERT Pro UI – Powered by S2W-AI

A modern Gradio app for masked language modeling, with batch mode, prompt library, download, and Terratek/Njord branding.

## Usage

1. Install dependencies:
    pip install -r requirements.txt
2. Run the app:
    python app.py
3. Open <http://127.0.0.1:7860> in your browser

**Requires access to s2w-ai/DarkBERT.**

### Downloading DarkBERT Locally

DarkBERT is a gated model. Request access at <https://huggingface.co/s2w-ai/DarkBERT> and run `huggingface-cli login` once granted.
Download `config.json`, `pytorch_model.bin`, `tokenizer.json`, `vocab.json`, `merges.txt`, `tokenizer_config.json`, and `special_tokens_map.json` and place them in a new `darkbert_cache/` directory (already listed in `.gitignore`).
You may also set `cache_dir="darkbert_cache"` when creating the `pipeline` in `app.py`.

---

Standard prompts can be edited in `app.py` (see the `STANDARD_PROMPTS` list).

## Docker Quickstart

1. Build the image:
   docker build -t darkbert-demo .

2. Run the container:
   docker run -p 7860:7860 -v C:\Users\knoks\darkbert-demo/darkbert_cache:/app/darkbert_cache darkbert-demo

3. Open <http://127.0.0.1:7860> in your browser.

4. For healthcheck (optional):
   curl <http://localhost:7860/health>
