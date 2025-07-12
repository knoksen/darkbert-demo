import gradio as gr
from transformers import pipeline

pipe = pipeline("fill-mask", model="s2w-ai/DarkBERT", tokenizer="s2w-ai/DarkBERT")

def fill_mask(text):
    results = pipe(text)
    return "\n".join([f"{r['sequence']} (score: {r['score']:.3f})" for r in results])

with gr.Blocks() as demo:
    gr.Markdown("# DarkBERT: Masked Language Model Demo")
    inp = gr.Textbox(label="Enter a sentence with <mask>")
    out = gr.Textbox(label="Predictions")
    btn = gr.Button("Predict")
    btn.click(fn=fill_mask, inputs=inp, outputs=out)

if __name__ == "__main__":
    demo.launch()
