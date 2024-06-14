import json
import os

from assets.constant import POSITION_MAP, STONES_POSITIONS, EQUIPMENTS_DIR, ENCHANTS_DIR, STONES_DIR, MAX_STONE_ATTR, \
    MAX_STRENGTH_LEVEL
from assets.constant import EMBED_POSITIONS, MAX_EMBED_LEVEL, MAX_STONE_LEVEL, SPECIAL_ENCHANT_POSITIONS
from general.gains.equipment import CriticalSet
from qt.components import ComboWithLabel, RadioWithLabel, TableWithLabel, SpinWithLabel
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QTabWidget


class EquipmentWidget(QWidget):
    def __init__(self, label):
        super().__init__()
        self.position = POSITION_MAP[label]
        layout = QVBoxLayout(self)

        self.equipment_json = json.load(open(os.path.join(EQUIPMENTS_DIR, self.position), encoding="utf-8"))
        self.equipment_mapping = {v['id']: k for k, v in self.equipment_json.items()}
        self.enchant_json = json.load(open(os.path.join(ENCHANTS_DIR, self.position), encoding="utf-8"))
        self.enchant_mapping = {v['id']: k for k, v in self.enchant_json.items()}
        self.equipment = ComboWithLabel("装备")
        layout.addWidget(self.equipment)

        self.detail_widget = QWidget()
        detail_layout = QHBoxLayout(self.detail_widget)
        layout.addWidget(self.detail_widget)
        self.detail_widget.hide()
        layout.addStretch()

        input_layout = QGridLayout()
        detail_layout.addLayout(input_layout)

        if not self.enchant_json:
            self.enchant = None
        else:
            self.enchant = ComboWithLabel("附魔")
            self.enchant.set_items([""] + list(self.enchant_json))
            input_layout.addWidget(self.enchant, 0, 0, 1, 2)

        if self.position not in SPECIAL_ENCHANT_POSITIONS:
            self.special_enchant = None
        else:
            self.special_enchant = RadioWithLabel("大附魔")
            input_layout.addWidget(self.special_enchant, 0, 2, 1, 2)

        self.strength_level = ComboWithLabel("精炼等级")
        input_layout.addWidget(self.strength_level, 1, 0)

        self.embed_levels = []
        for i in range(EMBED_POSITIONS[self.position]):
            embed_level = ComboWithLabel(
                f"镶嵌等级-{i + 1}", items=[str(i) for i in range(MAX_EMBED_LEVEL + 1)]
            )
            embed_level.combo_box.setCurrentIndex(MAX_EMBED_LEVEL)
            self.embed_levels.append(embed_level)
            input_layout.addWidget(embed_level, 1, i + 1)

        if self.position not in STONES_POSITIONS:
            self.stones_json = None
            self.stone_level = None
            self.stone_attrs = None
        else:
            self.stones_json = json.load(open(STONES_DIR, encoding="utf-8"))

            self.stone_level = ComboWithLabel(
                "五彩石等级", items=[str(i) for i in range(MAX_STONE_LEVEL + 1)]
            )
            self.stone_attrs = []
            input_layout.addWidget(self.stone_level, 2, 0)
            for i in range(MAX_STONE_ATTR):
                stone_attr = ComboWithLabel(f"五彩石属性-{i + 1}")
                self.stone_attrs.append(stone_attr)
                input_layout.addWidget(stone_attr, 2, i + 1)
        self.detail_widget.hide()

        output_layout = QVBoxLayout()
        detail_layout.addLayout(output_layout)
        self.base_attr = TableWithLabel("基本属性", column_count=2)
        output_layout.addWidget(self.base_attr)
        self.magic_attr = TableWithLabel("精炼属性", column_count=2)
        output_layout.addWidget(self.magic_attr)
        self.embed_attr = TableWithLabel("镶嵌属性", column_count=2)
        output_layout.addWidget(self.embed_attr)


class EquipmentsWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        top_layout = QHBoxLayout()
        layout.addLayout(top_layout)
        self.real_formulation = RadioWithLabel("开启真实装备增益模拟(仅包括存在覆盖率的BUFF,不包含额外技能)", tag=True)
        top_layout.addWidget(self.real_formulation, 3)
        self.all_special_enchant = RadioWithLabel("一键大附魔")
        top_layout.addWidget(self.all_special_enchant, 1)
        self.critical_set_rate = SpinWithLabel("套装效果", "覆盖(%)", maximum=100, value=100 * CriticalSet.rate)
        top_layout.addWidget(self.critical_set_rate, 1)
        self.all_strength_level = ComboWithLabel(
            "全部精炼等级", items=[str(i) for i in range(MAX_STRENGTH_LEVEL + 1)], index=MAX_STRENGTH_LEVEL)
        top_layout.addWidget(self.all_strength_level, 1)
        self.all_embed_level = ComboWithLabel(
            "全部镶嵌等级", items=[str(i) for i in range(MAX_EMBED_LEVEL + 1)], index=MAX_STRENGTH_LEVEL)
        top_layout.addWidget(self.all_embed_level, 1)

        tabs = QTabWidget()
        layout.addWidget(tabs)

        self.equipments = {}
        for label in POSITION_MAP:
            self.equipments[label] = EquipmentWidget(label)
            tabs.addTab(self.equipments[label], label)

    def __getitem__(self, item) -> EquipmentWidget:
        return self.equipments[item]

    def items(self):
        return self.equipments.items()

    def values(self):
        return self.equipments.values()
