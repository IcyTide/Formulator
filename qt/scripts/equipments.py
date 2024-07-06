from collections import defaultdict
from typing import Dict, List, Union, Tuple

from assets.constant import ATTR_TYPE_TRANSLATE, ATTR_TYPE_TRANSLATE_REVERSE
from assets.constant import POSITION_MAP, STONES_POSITIONS, EMBED_POSITIONS
from assets.constant import STRENGTH_COF, EMBED_COF, MAX_STRENGTH_LEVEL, MAX_EMBED_LEVEL
from general.gains.equipment import EQUIPMENT_GAINS, set_real_formulation, set_critical_set_rate
from qt.components.equipments import EquipmentsWidget


class Enchant:
    name: str
    attr: Dict[str, int]

    def __init__(self):
        self.clear()

    def clear(self):
        self.name = ""
        self.attr = {}


class Stone:
    name: str
    level: int
    attr: Dict[str, int]

    def __init__(self):
        self.clear()

    def clear(self):
        self.name = ""
        self.attr = {}


class Equipment:
    name: str
    base: Dict[str, int]
    magic: Dict[str, int]
    max_strength: int
    embed: Dict[str, int]
    gains: List[int]
    special_enchant: Union[int, Tuple[int, int]]
    special_enchant_gain: List[List[int]]
    set_id: str
    set_attr: Dict[int, Dict[str, int]]
    set_gain: Dict[int, List[int]]

    def __init__(self, label):
        self.clear()

        self.label = label
        self.position = POSITION_MAP[label]

        self.max_strength = MAX_STRENGTH_LEVEL
        self.strength_level = MAX_STRENGTH_LEVEL
        self.embed_levels = [MAX_EMBED_LEVEL for _ in range(EMBED_POSITIONS[self.position])]

        self.enchant = Enchant()
        if self.position in STONES_POSITIONS:
            self.stone = Stone()
        else:
            self.stone = None

    def clear(self):
        self.name = ""
        self.base = {}
        self.magic = {}
        self.embed = {}
        self.gains = []
        self.special_enchant_gain = []
        self.set_id = ""
        self.set_attr = {}
        self.set_gain = {}

    @property
    def base_attr(self) -> Dict[str, int]:
        return self.base

    @property
    def magic_attr(self) -> Dict[str, int]:
        return self.magic

    @property
    def strength_attr(self) -> Dict[str, int]:
        if self.strength_level:
            return {k: int(STRENGTH_COF(self.strength_level) * v + 0.5) for k, v in self.magic.items()}
        else:
            return {}

    @property
    def embed_attr(self) -> Dict[str, int]:
        return {
            k: int(EMBED_COF(self.embed_levels[i]) * self.embed[k])
            for i, k in enumerate(self.embed) if self.embed_levels[i]
        }

    @property
    def base_attr_content(self):
        return [[ATTR_TYPE_TRANSLATE[k], str(v)] for k, v in self.base_attr.items() if k in ATTR_TYPE_TRANSLATE]

    @property
    def magic_attr_content(self):
        if strength_attr := self.strength_attr:
            return [[ATTR_TYPE_TRANSLATE[k], f"{v}(+{strength_attr[k]})"] for k, v in self.magic_attr.items()]
        else:
            return [[ATTR_TYPE_TRANSLATE[k], f"{v}"] for k, v in self.magic_attr.items()]

    @property
    def embed_attr_content(self):
        return [[ATTR_TYPE_TRANSLATE[k], str(v)] for k, v in self.embed_attr.items()]


