from collections import defaultdict
from typing import Dict, List, Union, Tuple

import gradio as gr

from general.gains.equipment import EQUIPMENT_GAINS
from gr.components.equipments import EquipmentsComponent
from assets.constant import POSITION_MAP, STONES_POSITIONS, EMBED_POSITIONS
from assets.constant import ATTR_TYPE_TRANSLATE
from assets.constant import STRENGTH_COF, EMBED_COF, MAX_STRENGTH_LEVEL, MAX_EMBED_LEVEL

FULL_SPACE = "\u3000"


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
    special_enchant: Union[int | Tuple[int, int]]
    special_enchant_gain: List[int | List[int]]
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
        return "\n".join(
            ATTR_TYPE_TRANSLATE[k].ljust(10, FULL_SPACE) + str(v) for k, v in self.base_attr.items()
        )

    @property
    def magic_attr_content(self):
        if strength_attr := self.strength_attr:
            return "\n".join(
                ATTR_TYPE_TRANSLATE[k].ljust(10, FULL_SPACE) + f"{v}(+{strength_attr[k]})"
                for k, v in self.magic_attr.items()
            )
        else:
            return "\n".join(
                ATTR_TYPE_TRANSLATE[k].ljust(10, FULL_SPACE) + str(v) for k, v in self.magic_attr.items()
            )

    @property
    def embed_attr_content(self):
        return "\n".join(
            ATTR_TYPE_TRANSLATE[k].ljust(10, FULL_SPACE) + str(v) for k, v in self.embed_attr.items()
        )


class Equipments:
    def __init__(self):
        self.equipments = {label: Equipment(label) for label in POSITION_MAP}

    def __getitem__(self, item) -> Equipment:
        return self.equipments[item]

    @property
    def attrs(self):
        final_attrs = defaultdict(int)
        set_count = {}
        set_effect = {}
        for equipment in self.equipments.values():
            if not equipment.name:
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


def equipments_script(equipments_component: EquipmentsComponent):
    equipments = Equipments()

    def equipment_changed(label):
        def inner(equipment_name):
            equipment = equipments[label]
            component = equipments_component[label]
            if not equipment_name:
                equipment.clear()
                return {
                    component.equipment: gr.update(value=""),
                    component.detail: gr.update(visible=False)
                }

            equipment_update = {}
            if equipment.strength_level == equipment.max_strength:
                max_strength = True
            else:
                max_strength = False

            equipment.name = equipment_name
            equipment_detail = component.equipment_json[equipment_name]
            for k, v in equipment_detail.items():
                setattr(equipment, k, v)

            if equipment.base:
                equipment_update[component.base_attr] = gr.update(
                    value=equipment.base_attr_content, visible=True
                )
            else:
                equipment_update[component.base_attr] = gr.update(visible=False)

            if isinstance(equipment.special_enchant, list):
                equipment.special_enchant = tuple(equipment.special_enchant)

            if equipment.special_enchant:
                equipment_update[component.special_enchant] = gr.update(
                    label=EQUIPMENT_GAINS[equipment.special_enchant].gain_name
                )

            if max_strength:
                equipment.strength_level = equipment.max_strength

            equipment_update[component.strength_level] = gr.update(
                choices=list(range(equipment.max_strength + 1)), value=equipment.strength_level
            )
            equipment_update[component.magic_attr] = gr.update(
                value=equipment.magic_attr_content, visible=True
            )

            if equipment.embed:
                for i, attr in enumerate(equipment.embed):
                    embed_level_component = component.embed_levels[i]
                    equipment_update[embed_level_component] = gr.update(
                        label=f"镶嵌等级-{ATTR_TYPE_TRANSLATE[attr]}", visible=True
                    )
                equipment_update[component.embed_attr] = gr.update(
                    value=equipment.embed_attr_content, visible=True
                )
            else:
                for embed_level_component in component.embed_levels:
                    equipment_update[embed_level_component] = gr.update(visible=False)

            equipment_update[component.detail] = gr.update(visible=True)
            return equipment_update

        return inner

    def enchant_changed(label):
        def inner(enchant_name):
            equipment = equipments[label]
            component = equipments_component[label]
            if enchant_name:
                enchant_detail = component.enchant_json[enchant_name]
                equipment.enchant.name = enchant_name
                for k, v in enchant_detail.items():
                    setattr(equipment.enchant, k, v)
            else:
                equipment.enchant.clear()

        return inner

    def special_enchant_changed(label):
        def inner(special_enchant_check):
            equipment = equipments[label]
            component = equipments_component[label]
            if component.special_enchant and special_enchant_check:
                equipment.special_enchant_gain = [equipment.special_enchant]
            else:
                equipment.special_enchant_gain = []

        return inner

    def strength_level_changed(label):
        def inner(strength_level):
            equipment = equipments[label]
            equipment.strength_level = strength_level
            if magic_attr_content := equipment.magic_attr_content:
                return gr.update(value=magic_attr_content, visible=True)
            else:
                return gr.update(visible=False)

        return inner

    def embed_level_changed(i, label):
        def inner(embed_level):
            equipment = equipments[label]
            equipment.embed_levels[i] = embed_level
            if embed_attr_content := equipment.embed_attr_content:
                return gr.update(value=embed_attr_content, visible=True)
            else:
                return gr.update(visible=False)

        return inner

    def stone_changed(label):
        def inner(stone_level, *stone_attrs):
            equipment = equipments[label]
            component = equipments_component[label]

            current = component.stones_json
            i = 0
            for stone_attr in stone_attrs:
                if stone_attr in current:
                    current = current[stone_attr]
                    i += 1
                else:
                    break

            stone_update = {component.stone_level: gr.update()}
            stone_level = str(stone_level)
            if stone_level in current:
                for k, v in current[stone_level].items():
                    setattr(equipment.stone, k, v)
                return stone_update

            equipment.stone = Stone()
            stone_update[component.stone_attrs[i]] = gr.Dropdown(
                choices=list(current)
            )

            i += 1
            while i < len(stone_attrs):
                stone_update[component.stone_attrs[i]] = gr.Dropdown(
                    choices=[]
                )
                i += 1
            return stone_update

        return inner

    for equipment_label, equipment_component in equipments_component.items():
        equipment_component.equipment.change(
            equipment_changed(equipment_label), equipment_component.equipment,
            [equipment_component.detail, equipment_component.special_enchant,
             equipment_component.base_attr, equipment_component.magic_attr, equipment_component.embed_attr,
             equipment_component.strength_level, *equipment_component.embed_levels]
        )
        equipment_component.enchant.change(enchant_changed(equipment_label), equipment_component.enchant)
        equipment_component.special_enchant.change(
            special_enchant_changed(equipment_label), equipment_component.special_enchant
        )
        equipment_component.strength_level.change(
            strength_level_changed(equipment_label), equipment_component.strength_level, equipment_component.magic_attr
        )
        for n, embed_component in enumerate(equipment_component.embed_levels):
            embed_component.change(
                embed_level_changed(n, equipment_label), embed_component, equipment_component.embed_attr)
        stone_components = [equipment_component.stone_level] + equipment_component.stone_attrs
        equipment_component.stone_level.change(
            stone_changed(equipment_label), stone_components, stone_components
        )
        for stone_attr_component in equipment_component.stone_attrs:
            stone_attr_component.change(
                stone_changed(equipment_label), stone_components, stone_components
            )

    return equipments
