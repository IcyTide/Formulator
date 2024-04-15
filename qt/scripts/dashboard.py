from PySide6.QtWidgets import QMessageBox

from qt.components.dashboard import DashboardWidget
from qt.constant import ATTR_TYPE_TRANSLATE
from qt.scripts.consumables import Consumables
from qt.scripts.top import Parser
from qt.scripts.equipments import Equipments
# from qt.scripts.consumables import Consumables
# from qt.scripts.bonuses import Bonuses
from qt.scripts.recipes import Recipes
from qt.scripts.talents import Talents
from utils.analyzer import analyze_details


def summary_content(summary, total_damage):
    content = []
    for skill in sorted(summary, key=lambda x: summary[x]['damage'], reverse=True):
        detail = summary[skill]
        critical = round(detail['critical'], 2)
        critical_rate = round(detail['critical'] / detail['count'] * 100, 2)
        hit = round(detail['count'] - critical, 2)
        hit_rate = round(100 - critical_rate, 2)
        damage = round(detail['damage'], 2)
        damage_rate = round(damage / total_damage * 100, 2)
        content.append(
            [f"{skill}/{detail['count']}",
             f"{hit}/{hit_rate}%", f"{critical}/{critical_rate}%", f"{damage}/{damage_rate}%"]
        )
    return content


def detail_content(detail):
    damage_content = [
        ["命中伤害", f"{detail['damage']}"],
        ["会心伤害", f"{detail['critical_damage']}"],
        ["期望伤害", f"{round(detail['expected_damage'], 2)}"],
        ["会心", f"{round(detail['critical_strike'] * 100, 2)}%"],
        ["期望会心", f"{round(detail['expected_critical_strike'] * 100, 2)}%"],
    ]
    gradient_content = [
        [ATTR_TYPE_TRANSLATE[k], f"{round(v / detail['expected_damage'] * 100, 2)}%"]
        for k, v in detail['gradients'].items()
    ]

    return damage_content, gradient_content


def dashboard_script(parser: Parser,
                     dashboard_widget: DashboardWidget, talents: Talents, recipes: Recipes,
                     equipments: Equipments, consumables: Consumables):

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
        gains = sum([equipment_gains, talent_gains, recipe_gains], [])

        for gain in gains:
            attribute += gain
            school.skills += gain

        dashboard_widget.final_attribute.set_content(school.attr_content(attribute))

        total_damage, total_gradient, details, summary = analyze_details(record, duration, attribute, school)
        for gain in gains:
            attribute -= gain
            school.skills -= gain

        dashboard_widget.dps.set_text(str(round(total_damage / duration)))

        dashboard_widget.gradients.set_content(
            [[ATTR_TYPE_TRANSLATE[k], f"{round(v, 2)}%"] for k, v in total_gradient.items()]
        )

        dashboard_widget.detail_widget.details = details
        set_skills()

        dashboard_widget.summary.set_content(summary_content(summary, total_damage))

    dashboard_widget.button.clicked.connect(formulate)

    def set_skills():
        set_detail(None)
        detail_widget = dashboard_widget.detail_widget
        skill = detail_widget.skill_combo.combo_box.currentText()
        skill_choices = list(detail_widget.details)
        if skill in skill_choices:
            default_index = skill_choices.index(skill)
        else:
            default_index = -1
        detail_widget.skill_combo.set_items(skill_choices, default_index=default_index)

    def set_status(_):
        set_detail(None)
        detail_widget = dashboard_widget.detail_widget
        skill = detail_widget.skill_combo.combo_box.currentText()
        status = detail_widget.status_combo.combo_box.currentText()
        status_choices = list(detail_widget.details.get(skill, {}))
        if status in status_choices:
            default_index = status_choices.index(status)
        else:
            default_index = -1
        detail_widget.status_combo.set_items(status_choices, default_index=default_index)

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
