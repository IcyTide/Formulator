import json
import os

from assets.constant import POSITION_MAP, STONES_POSITIONS, EQUIPMENTS_DIR, ENCHANTS_DIR, STONES_DIR, MAX_STONE_ATTR, \
    ATTR_TYPE_TRANSLATE
from assets.constant import EMBED_POSITIONS, MAX_EMBED_LEVEL, MAX_STONE_LEVEL, SPECIAL_ENCHANT_POSITIONS
import gradio as gr


class EquipmentComponent:
    def __init__(self, label):
        self.position = POSITION_MAP[label]
        self.equipment_json = json.load(open(os.path.join(EQUIPMENTS_DIR, self.position), encoding="utf-8"))
        self.equipment_mapping = {v['id']: k for k, v in self.equipment_json.items()}
        self.enchant_json = json.load(open(os.path.join(ENCHANTS_DIR, self.position), encoding="utf-8"))
        self.enchant_mapping = {v['id']: k for k, v in self.enchant_json.items()}

        self.equipment = gr.Dropdown(label="装备")
        with gr.Row():
            with gr.Column(scale=3) as self.detail:
                with gr.Row():
                    if not self.enchant_json:
                        self.enchant = gr.Dropdown(visible=False)
                    else:
                        self.enchant = gr.Dropdown(choices=[""] + list(self.enchant_json), label="附魔")

                    if self.position not in SPECIAL_ENCHANT_POSITIONS:
                        self.special_enchant = gr.Checkbox(visible=False)
                    else:
                        self.special_enchant = gr.Checkbox(label="大附魔")

                with gr.Row():
                    self.strength_level = gr.Dropdown(label="精炼等级")

                    self.embed_levels = []
                    for i in range(EMBED_POSITIONS[self.position]):
                        embed_level = gr.Dropdown(
                            choices=list(range(MAX_EMBED_LEVEL + 1)), value=MAX_EMBED_LEVEL, visible=False
                        )
                        self.embed_levels.append(embed_level)

                with gr.Row():
                    if self.position not in STONES_POSITIONS:
                        self.stones_json = None
                        self.stone_level = gr.Dropdown(visible=False)
                        self.stone_attrs = [gr.Dropdown(visible=False)] * MAX_STONE_ATTR
                    else:
                        self.stones_json = json.load(open(STONES_DIR, encoding="utf-8"))

                        self.stone_level = gr.Dropdown(
                            choices=list(range(MAX_STONE_LEVEL + 1)), value=MAX_STONE_LEVEL, label="五彩石等级"
                        )
                        self.stone_attrs = []
                        for i in range(MAX_STONE_ATTR):
                            if i:
                                stone_attr = gr.Dropdown(label=f"五彩石属性-{i + 1}")
                            else:
                                stone_attr = gr.Dropdown(choices=list(self.stones_json), label=f"五彩石属性-{i + 1}")
                            self.stone_attrs.append(stone_attr)

            self.base_attr = gr.Textbox(label="基本属性", visible=False, scale=1, lines=5)
            self.magic_attr = gr.Textbox(label="精炼属性", visible=False, scale=1, lines=5)
            self.embed_attr = gr.Textbox(label="镶嵌属性", visible=False, scale=1, lines=5)


class EquipmentsComponent:
    def __init__(self):
        super().__init__()
        self.equipments = {}
        for label in POSITION_MAP:
            with gr.Tab(label):
                self.equipments[label] = EquipmentComponent(label)

    def __getitem__(self, item) -> EquipmentComponent:
        return self.equipments[item]

    def items(self):
        return self.equipments.items()

    def values(self):
        return self.equipments.values()
