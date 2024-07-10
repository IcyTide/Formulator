from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton

from qt.components import ComboWithLabel, TextWithLabel


class ConfigWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        top_layout = QHBoxLayout()
        layout.addLayout(top_layout)
        bottom_layout = QHBoxLayout()
        layout.addLayout(bottom_layout)

        self.config_select = ComboWithLabel("选择预设方案")
        top_layout.addWidget(self.config_select, 1)
        self.config_category = ComboWithLabel("选择导入类别", items=["全部", "装备", "消耗品", "增益", "秘籍"])
        top_layout.addWidget(self.config_category, 1)
        self.load_config = QPushButton("导入预设方案")
        bottom_layout.addWidget(self.load_config, 2)
        self.config_name = TextWithLabel("设置预设方案")
        top_layout.addWidget(self.config_name, 2)
        self.save_config = QPushButton("保存预设方案")
        bottom_layout.addWidget(self.save_config, 1)
        self.delete_config = QPushButton("删除预设方案")
        bottom_layout.addWidget(self.delete_config, 1)
