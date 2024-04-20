from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt

from qt.components import ComboWithLabel


class TopWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.upload_button = QPushButton("请上传JCL")
        layout.addWidget(self.upload_button)
        self.player_select = ComboWithLabel("请选择角色")
        layout.addWidget(self.player_select)
        self.player_select.hide()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
