from collections import defaultdict

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton

from qt.components import ComboWithLabel, LabelWithLabel, TableWithLabel, ListWithLabel, RadioWithLabel, \
    DoubleSpinWithLabel


class DetailWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.details = {}
        self.skill_combo = ComboWithLabel("选择技能", info="技能名字#技能ID-技能等级-技能层数")
        layout.addWidget(self.skill_combo)
        self.status_combo = ComboWithLabel("选择增益", info="增益名字#增益ID-增益等级-增益层数")
        layout.addWidget(self.status_combo)
        detail_table = QWidget()
        detail_table_layout = QHBoxLayout(detail_table)
        self.damage_detail = TableWithLabel("伤害细节", column_count=2)
        detail_table_layout.addWidget(self.damage_detail)
        self.timeline = TableWithLabel("时间轴", headers=["#", "时间", "会心", "伤害"])
        detail_table_layout.addWidget(self.timeline)
        layout.addWidget(detail_table)

        layout.addStretch()


class StatusWidget(QWidget):
    def __init__(self, name):
        super().__init__()
        layout = QVBoxLayout(self)
        self.status_list = ListWithLabel(name)
        layout.addWidget(self.status_list)
        bottom_layout = QHBoxLayout()
        layout.addLayout(bottom_layout)
        self.add_button = QPushButton(f"添加{name}")
        bottom_layout.addWidget(self.add_button)
        self.remove_button = QPushButton(f"移除{name}")
        bottom_layout.addWidget(self.remove_button)


class BuffSelectWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)

        left_layout = QVBoxLayout()
        layout.addLayout(left_layout)
        self.buff_id_select = ComboWithLabel("增益ID")
        left_layout.addWidget(self.buff_id_select)
        self.buff_level_select = ComboWithLabel("增益等级")
        left_layout.addWidget(self.buff_level_select)
        self.buff_stack_select = ComboWithLabel("增益层数")
        left_layout.addWidget(self.buff_stack_select)
        self.buff_name = LabelWithLabel("增益名称：")
        left_layout.addWidget(self.buff_name)

        self.attrs = TableWithLabel("附带属性", column_count=2)
        self.attrs.hide()
        layout.addWidget(self.attrs)
        self.recipes = TableWithLabel("附带秘籍", column_count=2)
        self.recipes.hide()
        layout.addWidget(self.recipes)
        self.current_status = StatusWidget("当前状态")
        layout.addWidget(self.current_status)
        self.snapshot_status = StatusWidget("快照状态")
        self.snapshot_status.hide()
        layout.addWidget(self.snapshot_status)


class DotSelectWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)

        left_layout = QVBoxLayout()
        layout.addLayout(left_layout)
        self.dot_skill_id_select = ComboWithLabel("DOT技能ID")
        left_layout.addWidget(self.dot_skill_id_select)
        self.dot_skill_level_select = ComboWithLabel("DOT技能等级")
        left_layout.addWidget(self.dot_skill_level_select)
        self.dot_stack_select = ComboWithLabel("DOT层数")
        left_layout.addWidget(self.dot_stack_select)
        self.dot_skill_name = LabelWithLabel("DOT技能名称：")
        left_layout.addWidget(self.dot_skill_name)
        right_layout = QVBoxLayout()
        layout.addLayout(right_layout)
        self.consume_skill_id_select = ComboWithLabel("吞噬技能ID")
        right_layout.addWidget(self.consume_skill_id_select)
        self.consume_skill_level_select = ComboWithLabel("吞噬技能等级")
        right_layout.addWidget(self.consume_skill_level_select)
        self.consume_tick_select = ComboWithLabel("吞噬跳数")
        right_layout.addWidget(self.consume_tick_select)
        self.consume_skill_name = LabelWithLabel("吞噬技能名称：")
        right_layout.addWidget(self.consume_skill_name)


class DamageSelectWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)

        left_layout = QVBoxLayout()
        layout.addLayout(left_layout, 1)
        self.damage_type_radio = RadioWithLabel("DOT伤害")
        left_layout.addWidget(self.damage_type_radio)
        self.damage_id_select = ComboWithLabel("伤害ID")
        left_layout.addWidget(self.damage_id_select)
        self.damage_level_select = ComboWithLabel("伤害等级")
        left_layout.addWidget(self.damage_level_select)
        self.damage_count = DoubleSpinWithLabel("伤害次数")
        left_layout.addWidget(self.damage_count)
        self.damage_name = LabelWithLabel("伤害名称：")
        left_layout.addWidget(self.damage_name)

        self.dot_select = DotSelectWidget()
        self.dot_select.hide()
        layout.addWidget(self.dot_select, 2)
        self.details = TableWithLabel("技能细节", column_count=2)
        layout.addWidget(self.details, 1)


class RecordWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.record_list = ListWithLabel("技能记录")
        layout.addWidget(self.record_list)
        bottom_layout = QHBoxLayout()
        layout.addLayout(bottom_layout)
        self.add_button = QPushButton(f"添加技能记录")
        bottom_layout.addWidget(self.add_button)
        self.remove_button = QPushButton(f"移除技能记录")
        bottom_layout.addWidget(self.remove_button)


class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.buff_select = BuffSelectWidget()
        layout.addWidget(self.buff_select)
        self.damage_select = DamageSelectWidget()
        layout.addWidget(self.damage_select)

        self.records = RecordWidget()
        layout.addWidget(self.records)

        # tab = QTabWidget()
        # bottom_layout.addWidget(tab, 2)
        # result_layout = QVBoxLayout()
        # bottom_layout.addLayout(result_layout, 1)
        #
        # attribute = QWidget()
        # attribute_layout = QHBoxLayout(attribute)
        # tab.addTab(attribute, "属性")
        #
        # self.init_attribute = TableWithLabel("增益前属性", column_count=2)
        # attribute_layout.addWidget(self.init_attribute)
        # self.final_attribute = TableWithLabel("增益后属性", column_count=2)
        # attribute_layout.addWidget(self.final_attribute)
        #
        # self.detail_widget = DetailWidget()
        # tab.addTab(self.detail_widget, "伤害总结")
        #
        # self.summary = TableWithLabel("伤害统计", headers=["技能/次数", "期望命中/%", "期望会心/%", "期望总伤害/%"])
        #
        # tab.addTab(self.summary, "战斗总结")
        #
        # self.dps = LabelWithLabel("每秒伤害")
        # result_layout.addWidget(self.dps)
        #
        # self.gradients = TableWithLabel("属性收益", column_count=2)
        #
        # result_layout.addWidget(self.gradients)
        #
        # result_layout.addStretch()

        layout.addStretch()
