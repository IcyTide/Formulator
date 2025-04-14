import json
from typing import Dict

from assets.constant import ATTR_TYPE_TRANSLATE
from base.constant import FRAME_PER_SECOND
from qt.components.dashboard import DashboardWidget
from qt.scripts.bonuses import Bonuses
from qt.scripts.consumables import Consumables
from qt.scripts.equipments import Equipments
from qt.scripts.recipes import Recipes
from qt.scripts.talents import Talents
from qt.scripts.top import Parser
from utils.analyzer import Analyzer, Detail


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


def summary_content(analyzer: Analyzer):
    content = []
    total_damage = analyzer.total.expected_damage
    for skill, detail in analyzer.summary.items():
        critical_rate = round(detail.critical_strike * 100, 2)
        critical_count = round(detail.expected_critical_count, 2)
        hit_rate = round(100 - critical_rate, 2)
        hit_count = round(detail.actual_count - critical_count, 2)
        damage = round(detail.expected_damage, 2)
        damage_rate = round(damage / total_damage * 100, 2)
        content.append(
            [f"{skill}/{round(detail.expected_count, 2)}",
             f"{hit_count}/{hit_rate}%", f"{critical_count}/{critical_rate}%", f"{damage}/{damage_rate}%"]
        )
    return content


def total_content(analyzer: Analyzer):
    gradients = []
    for k, v in analyzer.total.gradients.items():
        gradients.append([ATTR_TYPE_TRANSLATE[k], f"{round((v / analyzer.total.expected_damage - 1) * 100, 2)}%"])

    dps = str(round(analyzer.total.expected_damage / (analyzer.end_time - analyzer.start_time)))
    return dps, gradients


def anomaly_detect(analyzer: Analyzer):
    anomaly_details = {}
    for skill, skill_detail in analyzer.details.items():
        anomaly_details[skill] = {}
        for status, detail in skill_detail.items():
            if not status:
                continue
            if anomaly_detail := detail.anomaly_detail:
                anomaly_details[skill][status] = anomaly_detail
        if not anomaly_details[skill]:
            anomaly_details.pop(skill)
    return anomaly_details


def detail_content(detail: Detail):
    damage_content = [
        ["命中伤害", f"{round(detail.hit_damage)}"],
        ["会心伤害", f"{round(detail.critical_damage)}"],
        ["期望/实际会心", f"{round(detail.critical_strike * 100, 2)}%/{round(detail.actual_critical_strike * 100, 2)}%"],
        ["期望/实际数量", f"{round(detail.expected_count, 2)}/{detail.actual_count}"],
        ["期望平均伤害", f"{round(detail.expected_damage)}"],
        ["实际平均伤害", f"{round(detail.actual_damage)}"],
        ["期望总伤害", f"{round(detail.total_expected_damage)}"],
        ["实际总伤害", f"{round(detail.total_actual_damage)}"],
    ]
    timeline_content = [
        [str(i + 1), str(round(t[0] / FRAME_PER_SECOND, 2)), "会心" if t[1] else "命中", str(t[2])]
        for i, t in enumerate(sorted(detail.timeline))
    ]

    return damage_content, timeline_content


