from typing import Dict

from gr.components.combat import CombatComponent
from assets.constant import ATTR_TYPE_TRANSLATE
# from gr.scripts.bonuses import Bonuses
# from gr.scripts.consumables import Consumables
from gr.scripts.top import Parser
from gr.scripts.equipments import Equipments
from gr.scripts.recipes import Recipes
from gr.scripts.talents import Talents
from utils.analyzer import analyze_details, Detail

import gradio as gr

FULL_SPACE = "\u3000"


def attribute_content(display_attrs, attribute):
    content = []
    for attr, name in display_attrs.items():
        value = getattr(attribute, attr)
        if isinstance(value, int):
            content.append([name, f"{value}"])
        else:
            content.append([name, f"{round(value * 100, 2)}%"])
    return content


def summary_content(summary: Dict[str, Detail], total_damage):
    content = []
    for skill in sorted(summary, key=lambda x: summary[x].expected_damage, reverse=True):
        detail = summary[skill]
        critical = round(detail.critical_count, 2)
        critical_rate = round(detail.critical_count / detail.count * 100, 2)
        hit = round(detail.count - critical, 2)
        hit_rate = round(100 - critical_rate, 2)
        damage = round(detail.expected_damage, 2)
        damage_rate = round(damage / total_damage * 100, 2)
        content.append(
            [f"{skill}/{detail.count}",
             f"{hit}/{hit_rate}%", f"{critical}/{critical_rate}%", f"{damage}/{damage_rate}%"]
        )
    return content


def gradient_content(gradients, total_damage):
    return "\n".join(
        ATTR_TYPE_TRANSLATE[k].ljust(10, FULL_SPACE) + f"{round(v / total_damage * 100, 2)}%"
        for k, v in gradients.items()
    )


def detail_content(detail: Detail):
    damage_content = "\n".join([
        "命中伤害\t" + f"{round(detail.damage)}",
        "会心伤害\t" + f"{round(detail.critical_damage)}",
        "期望伤害\t" + f"{round(detail.expected_damage)}",
        "期望会心\t" + f"{round(detail.critical_strike * 100, 2)}%",
        "实际会心\t" + f"{round(detail.actual_critical_strike * 100, 2)}%",
        "统计数量\t" + f"{detail.count}"
    ])

    return damage_content, gradient_content(detail.gradients, detail.expected_damage)


def combat_script(
        parser: Parser,
        talents: Talents, recipes: Recipes, equipments: Equipments,
        # consumables: Consumables, bonuses: Bonuses
        combat_component: CombatComponent,
):
    def formulate(target_level, duration):
        combat_update = {}
        record = parser.current_records
        school = parser.current_school

        attribute = school.attribute()
        attribute.target_level = target_level
        for attr, value in equipments.attrs.items():
            setattr(attribute, attr, getattr(attribute, attr) + value)
        combat_update[combat_component.init_attribute] = gr.update(
            value=attribute_content(school.display_attrs, attribute)
        )
        # for attr, value in consumables.attrs.items():
        #     setattr(attribute, attr, getattr(attribute, attr) + value)

        equipment_gains = [school.gains[gain] for gain in equipments.gains]
        talent_gains = [school.talent_gains[school.talent_encoder[talent]] for talent in talents.gains]
        recipe_gains = [
            school.recipe_gains[skill][recipe]
            for i, skill in enumerate(school.recipe_gains)
            for recipe in recipes.gains[i]
        ]
        gains = equipment_gains + talent_gains + recipe_gains  # + bonuses.gains

        for gain in gains:
            gain.add(attribute, school.skills, school.buffs)

        combat_update[combat_component.final_attribute] = gr.update(
            value=attribute_content(school.display_attrs, attribute)
        )
        total, summary, details = analyze_details(record, duration, attribute, school)

        for gain in gains:
            gain.sub(attribute, school.skills, school.buffs)

        combat_update[combat_component.dps] = gr.update(value=round(total.expected_damage / duration))

        combat_update[combat_component.gradient] = gradient_content(total.gradients, total.expected_damage)
        #
        # dashboard_widget.detail_widget.details = details
        # set_skills()

        combat_update[combat_component.summary] = summary_content(summary, total.expected_damage)
        return combat_update

    combat_component.formulate.click(
        formulate,
        [combat_component.target_level, combat_component.combat_duration],
        [combat_component.init_attribute, combat_component.final_attribute,
         combat_component.dps, combat_component.gradient, combat_component.summary]
    )

    # def set_skills():
    #     detail_widget = dashboard_widget.detail_widget
    #     detail_widget.skill_combo.set_items(list(detail_widget.details), keep_index=True, default_index=-1)
    #     set_status(None)
    #
    # def set_status(_):
    #     detail_widget = dashboard_widget.detail_widget
    #     skill = detail_widget.skill_combo.combo_box.currentText()
    #     detail_widget.status_combo.set_items(
    #         list(detail_widget.details.get(skill, {})), keep_index=True, default_index=-1
    #     )
    #     set_detail(None)
    #
    # dashboard_widget.detail_widget.skill_combo.combo_box.currentTextChanged.connect(set_status)
    #
    # def set_detail(_):
    #     detail_widget = dashboard_widget.detail_widget
    #     skill = detail_widget.skill_combo.combo_box.currentText()
    #     status = detail_widget.status_combo.combo_box.currentText()
    #     if detail := detail_widget.details.get(skill, {}).get(status):
    #         damage_content, gradient_content = detail_content(detail)
    #         detail_widget.damage_detail.set_content(damage_content)
    #         detail_widget.gradient_detail.set_content(gradient_content)
    #     else:
    #         detail_widget.damage_detail.table.clear()
    #         detail_widget.gradient_detail.table.clear()
    #
    # dashboard_widget.detail_widget.status_combo.combo_box.currentTextChanged.connect(set_detail)