class Equipments:
    def __init__(self):
        self.equipments = {label: Equipment(label) for label in POSITION_MAP}
        self.real_formulation = False

    def __getitem__(self, item) -> Equipment:
        return self.equipments[item]

    @property
    def secondary_weapon(self):
        return bool(self.equipments['额外武器'])

    @property
    def secondary_weapon_attrs(self):
        primary_weapon, secondary_weapon = self.equipments["近战武器"], self.equipments['额外武器']

        secondary_weapon_attrs = defaultdict(int)
        for attr, value in secondary_weapon.base_attr.items():
            secondary_weapon_attrs[attr] += value
        for attr, value in secondary_weapon.magic_attr.items():
            secondary_weapon_attrs[attr] += value
        for attr, value in secondary_weapon.strength_attr.items():
            secondary_weapon_attrs[attr] += value
        for attr, value in secondary_weapon.embed_attr.items():
            secondary_weapon_attrs[attr] += value
        for attr, value in secondary_weapon.enchant.attr.items():
            secondary_weapon_attrs[attr] += value
        for attr, value in secondary_weapon.stone.attr.items():
            secondary_weapon_attrs[attr] += value

        for attr, value in primary_weapon.base_attr.items():
            secondary_weapon_attrs[attr] -= value
        for attr, value in primary_weapon.magic_attr.items():
            secondary_weapon_attrs[attr] -= value
        for attr, value in primary_weapon.strength_attr.items():
            secondary_weapon_attrs[attr] -= value
        for attr, value in primary_weapon.embed_attr.items():
            secondary_weapon_attrs[attr] -= value
        for attr, value in primary_weapon.enchant.attr.items():
            secondary_weapon_attrs[attr] -= value
        for attr, value in primary_weapon.stone.attr.items():
            secondary_weapon_attrs[attr] -= value
        return secondary_weapon_attrs

    @property
    def attrs(self):
        final_attrs = defaultdict(int)
        set_count = {}
        set_effect = {}
        for label, equipment in self.equipments.items():
            if not equipment.name or label == "额外武器":
                continue
            for attr, value in equipment.base_attr.items():
                final_attrs[attr] += value
            for attr, value in equipment.magic_attr.items():
                final_attrs[attr] += value
            for attr, value in equipment.strength_attr.items():
                final_attrs[attr] += value
            for attr, value in equipment.embed_attr.items():
                final_attrs[attr] += value
            for attr, value in equipment.enchant.attr.items():
                final_attrs[attr] += value
            if equipment.stone:
                for attr, value in equipment.stone.attr.items():
                    final_attrs[attr] += value

            if equipment.set_id not in set_count:
                set_count[equipment.set_id] = 0
                set_effect[equipment.set_id] = equipment.set_attr
            set_count[equipment.set_id] += 1

        for set_id, set_attr in set_effect.items():
            for count, attrs in set_attr.items():
                if int(count) > set_count[set_id]:
                    break
                for attr, value in attrs.items():
                    final_attrs[attr] += value

        return final_attrs

    @property
    def gains(self):
        final_gains = []
        set_count = {}
        set_effect = {}
        for equipment in self.equipments.values():
            if not equipment.name:
                continue
            final_gains += [gain for gain in equipment.gains + equipment.special_enchant_gain]
            if equipment.set_id not in set_count:
                set_count[equipment.set_id] = 0
                set_effect[equipment.set_id] = equipment.set_gain
            set_count[equipment.set_id] += 1

        for set_id, set_gain in set_effect.items():
            for count, gains in set_gain.items():
                if int(count) > set_count[set_id]:
                    break
                final_gains += gains

        return [tuple(gain) if isinstance(gain, list) else gain for gain in final_gains]


