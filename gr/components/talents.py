from typing import List

import gradio as gr

from assets.constant import MAX_TALENTS


class TalentsComponent:
    def __init__(self):
        self.talents = []

        rows = 2
        columns = MAX_TALENTS // rows

        for i in range(rows):
            with gr.Row():
                for j in range(columns):
                    talent = gr.Dropdown(label=f"奇穴第{i * columns + j + 1}层")
                    self.talents.append(talent)

    def __getitem__(self, item) -> gr.Dropdown:
        return self.talents[item]

    def values(self) -> List[gr.Dropdown]:
        return self.talents
