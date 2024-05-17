import pandas as pd

from gr.components.combat import CombatComponent
from assets.constant import ATTR_TYPE_TRANSLATE
# from gr.scripts.bonuses import Bonuses
# from gr.scripts.consumables import Consumables
from gr.scripts.top import Parser
from gr.scripts.equipments import Equipments
from gr.scripts.recipes import Recipes
from gr.scripts.talents import Talents
from utils.analyzer import analyze_records

import gradio as gr

FULL_SPACE = "\u3000"
BUFF_CONCAT = ":"


class Detail:
    records: pd.DataFrame = pd.DataFrame()

    skill: str = ""
    status_set: list = []

    @property
    def current_records(self):
        records = self.records
        if self.skill:
            records = records[records.skill == self.skill]
        if self.status_set:
            for buff in self.status_set:
                column, stack = buff.split(BUFF_CONCAT)
                records = records[records[column] == int(stack)]
        return records

    @property
    def available_status(self):
        status_set = []
        records = self.current_records
        for column in records.columns:
            if "#" not in column:
                continue
            for stack in records[column].unique():
                if not stack:
                    continue
                status_set.append(f"{column}{BUFF_CONCAT}{stack:.0f}")
        return status_set


def attribute_content(display_attrs, attribute):
    content = []
    for attr, name in display_attrs.items():
        value = getattr(attribute, attr)
        if isinstance(value, int):
            content.append(name.ljust(10, FULL_SPACE) + str(value))
        else:
            content.append(name.ljust(10, FULL_SPACE) + f"{value * 100:.2f}%")
    return "\n".join(content)


def summary_content(records, total_damage):
    content = {}
    group_records = records.groupby("skill_name")
    sum_expected_damage = group_records.expected_damage.sum()
    mean_critical_strike = group_records.critical_strike.mean()
    for skill_name, count in group_records.skill_name.count().items():
        critical_strike = mean_critical_strike[skill_name]
        critical_count = critical_strike * count
        hit = 1 - critical_strike
        hit_count = count - critical_strike
        expected_damage = sum_expected_damage[skill_name]
        content[expected_damage] = (
            [f"{skill_name}/{count}",
             f"{hit_count:.2f}/{hit * 100:.2f}%", f"{critical_count:.2f}/{critical_strike * 100:.2f}%",
             f"{expected_damage:.2f}/{expected_damage / total_damage:.2f}%"]
        )
    content = [content[k] for k in sorted(content, reverse=True)]
    return content


def gradient_content(records, attribute, total_damage):
    content = []
    for attr in attribute.grad_attrs:
        gradient = records[attr].sum() / total_damage - 1
        content.append(ATTR_TYPE_TRANSLATE[attr].ljust(10, FULL_SPACE) + f"{gradient * 100:.2f}")
    return "\n".join(content)


def detail_content(records):
    damage_detail = "\n".join([
        "统计数量".ljust(10) + f"{len(records)}",
        "命中伤害".ljust(10) + f"{records.damage.mean():.0f}",
        "会心伤害".ljust(10) + f"{records.critical_damage.mean():.0f}",
        "期望伤害".ljust(10) + f"{records.expected_damage.mean():.0f}",
        "实际伤害".ljust(10) + f"{records.actual_damage.mean():.0f}",
        "期望会心".ljust(10) + f"{records.critical_strike.mean() * 100:.2f}%",
        "实际会心".ljust(10) + f"{records.actual_critical_strike.mean() * 100:.2f}%"
    ])

    # damage_gradient = gradient_content(records, attribute, records.expected_damage.sum())

    return damage_detail


def timeline_content(records):
    columns = [column for column in records.columns if "#" in column]
    return records[["time", "skill"] + columns].rename(columns={"time": "时间", "skill": "技能"})


def combat_script(
        parser: Parser,
        talents: Talents, recipes: Recipes, equipments: Equipments,
        # consumables: Consumables, bonuses: Bonuses
        combat_component: CombatComponent,
):
    detail = Detail()

    def formulate(target_level, duration):
        combat_update = {}
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
        records = analyze_records(parser, duration, attribute)

        for gain in gains:
            gain.sub(attribute, school.skills, school.buffs)

        total_damage = records.expected_damage.sum()
        combat_update[combat_component.dps] = gr.update(value=f"{total_damage / duration:.0f}")

        combat_update[combat_component.gradient] = gradient_content(records, attribute, total_damage)

        combat_update[combat_component.summary] = summary_content(records, total_damage)

        detail.records = records

        combat_update[combat_component.skill_select] = gr.update(choices=list(records.skill.unique()))
        if detail.current_records.empty:
            detail.status_set = []
        records = detail.current_records

        combat_update[combat_component.status_select] = gr.update(choices=detail.available_status)
        combat_update[combat_component.damage_detail] = gr.update(value=detail_content(records), visible=True)
        combat_update[combat_component.damage_timeline] = gr.update(value=timeline_content(records), visible=True)

        return combat_update

    combat_component.formulate.click(
        formulate,
        [combat_component.target_level, combat_component.combat_duration],
        [combat_component.init_attribute, combat_component.final_attribute,
         combat_component.dps, combat_component.gradient, combat_component.summary,
         combat_component.skill_select, combat_component.status_select,
         combat_component.damage_detail, combat_component.damage_timeline]
    )

    def skill_changed(skill):
        detail.skill = skill

        if detail.current_records.empty:
            detail.status_set = []

        records = detail.current_records
        return gr.update(choices=detail.available_status), detail_content(records), timeline_content(records)

    combat_component.skill_select.change(
        skill_changed, combat_component.skill_select,
        [combat_component.status_select, combat_component.damage_detail, combat_component.damage_timeline]
    )

    def status_changed(status_set):
        detail.status_set = status_set
        records = detail.current_records

        if records.empty:
            return gr.update(visible=False), gr.update(visible=False)
        return (gr.update(value=detail_content(records), visible=True),
                gr.update(value=timeline_content(records), visible=True))

    combat_component.status_select.change(
        status_changed, combat_component.status_select,
        [combat_component.damage_detail, combat_component.damage_timeline]
    )
