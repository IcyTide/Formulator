from typing import Dict

from qt.components.dashboard import DashboardWidget
from qt.constant import ATTR_TYPE_TRANSLATE
from qt.scripts.bonuses import Bonuses
from qt.scripts.consumables import Consumables
from qt.scripts.top import Parser
from qt.scripts.equipments import Equipments
from qt.scripts.recipes import Recipes
from qt.scripts.talents import Talents
from utils.analyzer import analyze_details, Detail


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


def detail_content(detail: Detail):
    damage_content = [
        ["命中伤害", f"{round(detail.damage)}"],
        ["会心伤害", f"{round(detail.critical_damage)}"],
        ["期望伤害", f"{round(detail.expected_damage)}"],
        ["会心", f"{round(detail.critical_strike * 100, 2)}%"],
        ["实际会心", f"{round(detail.actual_critical_strike * 100, 2)}%"],
        ["数量", f"{detail.count}"]
    ]
    gradient_content = [
        [ATTR_TYPE_TRANSLATE[k], f"{round(v / detail.expected_damage * 100, 2)}%"]
        for k, v in detail.gradients.items()
    ]

    return damage_content, gradient_content


def dashboard_script(parser: Parser,
                     dashboard_widget: DashboardWidget, talents: Talents, recipes: Recipes,
                     equipments: Equipments, consumables: Consumables, bonuses: Bonuses):

    def select_fight(text):
        index = parser.record_index[text]
        dashboard_widget.duration.set_value(parser.duration(index))

    dashboard_widget.fight_select.combo_box.currentTextChanged.connect(select_fight)

    def formulate():
        duration = dashboard_widget.duration.spin_box.value()
        record = parser.records[parser.record_index[dashboard_widget.fight_select.combo_box.currentText()]]

        school = parser.school
        attribute = school.attribute()
        attribute.target_level = int(dashboard_widget.target_level.combo_box.currentText())
        for attr, value in equipments.attrs.items():
            setattr(attribute, attr, getattr(attribute, attr) + value)

        dashboard_widget.init_attribute.set_content(school.attr_content(attribute))
        for attr, value in consumables.attrs.items():
            setattr(attribute, attr, getattr(attribute, attr) + value)

        equipment_gains = [school.gains[gain] for gain in equipments.gains]
        talent_gains = [school.talent_gains[school.talent_encoder[talent]] for talent in talents.gains]
        recipe_gains = [school.recipe_gains[skill][recipe] for skill, recipe in recipes.gains]
        gains = sum([equipment_gains, talent_gains, recipe_gains, bonuses.gains], [])

        for gain in gains:
            gain.add(attribute, school.skills, school.buffs)

        dashboard_widget.final_attribute.set_content(school.attr_content(attribute))
        total, summary, details = analyze_details(record, duration, attribute, school)

        for gain in gains:
            gain.sub(attribute, school.skills, school.buffs)

        dashboard_widget.dps.set_text(str(round(total.expected_damage / duration)))

        dashboard_widget.gradients.set_content(
            [[ATTR_TYPE_TRANSLATE[k], f"{round(v / total.expected_damage * 100, 2)}%"]
             for k, v in total.gradients.items()]
        )

        dashboard_widget.detail_widget.details = details
        set_skills()

        dashboard_widget.summary.set_content(summary_content(summary, total.expected_damage))

    dashboard_widget.button.clicked.connect(formulate)

    def set_skills():
        detail_widget = dashboard_widget.detail_widget
        skill = detail_widget.skill_combo.combo_box.currentText()
        skill_choices = list(detail_widget.details)
        if skill in skill_choices:
            default_index = skill_choices.index(skill)
        else:
            default_index = -1
        detail_widget.skill_combo.set_items(skill_choices, default_index=default_index)
        set_status(None)

    def set_status(_):
        detail_widget = dashboard_widget.detail_widget
        skill = detail_widget.skill_combo.combo_box.currentText()
        status = detail_widget.status_combo.combo_box.currentText()
        status_choices = list(detail_widget.details.get(skill, {}))
        if status in status_choices:
            default_index = status_choices.index(status)
        else:
            default_index = -1
        detail_widget.status_combo.set_items(status_choices, default_index=default_index)
        set_detail(None)

    dashboard_widget.detail_widget.skill_combo.combo_box.currentTextChanged.connect(set_status)

    def set_detail(_):
        detail_widget = dashboard_widget.detail_widget
        skill = detail_widget.skill_combo.combo_box.currentText()
        status = detail_widget.status_combo.combo_box.currentText()
        if detail := detail_widget.details.get(skill, {}).get(status):
            damage_content, gradient_content = detail_content(detail)
            detail_widget.damage_detail.set_content(damage_content)
            detail_widget.gradient_detail.set_content(gradient_content)
        else:
            detail_widget.damage_detail.table.clear()
            detail_widget.gradient_detail.table.clear()

    dashboard_widget.detail_widget.status_combo.combo_box.currentTextChanged.connect(set_detail)