def equipments_script(equipments_widget: EquipmentsWidget):
    equipments = Equipments()

    def real_equipment_gain():
        widget = equipments_widget.real_formulation
        if widget.radio_button.isChecked():
            set_real_formulation(True)
        else:
            set_real_formulation(False)

    equipments_widget.real_formulation.radio_button.clicked.connect(real_equipment_gain)

    def critical_set_rate(value):
        set_critical_set_rate(value / 100)

    equipments_widget.critical_set_rate.spin_box.valueChanged.connect(critical_set_rate)

    def all_special_enchant_update():
        for label, widget in equipments_widget.items():
            if special_enchant := widget.special_enchant:
                special_enchant.radio_button.setChecked(equipments_widget.all_special_enchant.radio_button.isChecked())
                special_enchant_update(label)()

    equipments_widget.all_special_enchant.radio_button.clicked.connect(all_special_enchant_update)

    def all_strength_level_update(index):
        for label, widget in equipments_widget.items():
            equipment = equipments[label]
            index = min(equipment.max_strength, index)
            widget.strength_level.combo_box.setCurrentIndex(index)

    equipments_widget.all_strength_level.combo_box.currentIndexChanged.connect(all_strength_level_update)

    def all_embed_level_update(index):
        for widget in equipments_widget.values():
            for embed_level in widget.embed_levels:
                embed_level.combo_box.setCurrentIndex(index)

    equipments_widget.all_embed_level.combo_box.currentIndexChanged.connect(all_embed_level_update)

    def equipment_update(label):
        widget = equipments_widget[label]
        equipment = equipments[label]

        def inner(equipment_name):

            if not equipment_name:
                equipment.clear()
                widget.detail_widget.hide()
                return

            if equipment.strength_level == equipment.max_strength:
                max_strength = True
            else:
                max_strength = False

            equipment.name = equipment_name
            equipment_detail = widget.equipment_json[equipment_name]
            for k, v in equipment_detail.items():
                setattr(equipment, k, v)

            if equipment.base:
                widget.base_attr.set_content(equipment.base_attr_content)
                widget.base_attr.show()
            else:
                widget.base_attr.hide()

            if max_strength:
                equipment.strength_level = equipment.max_strength

            widget.strength_level.set_items([str(i) for i in range(equipment.max_strength + 1)])
            widget.strength_level.combo_box.setCurrentIndex(equipment.strength_level)

            if equipment.embed:
                for i, (attr, value) in enumerate(equipment.embed.items()):
                    widget.embed_levels[i].set_label(f"镶嵌等级-{ATTR_TYPE_TRANSLATE[attr]}\t")
                widget.embed_attr.set_content(equipment.embed_attr_content)
                widget.embed_attr.show()
            else:
                widget.embed_attr.hide()

            if isinstance(equipment.special_enchant, list):
                equipment.special_enchant = tuple(equipment.special_enchant)

            if equipment.special_enchant:
                widget.special_enchant.set_text(EQUIPMENT_GAINS[equipment.special_enchant].gain_name)

            widget.detail_widget.show()

        return inner

    def enchant_update(label):
        widget = equipments_widget.equipments[label]
        equipment = equipments[label]

        def inner(enchant_name):
            if enchant_name:
                enchant_detail = widget.enchant_json[enchant_name]
                equipment.enchant.name = enchant_name
                for k, v in enchant_detail.items():
                    setattr(equipment.enchant, k, v)
            else:
                equipment.enchant.clear()

        return inner

    def special_enchant_update(label):
        widget = equipments_widget.equipments[label]
        equipment = equipments[label]

        def inner():
            if widget.special_enchant and widget.special_enchant.radio_button.isChecked():
                equipment.special_enchant_gain = [equipment.special_enchant]
            else:
                equipment.special_enchant_gain = []

        return inner

    def strength_level_update(label):
        widget = equipments_widget.equipments[label]
        equipment = equipments[label]

        def inner(index):
            equipment.strength_level = index
            if magic_attr_content := equipment.magic_attr_content:
                widget.magic_attr.set_content(magic_attr_content)
                widget.magic_attr.show()
            else:
                widget.magic_attr.hide()

        return inner

    def embed_level_update(i, label):
        widget = equipments_widget.equipments[label]
        equipment = equipments[label]

        def inner(index):
            equipment.embed_levels[i] = index
            if embed_attr_content := equipment.embed_attr_content:
                widget.embed_attr.set_content(embed_attr_content)
                widget.embed_attr.show()
            else:
                widget.embed_attr.hide()

        return inner

    def stone_update(label):
        widget = equipments_widget.equipments[label]
        equipment = equipments[label]

        def inner(_):
            level = widget.stone_level.combo_box.currentText()
            if level == '0':
                for stone in widget.stone_attrs:
                    stone.set_items([""])
                widget.stone_attrs[0].set_items([""] + [ATTR_TYPE_TRANSLATE[k] for k in widget.stones_json])
                equipment.stone = Stone()
                return
            current = widget.stones_json
            i = 0
            while i < len(widget.stone_attrs):
                attr = ATTR_TYPE_TRANSLATE_REVERSE.get(widget.stone_attrs[i].combo_box.currentText())
                if attr in current:
                    current = current[attr]
                    i += 1
                else:
                    break
            if level in current:
                for k, v in current[level].items():
                    setattr(equipment.stone, k, v)
            else:
                widget.stone_attrs[i].set_items([""] + [ATTR_TYPE_TRANSLATE[k] for k in current])
                equipment.stone = Stone()

            i += 1
            while i < len(widget.stone_attrs):
                widget.stone_attrs[i].set_items([""])
                i += 1

        return inner

    for equipment_label, equipment_widget in equipments_widget.items():

        equipment_widget.equipment.combo_box.currentTextChanged.connect(equipment_update(equipment_label))
        if equipment_widget.special_enchant:
            equipment_widget.special_enchant.radio_button.clicked.connect(special_enchant_update(equipment_label))
        if equipment_widget.enchant:
            equipment_widget.enchant.combo_box.currentTextChanged.connect(enchant_update(equipment_label))
        equipment_widget.strength_level.combo_box.currentIndexChanged.connect(strength_level_update(equipment_label))
        for n, embed_widget in enumerate(equipment_widget.embed_levels):
            embed_widget.combo_box.currentIndexChanged.connect(embed_level_update(n, equipment_label))
        if equipment_widget.stones_json:
            equipment_widget.stone_level.combo_box.currentIndexChanged.connect(stone_update(equipment_label))
            for stone_attr in equipment_widget.stone_attrs:
                stone_attr.combo_box.currentIndexChanged.connect(stone_update(equipment_label))

    return equipments
