from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton

from qt.components import ComboWithLabel
from schools import SUPPORT_SCHOOLS


class TopWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.school_select = ComboWithLabel("请选择门派", items=list(SUPPORT_SCHOOLS), index=-1)
        layout.addWidget(self.school_select, 2)
        self.upload_json = QPushButton("请上传JSON")
        layout.addWidget(self.upload_json, 1)
        self.save_json = QPushButton("保存JSON")
        layout.addWidget(self.save_json, 1)

        self.save_json.hide()
