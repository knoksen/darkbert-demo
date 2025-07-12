import gradio as gr
from transformers import pipeline

STANDARD_PROMPTS = [
    "RagnarLocker, LockBit, and REvil are types of <mask>.",
    "Bitcoin is commonly used for <mask> on the dark web.",
    "Common attack vectors include <mask>.",
    "Tor and I2P are examples of <mask>.",
    "Stolen credentials are traded on <mask>.",
    "Popular ransomware families include <mask>.",
    "Cybercriminals often use <mask> for anonymity.",
    "The darknet is accessed using <mask>.",
    "Data breaches often lead to <mask>.",
    "The most targeted sectors are <mask>.",
]

pipe = pipeline('fill-mask', model='s2w-ai/DarkBERT', tokenizer='s2w-ai/DarkBERT')

def batch_fill_mask(prompts, top_k):
    results = []
    for prompt in prompts.split('\n'):
        if prompt.strip():
            try:
                preds = pipe(prompt.strip(), top_k=top_k)
                for p in preds:
                    results.append({
                        "Prompt": prompt,
                        "Prediction": p['sequence'],
                        "Score": p['score']
                    })
            except Exception as e:
                results.append({
                    "Prompt": prompt,
                    "Prediction": f"ERROR: {e}",
                    "Score": 0
                })
    return results

def insert_std_prompt(p, std):
    if not p: return std
    return p + '\n' + std if std else p

with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
    gr.Markdown("# ⚡️ DarkBERT: AI-Powered Masked Language for Cybersecurity & Darknet Analysis")

    with gr.Tab("Batch Mode"):
        with gr.Row():
            prompts = gr.Textbox(label="Enter prompts (one per line, use <mask>)", lines=7)
            top_k = gr.Slider(1, 10, value=5, step=1, label="Top K Predictions")
        with gr.Row():
            std_prompt = gr.Dropdown(STANDARD_PROMPTS, label="Standard Prompt", interactive=True)
            std_prompt.change(insert_std_prompt, inputs=[prompts, std_prompt], outputs=prompts)
        result_table = gr.Dataframe(headers=["Prompt", "Prediction", "Score"], label="Results", interactive=False)
        run_btn = gr.Button("Run Batch")
        run_btn.click(batch_fill_mask, inputs=[prompts, top_k], outputs=result_table)
        gr.DownloadButton(result_table, label="Download CSV")

    with gr.Tab("Single Prompt Mode"):
        single_prompt = gr.Textbox(label="Enter prompt (use <mask>)", lines=2)
        single_topk = gr.Slider(1, 10, value=5, step=1, label="Top K Predictions")
        single_result = gr.Dataframe(headers=["Prompt", "Prediction", "Score"], label="Results", interactive=False)
        def single_fill_mask(prompt, top_k):
            if not prompt.strip():
                return []
            try:
                preds = pipe(prompt.strip(), top_k=top_k)
                return [{"Prompt": prompt, "Prediction": p['sequence'], "Score": p['score']} for p in preds]
            except Exception as e:
                return [{"Prompt": prompt, "Prediction": f"ERROR: {e}", "Score": 0}]
        gr.Button("Predict").click(single_fill_mask, inputs=[single_prompt, single_topk], outputs=single_result)

    gr.Markdown("**Terratek/Njord & S2W-AI DarkBERT | Powered by Hugging Face | Bærekraftig cybersikkerhet**")

if __name__ == "__main__":
    demo.launch()
