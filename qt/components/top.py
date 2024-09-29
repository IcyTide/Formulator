from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton

from qt.components import ComboWithLabel


class TopWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.upload_log = QPushButton("请上传JCL")
        layout.addWidget(self.upload_log, 2)
        self.upload_json = QPushButton("请上传JSON")
        layout.addWidget(self.upload_json, 1)
        self.save_json = QPushButton("保存JSON")
        layout.addWidget(self.save_json, 1)

        self.player_select = ComboWithLabel("请选择角色")
        layout.addWidget(self.player_select, 2)
        self.target_select = ComboWithLabel("选择目标")
        layout.addWidget(self.target_select, 2)

        self.save_json.hide()
        self.player_select.hide()
        self.target_select.hide()
