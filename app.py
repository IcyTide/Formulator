from gr.components.top import TopComponent
from gr.components.equipments import EquipmentsComponent
from gr.components.talents import TalentsComponent
from gr.components.recipes import RecipesComponent
from gr.components.combat import CombatComponent

from gr.scripts.top import top_script
from gr.scripts.equipments import equipments_script
from gr.scripts.talents import talents_script
from gr.scripts.recipes import recipes_script
from gr.scripts.combat import combat_script

import gradio as gr


def start():
    with gr.Blocks(theme=gr.themes.Soft()) as app:
        top_component = TopComponent()
        with gr.Group(visible=False) as bottom_component:
            with gr.Tab("装备"):
                equipments_component = EquipmentsComponent()
            with gr.Tab("奇穴"):
                talents_component = TalentsComponent()
            with gr.Tab("秘籍"):
                recipes_component = RecipesComponent()
            with gr.Tab("战斗"):
                combat_component = CombatComponent()

        parser = top_script(top_component, bottom_component,
                            equipments_component, talents_component, recipes_component,
                            combat_component)
        equipments = equipments_script(equipments_component)
        talents = talents_script(talents_component)
        recipes = recipes_script(recipes_component)
        combat_script(parser, talents, recipes, equipments, combat_component)

    app.queue()
    app.launch(allowed_paths=["."])


if __name__ == '__main__':
    start()
