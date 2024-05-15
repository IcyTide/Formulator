import gradio as gr

from base.constant import SHIELD_BASE_MAP


class CombatComponent:
    def __init__(self):
        with gr.Row():
            self.combat_duration = gr.Slider(label="战斗时长", step=0.01)
            target_levels = list(SHIELD_BASE_MAP)
            self.target_level = gr.Dropdown(choices=target_levels, value=target_levels[0], label="目标等级")
        self.formulate = gr.Button("开始模拟")

        with gr.Tab("属性"):
            with gr.Row():
                self.init_attribute = gr.Textbox(label="初始属性")
                self.final_attribute = gr.Textbox(label="增益后属性")
        with gr.Tab("伤害总结"):
            self.details = gr.State({})
            self.skill_select = gr.Dropdown(label="选择技能")
            self.status_select = gr.Dropdown(label="选择增益")
            with gr.Row():
                self.damage_detail = gr.Textbox(label="伤害细节")
                self.damage_gradient = gr.Textbox(label="属性收益")
        with gr.Tab("战斗统计"):
            with gr.Row():
                self.summary = gr.DataFrame(label="战斗总结", headers=["技能/次数", "命中/%", "会心/%", "伤害/%"], scale=3)
                with gr.Column(scale=1):
                    self.dps = gr.Textbox(label="每秒伤害")
                    self.gradient = gr.Textbox(label="属性收益", lines=10)



