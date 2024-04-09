from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class TopWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.upload_button = QPushButton("请上传JCL")

        layout.addWidget(self.upload_button)
