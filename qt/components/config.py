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

        self.config_select = ComboWithLabel("Select")
        top_layout.addWidget(self.config_select, 1)
        self.load_config = QPushButton("Load")
        bottom_layout.addWidget(self.load_config, 1)
        self.config_name = TextWithLabel("Name")
        top_layout.addWidget(self.config_name, 1)
        self.save_config = QPushButton("Save")
        bottom_layout.addWidget(self.save_config, 1)
