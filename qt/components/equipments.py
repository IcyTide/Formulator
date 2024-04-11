import json
import os

from qt.constant import POSITION_MAP, STONES_POSITIONS, EQUIPMENTS_DIR, ENCHANTS_DIR, STONES_DIR, MAX_STONE_ATTR
from qt.constant import EMBED_POSITIONS, MAX_EMBED_LEVEL, MAX_STONE_LEVEL, SPECIAL_ENCHANT_POSITIONS
from qt.components import ComboWithLabel, RadioWithLabel, TableWithLabel
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QTabWidget, QSizePolicy, QSpacerItem
from PySide6.QtCore import Qt


class EquipmentWidget(QWidget):
    def __init__(self, label):
        super().__init__()
        self.position = POSITION_MAP[label]
        layout = QHBoxLayout(self)

        input_widget = QWidget()
        input_layout = QVBoxLayout(input_widget)
        layout.addWidget(input_widget, 2, alignment=Qt.AlignmentFlag.AlignTop)

        self.output_widget = QWidget()
        output_layout = QVBoxLayout(self.output_widget)
        layout.addWidget(self.output_widget, 1, alignment=Qt.AlignmentFlag.AlignLeft)

        self.equipment_json = json.load(open(os.path.join(EQUIPMENTS_DIR, self.position), encoding="utf-8"))
        self.enchant_json = json.load(open(os.path.join(ENCHANTS_DIR, self.position), encoding="utf-8"))
        self.equipment = ComboWithLabel("装备")

        self.detail_widget = QWidget()
        detail_layout = QGridLayout(self.detail_widget)

        input_layout.addWidget(self.equipment)
        input_layout.addWidget(self.detail_widget)

        if not self.enchant_json:
            self.enchant = None
        else:
            self.enchant = ComboWithLabel("附魔")
            self.enchant.combo_box.addItems([""] + list(self.enchant_json))
            detail_layout.addWidget(self.enchant, 0, 0, 1, 2)

        if self.position not in SPECIAL_ENCHANT_POSITIONS:
            self.special_enchant = None
        else:
            self.special_enchant = RadioWithLabel("大附魔")
            detail_layout.addWidget(self.special_enchant, 0, 2, 1, 2)

        self.strength_level = ComboWithLabel("精炼等级")
        detail_layout.addWidget(self.strength_level, 1, 0)

        self.embed_levels = []
        for i in range(EMBED_POSITIONS[self.position]):
            embed_level = ComboWithLabel(
                f"镶嵌等级-{i + 1}", items=[str(i) for i in range(MAX_EMBED_LEVEL + 1)]
            )
            embed_level.combo_box.setCurrentIndex(MAX_EMBED_LEVEL)
            self.embed_levels.append(embed_level)
            detail_layout.addWidget(embed_level, 1, i + 1)

        if self.position not in STONES_POSITIONS:
            self.stones_json = None
            self.stone_level = None
            self.stone_attrs = None
        else:
            self.stones_json = json.load(open(STONES_DIR, encoding="utf-8"))

            self.stone_level = ComboWithLabel(
                "五彩石等级", items=[str(i) for i in range(MAX_STONE_LEVEL + 1)])
            self.stone_attrs = []
            detail_layout.addWidget(self.stone_level, 2, 0)
            for i in range(MAX_STONE_ATTR):
                stone_attr = ComboWithLabel(f"五彩石属性-{i + 1}")
                self.stone_attrs.append(stone_attr)
                detail_layout.addWidget(stone_attr, 2, i + 1)
        self.detail_widget.hide()

        self.base_attr = TableWithLabel("基本属性", column_count=2)
        output_layout.addWidget(self.base_attr)
        self.magic_attr = TableWithLabel("精炼属性", column_count=2)
        output_layout.addWidget(self.magic_attr)
        self.embed_attr = TableWithLabel("镶嵌属性", column_count=2)
        output_layout.addWidget(self.embed_attr)
        output_layout.addStretch()
        self.output_widget.hide()


class EquipmentsWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.equipments = {}
        for label in POSITION_MAP:
            self.equipments[label] = EquipmentWidget(label)
            self.addTab(self.equipments[label], label)

    def __getitem__(self, item) -> EquipmentWidget:
        return self.equipments[item]

    def items(self):
        return self.equipments.items()

    def values(self):
        return self.equipments.values()
