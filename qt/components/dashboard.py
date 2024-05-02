from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTabWidget

from qt.components import ComboWithLabel, DoubleSpinWithLabel, LabelWithLabel, TableWithLabel
from base.constant import SHIELD_BASE_MAP


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
        self.gradient_detail = TableWithLabel("属性收益", column_count=2)
        detail_table_layout.addWidget(self.gradient_detail)
        layout.addWidget(detail_table)

        layout.addStretch()


class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        top_layout = QHBoxLayout()
        layout.addLayout(top_layout)

        self.target_level = ComboWithLabel("目标等级", items=[str(level) for level in SHIELD_BASE_MAP])
        top_layout.addWidget(self.target_level)
        self.duration = DoubleSpinWithLabel("战斗时长", maximum=3600, value=180)
        top_layout.addWidget(self.duration)

        self.button = QPushButton(text="开始模拟!")
        layout.addWidget(self.button)

        bottom_layout = QHBoxLayout()
        layout.addLayout(bottom_layout)

        tab = QTabWidget()
        bottom_layout.addWidget(tab, 2)
        result_layout = QVBoxLayout()
        bottom_layout.addLayout(result_layout, 1)

        attribute = QWidget()
        attribute_layout = QHBoxLayout(attribute)
        tab.addTab(attribute, "属性")

        self.init_attribute = TableWithLabel("增益前属性", column_count=2)
        attribute_layout.addWidget(self.init_attribute)
        self.final_attribute = TableWithLabel("增益后属性", column_count=2)
        attribute_layout.addWidget(self.final_attribute)

        self.detail_widget = DetailWidget()
        tab.addTab(self.detail_widget, "伤害总结")

        self.summary = TableWithLabel("伤害统计", headers=["技能/次数", "命中/%", "会心/%", "伤害/%"])

        tab.addTab(self.summary, "战斗总结")

        self.dps = LabelWithLabel("每秒伤害")
        result_layout.addWidget(self.dps)

        self.gradients = TableWithLabel("属性收益", column_count=2)

        result_layout.addWidget(self.gradients)

        result_layout.addStretch()

        layout.addStretch()
