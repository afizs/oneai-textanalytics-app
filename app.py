import gradio as gr
from oneai import oneai_pipeline


demo = gr.Interface(
    fn=oneai_pipeline,
    inputs=gr.Textbox(lines=2, placeholder="Name Here..."),
    outputs="text",
)
demo.launch(share=True)
