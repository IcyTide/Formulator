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
            content.append(name.ljust(10, FULL_SPACE) + str(value))
        else:
            content.append(name.ljust(10, FULL_SPACE) + f"{round(value * 100, 2)}%")
    return "\n".join(content)


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
    damage_detail = "\n".join([
        "命中伤害".ljust(10) + f"{round(detail.damage)}",
        "会心伤害".ljust(10) + f"{round(detail.critical_damage)}",
        "期望伤害".ljust(10) + f"{round(detail.expected_damage)}",
        "期望会心".ljust(10) + f"{round(detail.critical_strike * 100, 2)}%",
        "实际会心".ljust(10) + f"{round(detail.actual_critical_strike * 100, 2)}%",
        "统计数量".ljust(10) + f"{detail.count}"
    ])

    damage_gradient = gradient_content(detail.gradients, detail.expected_damage)

    return damage_detail, damage_gradient


def combat_script(
        parser: Parser,
        talents: Talents, recipes: Recipes, equipments: Equipments,
        # consumables: Consumables, bonuses: Bonuses
        combat_component: CombatComponent,
):
    def formulate(target_level, duration, skill, status):
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

        combat_update[combat_component.details] = details
        combat_update[combat_component.skill_select] = gr.update(choices=list(details))
        if skill_detail := details.get(skill, {}):
            combat_update[combat_component.status_select] = gr.update(choices=[""] + list(skill_detail))
        if detail := skill_detail.get(status):
            damage_detail, damage_gradient = detail_content(detail)
            combat_update[combat_component.damage_detail] = gr.update(value=damage_detail)
            combat_update[combat_component.damage_gradient] = gr.update(value=damage_gradient)
        else:
            combat_update[combat_component.damage_detail] = gr.update(value="")
            combat_update[combat_component.damage_gradient] = gr.update(value="")

        combat_update[combat_component.summary] = summary_content(summary, total.expected_damage)
        return combat_update

    combat_component.formulate.click(
        formulate,
        [combat_component.target_level, combat_component.combat_duration,
         combat_component.skill_select, combat_component.status_select],
        [combat_component.init_attribute, combat_component.final_attribute,
         combat_component.dps, combat_component.gradient, combat_component.summary,
         combat_component.details, combat_component.skill_select, combat_component.status_select,
         combat_component.damage_detail, combat_component.damage_gradient
         ]
    )

    def skill_changed(skill, details):
        if skill not in details:
            return None
        return gr.update(choices=[""] + list(details[skill]))

    combat_component.skill_select.change(
        skill_changed, [combat_component.skill_select, combat_component.details], combat_component.status_select
    )

    def status_changed(skill, status, details):
        if skill not in details:
            return None, None
        if status not in details[skill]:
            return None, None
        damage_detail, damage_gradient = detail_content(details[skill][status])
        return gr.update(value=damage_detail), gr.update(value=damage_gradient)

    combat_component.status_select.change(
        status_changed, [combat_component.skill_select, combat_component.status_select, combat_component.details],
        [combat_component.damage_detail, combat_component.damage_gradient]
    )
