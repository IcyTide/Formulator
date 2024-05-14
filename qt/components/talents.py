from typing import List

from qt.components import ComboWithLabel
from PySide6.QtWidgets import QWidget, QGridLayout

from assets.constant import MAX_TALENTS


class TalentsWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)

        self.talents = []

        rows = 2
        columns = MAX_TALENTS // rows

        for i in range(rows):
            for j in range(columns):
                talent = ComboWithLabel(f"奇穴第{i * columns + j + 1}层")
                self.talents.append(talent)
                layout.addWidget(talent, i, j)

    def __getitem__(self, item) -> ComboWithLabel:
        return self.talents[item]

    def values(self) -> List[ComboWithLabel]:
        return self.talents