def dashboard_script(parser: Parser,
                     dashboard_widget: DashboardWidget, talents: Talents, recipes: Recipes,
                     equipments: Equipments, consumables: Consumables, bonuses: Bonuses):
    def formulate():
        record = parser.current_records
        kungfu = parser.current_kungfu

        target_level = int(dashboard_widget.target_level.combo_box.currentText())
        start_time = dashboard_widget.start_time.spin_box.value()
        end_time = dashboard_widget.end_time.spin_box.value()
        analyzer = Analyzer(kungfu, target_level, start_time, end_time, record)
        equipment_attrs, equipment_gains, equipment_recipes = equipments.details
        analyzer.add_attrs(equipment_attrs)
        dashboard_widget.init_attribute.set_content(attr_content(analyzer.attribute))
        analyzer.add_gains(bonuses.gains)
        analyzer.add_attrs(consumables.attrs)
        if not_support_gains := analyzer.add_gains(equipment_gains):
            dashboard_widget.pop_warning(f"以下装备特效未支持：{';'.join(not_support_gains)}")
        if not_support_recipes := analyzer.add_recipes(equipment_recipes):
            dashboard_widget.pop_warning(f"以下装备秘籍未支持：{';'.join(not_support_recipes)}")

        analyzer.add_gains([kungfu.talent_encoder[t] for t in talents.gains])
        analyzer.add_recipes([kungfu.recipe_choices[s][r] for e in recipes.recipes for s, r in e])

        dashboard_widget.final_attribute.set_content(attr_content(analyzer.attribute))
        analyzer.analyze_details()
        analyzer.sub_gains()
        analyzer.sub_recipes()

        dps, gradients_content = total_content(analyzer)
        dashboard_widget.dps.set_text(dps)
        dashboard_widget.gradients.set_content(gradients_content)
        dashboard_widget.summary.set_content(summary_content(analyzer))

        dashboard_widget.detail_widget.details = analyzer.details
        set_skills()
        dashboard_widget.anomaly_widget.details = anomaly_detect(analyzer)
        set_anomaly_skills()

    dashboard_widget.formulate_button.clicked.connect(formulate)

    def export():
        player_name = parser.id2name[parser.current_player]
        file_name = parser.file_name.split(".jcl")[0] + f"-{player_name}.json"
        result = {
            damage: {
                status: vars(detail) for status, detail in details.items()
            }
            for damage, details in dashboard_widget.detail_widget.details.items()
        }
        json.dump(result, open(file_name, "w", encoding="utf-8"), ensure_ascii=False)

    dashboard_widget.export_button.clicked.connect(export)

    def set_skills():
        detail_widget = dashboard_widget.detail_widget
        detail_widget.skill_combo.set_items(list(detail_widget.details), keep_content=True, default_index=-1)
        set_status(None)

    def set_anomaly_skills():
        anomaly_widget = dashboard_widget.anomaly_widget
        anomaly_widget.skill_combo.set_items(list(anomaly_widget.details), keep_content=True, default_index=-1)
        set_anomaly_status(None)

    def set_status(_):
        detail_widget = dashboard_widget.detail_widget
        skill = detail_widget.skill_combo.combo_box.currentText()
        detail_widget.status_combo.set_items(
            list(detail_widget.details.get(skill, {})), keep_content=True, default_index=-1
        )
        set_detail(None)

    dashboard_widget.detail_widget.skill_combo.combo_box.currentTextChanged.connect(set_status)

    def set_anomaly_status(_):
        anomaly_widget = dashboard_widget.anomaly_widget
        skill = anomaly_widget.skill_combo.combo_box.currentText()
        anomaly_widget.status_combo.set_items(
            list(anomaly_widget.details.get(skill, {})), keep_content=True, default_index=-1
        )
        set_anomaly_detail(None)

    dashboard_widget.anomaly_widget.skill_combo.combo_box.currentTextChanged.connect(set_anomaly_status)

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

    def set_anomaly_detail(_):
        anomaly_widget = dashboard_widget.anomaly_widget
        skill = anomaly_widget.skill_combo.combo_box.currentText()
        status = anomaly_widget.status_combo.combo_box.currentText()
        if detail := anomaly_widget.details.get(skill, {}).get(status):
            damage_content, timeline_content = detail_content(detail)
            anomaly_widget.damage_detail.set_content(damage_content)
            anomaly_widget.timeline.set_content(timeline_content)
        else:
            anomaly_widget.damage_detail.table.clear()
            anomaly_widget.timeline.clear_content()
    dashboard_widget.anomaly_widget.status_combo.combo_box.currentTextChanged.connect(set_anomaly_detail)