from typing import Dict

from assets.constant import ATTR_TYPE_TRANSLATE
from assets.dot_bind_skills import DOT_BIND_SKILLS
from assets.dot_buffs import DOT_BUFFS
from assets.dot_consume_skills import DOT_CONSUME_SKILLS
from assets.school_buffs import SCHOOL_BUFFS
from assets.skill_buffs import SKILL_BUFFS
from base.constant import FRAME_PER_SECOND
from qt.components.dashboard import DashboardWidget
from qt.scripts.bonuses import Bonuses
from qt.scripts.consumables import Consumables
from qt.scripts.equipments import Equipments
from qt.scripts.recipes import Recipes
from qt.scripts.talents import Talents
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


def summary_content(summary: Dict[str, Detail], total: Detail):
    content = []
    total_damage = total.expected_damage
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


def gradient_content(total: Detail):
    content = []
    for k, v in total.gradients.items():
        content.append([ATTR_TYPE_TRANSLATE[k], f"{round(v / total.expected_damage * 100, 2)}%"])
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
        [str(i + 1), str(round(t[0] / FRAME_PER_SECOND, 2)), "会心" if t[1] else "命中", str(t[2])]
        for i, t in enumerate(sorted(detail.timeline))
    ]

    return damage_content, timeline_content


def dashboard_script(analyzer: Analyzer,
                     dashboard_widget: DashboardWidget, talents: Talents, recipes: Recipes,
                     equipments: Equipments, consumables: Consumables, bonuses: Bonuses):
    def select_buff_id(_):
        widget = dashboard_widget.buff_select
        buff_id = widget.buff_id_select.combo_box.currentText()
        damage_id = dashboard_widget.damage_select.damage_id_select.combo_box.currentText()
        dot_skill_id = dashboard_widget.damage_select.dot_select.dot_skill_id_select.combo_box.currentText()
        if buff_id:
            school = analyzer.school
            buff_id = int(buff_id)
            if buff_id in SCHOOL_BUFFS[school.id]:
                buff_levels = SCHOOL_BUFFS[school.id][buff_id]
            elif dot_skill_id:
                buff_levels = DOT_BUFFS[school.id][int(dot_skill_id)][buff_id]
            else:
                buff_levels = SKILL_BUFFS[school.id][int(damage_id)][buff_id]
            buff_levels = [str(level) for level in buff_levels]
            widget.buff_level_select.set_items(buff_levels, default_index=len(buff_levels) - 1)
        else:
            widget.buff_level_select.set_items([], default_index=-1)
        select_buff_level(None)

    dashboard_widget.buff_select.buff_id_select.combo_box.currentTextChanged.connect(select_buff_id)

    def select_buff_level(_):
        widget = dashboard_widget.buff_select
        buff_id = widget.buff_id_select.combo_box.currentText()
        buff_level = widget.buff_level_select.combo_box.currentText()
        if buff_id and buff_level:
            school = analyzer.school
            buff_id, buff_level = int(buff_id), int(buff_level)
            buff, buff.buff_level = school.buffs[buff_id], buff_level
            buff_stacks = [str(buff_stack + 1) for buff_stack in range(buff.max_stack)]
            widget.buff_name.set_text(buff.display_name)
            widget.buff_stack_select.set_items(buff_stacks, keep_index=True)
            if buff.attributes:
                widget.attrs.show()
                widget.attrs.set_content(list(buff.attributes.items()))
            else:
                widget.attrs.hide()
            if buff.recipes:
                widget.recipes.show()
                widget.recipes.set_content(list(buff.recipes.items()))
            else:
                widget.recipes.hide()
        else:
            widget.buff_name.text.clear()
            widget.attrs.clear_content()
            widget.recipes.clear_content()

    dashboard_widget.buff_select.buff_level_select.combo_box.currentTextChanged.connect(select_buff_level)

    def add_current_status():
        widget = dashboard_widget.buff_select
        buff_id = widget.buff_id_select.combo_box.currentText()
        buff_level = widget.buff_level_select.combo_box.currentText()
        buff_stack = widget.buff_stack_select.combo_box.currentText()
        if buff_id and buff_level and buff_stack:
            school = analyzer.school
            buff_id, buff_level, buff_stack = int(buff_id), int(buff_level), int(buff_stack)
            buff, buff.buff_level, buff.buff_stack = school.buffs[buff_id], buff_level, buff_stack
            widget.current_status.status[(buff_id, buff_level)] = buff_stack
            widget.current_status.buff2name[(buff_id, buff_level)] = buff.display_name
            widget.current_status.status_list.set_items(list(widget.current_status.buff2name.values()))

    dashboard_widget.buff_select.current_status.add_button.clicked.connect(add_current_status)

    def add_snapshot_status():
        widget = dashboard_widget.buff_select
        buff_id = widget.buff_id_select.combo_box.currentText()
        buff_level = widget.buff_level_select.combo_box.currentText()
        buff_stack = widget.buff_stack_select.combo_box.currentText()
        if buff_id and buff_level:
            school = analyzer.school
            buff_id, buff_level, buff_stack = int(buff_id), int(buff_level), int(buff_stack)
            buff, buff.buff_level, buff.buff_stack = school.buffs[buff_id], buff_level, buff_stack
            widget.snapshot_status.status[(buff_id, buff_level)] = buff_stack
            widget.snapshot_status.buff2name[(buff_id, buff_level)] = buff.display_name
            widget.snapshot_status.status_list.set_items(list(widget.snapshot_status.buff2name.values()))

    dashboard_widget.buff_select.snapshot_status.add_button.clicked.connect(add_snapshot_status)

    def remove_current_status():
        widget = dashboard_widget.buff_select.current_status
        selected_items = widget.status_list.list.selectedItems()
        if selected_items:
            for selected_item in selected_items:
                widget.status_list.list.takeItem(widget.status_list.list.row(selected_item))
                buff_key = widget.name2buff[selected_item.text()]
                widget.status.pop(buff_key)
                widget.buff2name.pop(buff_key)

    dashboard_widget.buff_select.current_status.remove_button.clicked.connect(remove_current_status)

    def remove_snapshot_status():
        widget = dashboard_widget.buff_select.snapshot_status
        selected_items = widget.status_list.list.selectedItems()
        if selected_items:
            for selected_item in selected_items:
                widget.status_list.list.takeItem(widget.status_list.list.row(selected_item))
                buff_key = widget.name2buff[selected_item.text()]
                widget.status.pop(buff_key)
                widget.buff2name.pop(buff_key)

    dashboard_widget.buff_select.snapshot_status.remove_button.clicked.connect(remove_snapshot_status)

    def update_current_status(item):
        widget = dashboard_widget.buff_select
        buff_name = item.text()
        if buff_name in widget.current_status.name2buff:
            buff_id, buff_level = widget.current_status.name2buff[buff_name]
            buff_stack = widget.current_status.status[(buff_id, buff_level)]

            widget.buff_id_select.combo_box.setCurrentText(str(buff_id))
            widget.buff_level_select.combo_box.setCurrentText(str(buff_level))
            widget.buff_stack_select.combo_box.setCurrentText(str(buff_stack))

    dashboard_widget.buff_select.current_status.status_list.list.itemClicked.connect(update_current_status)

    def update_snapshot_status(item):
        widget = dashboard_widget.buff_select
        buff_name = item.text()
        if buff_name in widget.snapshot_status.name2buff:
            buff_id, buff_level = widget.snapshot_status.name2buff[buff_name]
            buff_stack = widget.snapshot_status.status[(buff_id, buff_level)]

            widget.buff_id_select.combo_box.setCurrentText(str(buff_id))
            widget.buff_level_select.combo_box.setCurrentText(str(buff_level))
            widget.buff_stack_select.combo_box.setCurrentText(str(buff_stack))

    dashboard_widget.buff_select.snapshot_status.status_list.list.itemClicked.connect(update_snapshot_status)

    def damage_type_check(_):
        if dashboard_widget.damage_select.damage_type_radio.radio_button.isChecked():
            damage_ids = [str(dot_id) for dot_id in DOT_BIND_SKILLS[analyzer.school.id]]
            dashboard_widget.damage_select.dot_select.show()
            dashboard_widget.buff_select.snapshot_status.show()
        else:
            damage_ids = [str(skill_id) for skill_id in SKILL_BUFFS[analyzer.school.id]]
            dashboard_widget.damage_select.dot_select.hide()
            dashboard_widget.buff_select.snapshot_status.hide()
        dashboard_widget.damage_select.damage_id_select.set_items(damage_ids, default_index=-1)

    dashboard_widget.damage_select.damage_type_radio.radio_button.clicked.connect(damage_type_check)

    def select_damage_id(_):
        widget = dashboard_widget.damage_select
        damage_id = widget.damage_id_select.combo_box.currentText()
        is_dot = widget.damage_type_radio.radio_button.isChecked()
        if damage_id:
            school = analyzer.school
            damage_id = int(damage_id)
            if is_dot:
                damage = school.dots[damage_id]
                dot_skill_ids = [str(skill_id) for skill_id in DOT_BIND_SKILLS[school.id][damage_id]]
                widget.dot_select.dot_skill_id_select.set_items(dot_skill_ids)
                consume_skill_ids = [str(skill_id) for skill_id in DOT_CONSUME_SKILLS[school.id][damage_id]]
                widget.dot_select.consume_skill_id_select.set_items([""] + consume_skill_ids)
            else:
                damage = school.skills[damage_id]
                buff_ids = [str(buff_id) for buff_id in
                            list(SKILL_BUFFS[school.id][damage_id]) + list(SCHOOL_BUFFS[school.id])]
                dashboard_widget.buff_select.buff_id_select.set_items(buff_ids, keep_index=True, default_index=-1)
            damage_levels = [str(damage_level + 1) for damage_level in range(damage.max_level)]
            widget.damage_level_select.set_items(damage_levels, default_index=len(damage_levels) - 1)
        else:
            widget.damage_level_select.set_items([], default_index=-1)
            widget.dot_select.dot_skill_id_select.set_items([], default_index=-1)
            widget.dot_select.consume_skill_id_select.set_items([], default_index=-1)
        select_dot_skill_id(None)
        select_consume_skill_id(None)
        select_damage_level(None)

    dashboard_widget.damage_select.damage_id_select.combo_box.currentTextChanged.connect(select_damage_id)

    def select_damage_level(_):
        widget = dashboard_widget.damage_select
        damage_id = widget.damage_id_select.combo_box.currentText()
        damage_level = widget.damage_level_select.combo_box.currentText()
        is_dot = widget.damage_type_radio.radio_button.isChecked()
        if damage_id and damage_level:
            school = analyzer.school
            damage_id, damage_level = int(damage_id), int(damage_level)
            if is_dot:
                damage, damage.buff_level = school.dots[damage_id], damage_level
                dot_stacks = [str(dot_stack + 1) for dot_stack in range(damage.max_stack)]
                widget.dot_select.dot_stack_select.set_items(dot_stacks)
                consume_ticks = [str(consume_tick + 1) for consume_tick in range(damage.tick)]
                widget.dot_select.consume_tick_select.set_items(consume_ticks)
            else:
                damage, damage.skill_level = school.skills[damage_id], damage_level
            widget.damage_name.set_text(damage.display_name)
        else:
            widget.damage_name.text.clear()
            widget.dot_select.dot_stack_select.set_items([], default_index=-1)
            widget.dot_select.consume_tick_select.set_items([], default_index=-1)

    dashboard_widget.damage_select.damage_level_select.combo_box.currentTextChanged.connect(select_damage_level)

    def select_dot_skill_id(_):
        widget = dashboard_widget.damage_select
        damage_id = widget.damage_id_select.combo_box.currentText()
        dot_skill_id = widget.dot_select.dot_skill_id_select.combo_box.currentText()

        if damage_id and dot_skill_id:
            school = analyzer.school
            damage_id, dot_skill_id = int(damage_id), int(dot_skill_id)
            dot_skill_levels = [str(skill_level) for skill_level in
                                DOT_BIND_SKILLS[school.id][damage_id][dot_skill_id]]
            widget.dot_select.dot_skill_level_select.set_items(dot_skill_levels,
                                                               default_index=len(dot_skill_levels) - 1)

            buff_ids = [str(buff_id) for buff_id in
                        list(DOT_BUFFS[school.id][dot_skill_id]) + list(SCHOOL_BUFFS[school.id])]
            dashboard_widget.buff_select.buff_id_select.set_items(buff_ids, keep_index=True, default_index=-1)
        else:
            widget.dot_select.dot_skill_level_select.set_items([], default_index=-1)
        select_dot_skill_level(None)

    dashboard_widget.damage_select.dot_select.dot_skill_id_select.combo_box.currentTextChanged.connect(
        select_dot_skill_id)

    def select_dot_skill_level(_):
        widget = dashboard_widget.damage_select
        damage_id = widget.damage_id_select.combo_box.currentText()
        dot_skill_id = widget.dot_select.dot_skill_id_select.combo_box.currentText()
        dot_skill_level = widget.dot_select.dot_skill_level_select.combo_box.currentText()

        if damage_id and dot_skill_id and dot_skill_level:
            school = analyzer.school
            damage_id, dot_skill_id, dot_skill_level = int(damage_id), int(dot_skill_id), int(dot_skill_level)
            dot_skill, dot_skill.skill_level = school.skills[dot_skill_id], dot_skill_level
            widget.dot_select.dot_skill_name.set_text(dot_skill.display_name)
        else:
            widget.dot_select.dot_skill_name.text.clear()

    dashboard_widget.damage_select.dot_select.dot_skill_level_select.combo_box.currentTextChanged.connect(
        select_dot_skill_level)

    def select_consume_skill_id(_):
        widget = dashboard_widget.damage_select
        damage_id = widget.damage_id_select.combo_box.currentText()
        consume_skill_id = widget.dot_select.consume_skill_id_select.combo_box.currentText()

        if damage_id and consume_skill_id:
            school = analyzer.school
            damage_id, consume_skill_id = int(damage_id), int(consume_skill_id)
            consume_skill_levels = [str(skill_level) for skill_level in
                                    DOT_CONSUME_SKILLS[school.id][damage_id][consume_skill_id]]
            widget.dot_select.consume_skill_level_select.set_items(consume_skill_levels,
                                                                   default_index=len(consume_skill_levels) - 1)
        else:
            widget.dot_select.consume_skill_level_select.set_items([], default_index=-1)

    dashboard_widget.damage_select.dot_select.consume_skill_id_select.combo_box.currentTextChanged.connect(
        select_consume_skill_id)

    def select_consume_skill_level(_):
        widget = dashboard_widget.damage_select
        damage_id = widget.damage_id_select.combo_box.currentText()
        consume_skill_id = widget.dot_select.consume_skill_id_select.combo_box.currentText()
        consume_skill_level = widget.dot_select.consume_skill_level_select.combo_box.currentText()

        if damage_id and consume_skill_id and consume_skill_level:
            school = analyzer.school
            damage_id, consume_skill_id, consume_skill_level = int(damage_id), int(consume_skill_id), int(
                consume_skill_level)
            consume_skill, consume_skill.skill_level = school.skills[consume_skill_id], consume_skill_level
            widget.dot_select.consume_skill_name.set_text(consume_skill.display_name)
        else:
            widget.dot_select.consume_skill_name.text.clear()

    dashboard_widget.damage_select.dot_select.consume_skill_level_select.combo_box.currentTextChanged.connect(
        select_consume_skill_level)

    def add_record():
        is_dot = dashboard_widget.damage_select.damage_type_radio.radio_button.isChecked()
        damage_id = dashboard_widget.damage_select.damage_id_select.combo_box.currentText()
        damage_level = dashboard_widget.damage_select.damage_level_select.combo_box.currentText()
        damage_count = dashboard_widget.damage_select.damage_count.spin_box.value()
        dot_skill_id = dashboard_widget.damage_select.dot_select.dot_skill_id_select.combo_box.currentText()
        dot_skill_level = dashboard_widget.damage_select.dot_select.dot_skill_level_select.combo_box.currentText()
        dot_stack = dashboard_widget.damage_select.dot_select.dot_stack_select.combo_box.currentText()
        consume_skill_id = dashboard_widget.damage_select.dot_select.consume_skill_id_select.combo_box.currentText()
        consume_skill_level = dashboard_widget.damage_select.dot_select.consume_skill_level_select.combo_box.currentText()
        consume_tick = dashboard_widget.damage_select.dot_select.consume_tick_select.combo_box.currentText()
        current_status = dashboard_widget.buff_select.current_status.status
        current_status = tuple([(buff_id, buff_level, buff_stack) for (buff_id, buff_level), buff_stack in
                                current_status.items()])
        if is_dot and damage_id and dot_skill_id and damage_count:
            damage_id, damage_level = int(damage_id), int(damage_level)
            dot_skill_id, dot_skill_level, dot_stack = int(dot_skill_id), int(dot_skill_level), int(dot_stack)
            if consume_skill_id:
                consume_tick = int(consume_tick)
                consume_skill_id, consume_skill_level = int(consume_skill_id), int(consume_skill_level)
                damage = ((damage_id, damage_level, dot_stack * consume_tick), (dot_skill_id, dot_skill_level),
                          (consume_skill_id, consume_skill_level))
            else:
                damage = ((damage_id, damage_level, dot_stack * consume_tick), (dot_skill_id, dot_skill_level), tuple())
            snapshot_status = dashboard_widget.buff_select.snapshot_status.status
            snapshot_status = tuple([(buff_id, buff_level, buff_stack) for (buff_id, buff_level), buff_stack in
                                     snapshot_status.items()])
            status = (current_status, snapshot_status)
            dashboard_widget.records.records[damage][status] = damage_count

            name = f"{damage}|{current_status}|{snapshot_status}"
            dashboard_widget.records.record2name[(damage, status)] = name
        elif not is_dot and damage_id and damage_count:
            damage_id, damage_level = int(damage_id), int(damage_level)
            damage = ((damage_id, damage_level, 1), (), ())
            status = (current_status, tuple())
            dashboard_widget.records.records[damage][status] = damage_count
            name = f"{damage}|{current_status}"
            dashboard_widget.records.record2name[(damage, status)] = name
        else:
            return

        dashboard_widget.records.record_list.set_items(list(dashboard_widget.records.record2name.values()))

    dashboard_widget.records.add_button.clicked.connect(add_record)
