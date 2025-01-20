from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTabWidget, QMessageBox

from base.constant import SHIELD_BASE_MAP
from qt.components import ComboWithLabel, DoubleSpinWithLabel, LabelWithLabel, TableWithLabel


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


class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        top_layout = QHBoxLayout()
        layout.addLayout(top_layout)

        self.target_level = ComboWithLabel("目标等级", items=[str(level) for level in SHIELD_BASE_MAP])
        top_layout.addWidget(self.target_level)
        self.start_time = DoubleSpinWithLabel("开始时间", maximum=3600, value=0)
        top_layout.addWidget(self.start_time)
        self.end_time = DoubleSpinWithLabel("结束时间", maximum=3600, value=180)
        top_layout.addWidget(self.end_time)

        mid_layout = QHBoxLayout()
        layout.addLayout(mid_layout)
        self.formulate_button = QPushButton(text="开始模拟!")
        mid_layout.addWidget(self.formulate_button)
        self.export_button = QPushButton(text="导出上一次模拟结果！")
        mid_layout.addWidget(self.export_button)

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
        self.anomaly_widget = DetailWidget()
        tab.addTab(self.anomaly_widget, "异常伤害")

        self.summary = TableWithLabel("伤害统计", headers=["技能/次数", "期望命中/%", "期望会心/%", "期望总伤害/%"])

        tab.addTab(self.summary, "战斗总结")

        self.dps = LabelWithLabel("每秒伤害")
        result_layout.addWidget(self.dps)

        self.gradients = TableWithLabel("属性收益", column_count=2)

        result_layout.addWidget(self.gradients)

        result_layout.addStretch()

        layout.addStretch()

    def pop_warning(self, text):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("报告")
        msg_box.setText(text)
        msg_box.exec()
