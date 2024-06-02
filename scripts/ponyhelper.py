import os
import gradio as gr
from modules import scripts

class PonyhelperScript(scripts.Script):
    def __init__(self) -> None:
        super().__init__()

    def title(self):
        return "Ponyhelper"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Group():
            with gr.Accordion("Ponyhelper: Not Active", open=False) as acc:
                enable_score_prompt = gr.Checkbox(label="Enable Ponyhelper", value=False)
                score_slider = gr.Slider(minimum=1, maximum=9, step=1, value=9, label="Score Level")
                
                # Change Accordion name based on checkbox state
                enable_score_prompt.change(
                    fn=lambda x: gr.update(label=f"Ponyhelper: {'Active' if x else 'Not Active'}"),
                    inputs=enable_score_prompt,
                    outputs=acc
                )
                
        return [enable_score_prompt, score_slider]

    def process(self, p, enable_score_prompt, score_slider):
        if enable_score_prompt:
            score_positive_prefix = self.create_score_prefix(score_slider)
            score_negative_prefix = self.create_score_negative_prefix(score_slider)

            for i, prompt in enumerate(p.all_prompts):
                p.all_prompts[i] = score_positive_prefix + prompt
                print(f"Modified prompt: {p.all_prompts[i]}")

            for i, negative_prompt in enumerate(p.all_negative_prompts):
                p.all_negative_prompts[i] = score_negative_prefix + negative_prompt
                print(f"Modified negative prompt: {p.all_negative_prompts[i]}")

    def create_score_prefix(self, score):
        score_prefix = "score_9, "
        for i in range(8, score - 1, -1):
            score_prefix += f"score_{i}_up, "
        return score_prefix

    def create_score_negative_prefix(self, score):
        score_negative_prefix = ""
        for i in range(score - 1, 0, -1):
            score_negative_prefix += f"score_{i}, "
        return score_negative_prefix

    def after_component(self, component, **kwargs):
        if kwargs.get("elem_id") == "txt2img_prompt":
            self.boxx = component
        if kwargs.get("elem_id") == "img2img_prompt":
            self.boxxIMG = component
        if kwargs.get("elem_id") == "txt2img_neg_prompt":
            self.neg_boxx = component
        if kwargs.get("elem_id") == "img2img_neg_prompt":
            self.neg_boxxIMG = component
