from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt

from qt.components import ComboWithLabel


class TopWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.upload_log = QPushButton("请上传JCL")
        layout.addWidget(self.upload_log)
        self.upload_json = QPushButton("请上传JSON")
        layout.addWidget(self.upload_json)
        self.save_json = QPushButton("保存JSON")
        layout.addWidget(self.save_json)
        self.player_select = ComboWithLabel("请选择角色")
        layout.addWidget(self.player_select)

        self.save_json.hide()
        self.player_select.hide()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
