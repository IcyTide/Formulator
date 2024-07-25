from typing import Dict

from assets.constant import ATTR_TYPE_TRANSLATE, MOBILE_MAX_TALENTS
from base.constant import FRAME_PER_SECOND
from qt.components.dashboard import DashboardWidget
from qt.scripts.bonuses import Bonuses
from qt.scripts.consumables import Consumables
from qt.scripts.equipments import Equipments
from qt.scripts.recipes import Recipes
from qt.scripts.talents import Talents
from qt.scripts.top import Parser
from schools.wen_shui_jue.gains import SecondaryWeapon
from utils.analyzer import analyze_details, Detail


def attr_content(attribute):
    content = []
    for attr in attribute.display_attrs:
        value = getattr(attribute, attr)
        name = ATTR_TYPE_TRANSLATE[attr]
        if isinstance(value, int):
            content.append([name, f"{value}"])
        else:
            content.append([name, f"{round(value * 100, 2)}%"])
    return content


def summary_content(summary: Dict[str, Detail], total_damage):
    content = []
    for skill in sorted(summary, key=lambda x: summary[x].expected_damage, reverse=True):
        detail = summary[skill]
        critical_count = round(detail.critical_strike, 2)
        critical_rate = round(critical_count / detail.count * 100, 2)
        hit_count = round(detail.count - critical_count, 2)
        hit_rate = round(100 - critical_rate, 2)
        damage = round(detail.expected_damage, 2)
        damage_rate = round(damage / total_damage * 100, 2)
        content.append(
            [f"{skill}/{detail.count}",
             f"{hit_count}/{hit_rate}%", f"{critical_count}/{critical_rate}%", f"{damage}/{damage_rate}%"]
        )
    return content


def detail_content(detail: Detail):
    damage_content = [
        ["命中伤害", f"{round(detail.damage)}"],
        ["会心伤害", f"{round(detail.critical_damage)}"],
        ["期望会心", f"{round(detail.critical_strike * 100, 2)}%"],
        ["实际会心", f"{round(detail.actual_critical_strike * 100, 2)}%"],
        ["期望平均伤害", f"{round(detail.expected_damage)}"],
        ["实际平均伤害", f"{round(detail.actual_damage)}"],
        ["期望总伤害", f"{round(detail.expected_damage * detail.count)}"],
        ["实际总伤害", f"{round(detail.total_actual_damage)}"],
        ["数量", f"{detail.count}"]
    ]
    timeline_content = [
        [str(round(t[0] / FRAME_PER_SECOND, 2)), "会心" if t[1] else "命中", str(t[2])] for t in sorted(detail.timeline)
    ]

    return damage_content, timeline_content


def dashboard_script(parser: Parser,
                     dashboard_widget: DashboardWidget, talents: Talents, recipes: Recipes,
                     equipments: Equipments, consumables: Consumables, bonuses: Bonuses):
    def formulate():
        target_name = dashboard_widget.target_select.combo_box.currentText()
        if target_name:
            target_id = parser.name2id.get(target_name, "")
        else:
            target_id = target_name
        parser.current_target = target_id
        record = parser.current_records
        school = parser.current_school

        attribute = school.attribute(school.platform)
        attribute.target.level = int(dashboard_widget.target_level.combo_box.currentText())
        for attr, value in equipments.attrs.items():
            setattr(attribute, attr, getattr(attribute, attr) + value)

        dashboard_widget.init_attribute.set_content(attr_content(attribute))
        for attr, value in consumables.attrs.items():
            setattr(attribute, attr, getattr(attribute, attr) + value)

        equipment_gains = [school.gains[gain] for gain in equipments.gains]
        if not school.platform:
            talent_gains = [school.talent_gains[school.talent_encoder[talent]] for talent in talents.gains]
            recipe_gains = [school.recipe_gains[skill][recipe] for skill, recipe in recipes.gains]
        else:
            talent_gains = [school.talent_gains[school.talent_encoder[talent]]
                            for talent in talents.gains[:MOBILE_MAX_TALENTS]]
            recipe_gains = []
        gains = sum([equipment_gains, talent_gains, recipe_gains, bonuses.gains], [])
        if school.id == 10145:
            gains.append(SecondaryWeapon(equipments.secondary_weapon_attrs))

        for gain in gains:
            gain.add(attribute, school.skills, school.dots, school.buffs)

        start_time = dashboard_widget.start_time.spin_box.value()
        end_time = dashboard_widget.end_time.spin_box.value()
        dashboard_widget.final_attribute.set_content(attr_content(attribute))
        total, summary, details = analyze_details(record, start_time, end_time, attribute, school)

        for gain in gains:
            gain.sub(attribute, school.skills, school.dots, school.buffs)

        dashboard_widget.dps.set_text(str(round(total.expected_damage / (end_time - start_time))))

        dashboard_widget.gradients.set_content(
            [[ATTR_TYPE_TRANSLATE[k], f"{round(v / total.expected_damage * 100, 2)}%"]
             for k, v in total.gradients.items()]
        )

        dashboard_widget.detail_widget.details = details
        set_skills()

        dashboard_widget.summary.set_content(summary_content(summary, total.expected_damage))

    dashboard_widget.formulate_button.clicked.connect(formulate)

    def set_skills():
        detail_widget = dashboard_widget.detail_widget
        detail_widget.skill_combo.set_items(list(detail_widget.details), keep_index=True, default_index=-1)
        set_status(None)

    def set_status(_):
        detail_widget = dashboard_widget.detail_widget
        skill = detail_widget.skill_combo.combo_box.currentText()
        detail_widget.status_combo.set_items(
            list(detail_widget.details.get(skill, {})), keep_index=True, default_index=-1
        )
        set_detail(None)

    dashboard_widget.detail_widget.skill_combo.combo_box.currentTextChanged.connect(set_status)

    def set_detail(_):
        detail_widget = dashboard_widget.detail_widget
        skill = detail_widget.skill_combo.combo_box.currentText()
        status = detail_widget.status_combo.combo_box.currentText()
        if detail := detail_widget.details.get(skill, {}).get(status):
            damage_content, timeline_content = detail_content(detail)
            detail_widget.damage_detail.set_content(damage_content)
            detail_widget.timeline.set_content(timeline_content)
        else:
            detail_widget.damage_detail.table.clear()
            detail_widget.timeline.clear_content()

    dashboard_widget.detail_widget.status_combo.combo_box.currentTextChanged.connect(set_detail)
