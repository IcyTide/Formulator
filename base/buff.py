from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, Union

from assets.buffs import BUFFS

ATTR_DICT = Dict[str, Union[List[int], int]]


class BaseBuff:
    DOT_SNAPSHOT_ATTRS = [
        "attack_power", "critical_strike", "critical_power", "surplus", "strain", "damage_addition", "pve_addition"
    ]
    PET_SNAPSHOT_ATTRS = [
        "attack_power", "critical_power", "overcome", "surplus", "strain", "damage_addition", "pve_addition"
    ]
    buff_id: int = 0
    buff_level: int = 0
    _buff_stack: int = 1
    alias_name: str = ""

    max_level: int = 1
    stackable: bool = True
    _buff_name: List[str] = None

    _max_stack: List[int] = None
    interval: int = 0

    def set_asset(self, attrs):
        for attr, value in BUFFS.get(abs(self.buff_id), {}).items():
            setattr(self, attr, value)
        for attr, value in attrs.items():
            setattr(self, attr, value)

    @property
    def display_name(self):
        return f"{self.buff_name}#{self.buff_id}-{self.buff_level}-{self.buff_stack}"

    @property
    def buff_stack(self):
        return self._buff_stack if self.stackable else 1

    @buff_stack.setter
    def buff_stack(self, buff_stack):
        self._buff_stack = buff_stack

    @property
    def buff_name(self):
        if not self._buff_name:
            return ""
        elif self.buff_level > len(self._buff_name):
            return self._buff_name[-1]
        else:
            return self._buff_name[self.buff_level - 1]

    @buff_name.setter
    def buff_name(self, buff_name):
        if isinstance(buff_name, list):
            self._buff_name = buff_name
        else:
            self._buff_name = [buff_name]

    @property
    def max_stack(self):
        if not self._max_stack:
            return 1
        elif self.buff_level > len(self._max_stack):
            return self._max_stack[-1]
        else:
            return self._max_stack[self.buff_level - 1]

    @max_stack.setter
    def max_stack(self, max_stack):
        if isinstance(max_stack, list):
            self._max_stack = max_stack
        else:
            self._max_stack = [max_stack]

    def __gt__(self, other: "BaseBuff"):
        if abs(self.buff_id) > abs(other.buff_id):
            return True
        if abs(self.buff_id) < abs(other.buff_id):
            return False
        if self.buff_level > other.buff_level:
            return True
        return False


@dataclass
class Buff(BaseBuff):
    buff_id: int

    begin_frame_shift: int = 0
    end_frame_shift: int = 0
    unique: bool = True
    activate: bool = True

    _recipes: List[dict] = None
    _attributes: List[dict] = None

    begin_effects: list = None
    begin_buffs: dict = None
    begin_target_buffs: dict = None
    end_effects: list = None
    end_buffs: dict = None
    end_target_buffs: dict = None

    def __post_init__(self):
        if self.recipes is None:
            self.recipes = [{}]
        if self.attributes is None:
            self.attributes = [{}]
        if not self.begin_buffs:
            self.begin_buffs = {}
        if not self.begin_target_buffs:
            self.begin_target_buffs = {}
        if not self.begin_effects:
            self.begin_effects = []
        if not self.end_buffs:
            self.end_buffs = {}
        if not self.end_target_buffs:
            self.end_target_buffs = {}
        if not self.end_effects:
            self.end_effects = []

    @property
    def all_attributes(self):
        if not self._attributes:
            return [{}]
        return self._attributes

    def get_attributes(self, level=1, stack=1, weights: list = None):
        if weights:
            origin_level = self.buff_level
            attributes = defaultdict(int)
            total_weight = sum(weights)
            for level, weight in zip(range(self.max_level), weights):
                self.buff_level = level
                for k, v in self.attributes.items():
                    attributes[k] += v * weight / total_weight
            attributes = {k: int(v) for k, v in attributes.items()}
            self.buff_level = origin_level
        else:
            self.buff_level, origin_level = level, self.buff_level
            self.buff_stack, origin_stack = stack, self.buff_stack
            attributes = self.attributes
            self.buff_level = origin_level
            self.buff_stack = origin_stack
        return attributes

    @property
    def attributes(self):
        if not self._attributes:
            return {}
        if self.buff_level > len(self._attributes):
            attributes = self._attributes[-1]
        else:
            attributes = self._attributes[self.buff_level - 1]
        return {k: int(v * self.buff_stack) for k, v in attributes.items()}

    @attributes.setter
    def attributes(self, attributes):
        if isinstance(attributes, list):
            self._attributes = attributes
        else:
            self._attributes = [attributes]

    @property
    def recipes(self):
        if not self._recipes:
            return {}
        elif self.buff_level > len(self._recipes):
            return self._recipes[-1]
        else:
            return self._recipes[self.buff_level - 1]

    @recipes.setter
    def recipes(self, recipes):
        if recipes and isinstance(recipes, list):
            self._recipes = recipes
        else:
            self._recipes = [recipes]

    def begin(self, parser):
        for buff_id, buff_levels in self.begin_buffs.items():
            for buff_level, buff_stack in buff_levels.items():
                parser.refresh_buff(buff_id, buff_level, buff_stack)
        for buff_id, buff_levels in self.begin_target_buffs.items():
            for buff_level, buff_stack in buff_levels.items():
                parser.refresh_target_buff(buff_id, buff_level, buff_stack)
        for effect in self.begin_effects:
            effect(parser)

    def end(self, parser):
        for buff_id, buff_levels in self.end_buffs.items():
            for buff_level, buff_stack in buff_levels.items():
                parser.refresh_buff(buff_id, buff_level, buff_stack)
        for buff_id, buff_levels in self.end_target_buffs.items():
            for buff_level, buff_stack in buff_levels.items():
                parser.refresh_target_buff(buff_id, buff_level, buff_stack)
        for effect in self.end_effects:
            effect(parser)


class CustomBuff(Buff):
    pass
