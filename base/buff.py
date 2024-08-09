from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, Union

from base.attribute import Attribute
from base.skill import Skill

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
    max_level: int = 1
    stackable: bool = True
    _buff_name: List[str] = None

    _max_stack: List[int] = None
    interval: int = 0

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


@dataclass
class Buff(BaseBuff):
    buff_id: int

    frame_shift: int = 0
    unique: bool = True
    activate: bool = True

    _gains: List[list] = None
    _attributes: List[dict] = None

    begin_effects: list = None
    begin_buffs: dict = None
    begin_target_buffs: dict = None
    end_effects: list = None
    end_buffs: dict = None
    end_target_buffs: dict = None

    def __post_init__(self):
        if self.gains is None:
            self.gains = [[]]
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
        return {k: v * self.buff_stack for k, v in attributes.items()}

    @attributes.setter
    def attributes(self, attributes):
        if isinstance(attributes, list):
            self._attributes = attributes
        else:
            self._attributes = [attributes]

    @property
    def gains(self):
        if not self._gains:
            return []
        elif self.buff_level > len(self._gains):
            return self._gains[-1]
        else:
            return self._gains[self.buff_level - 1]

    @gains.setter
    def gains(self, gains):
        if gains and isinstance(gains[0], list):
            self._gains = gains
        else:
            self._gains = [gains]

    def begin(self, parser):
        for (buff_id, buff_level), buff_stack in self.begin_buffs.items():
            buff_level = buff_level if buff_level else self.buff_level
            parser.refresh_buff(buff_id, buff_level, buff_stack)
        for (buff_id, buff_level), buff_stack in self.begin_target_buffs.items():
            buff_level = buff_level if buff_level else self.buff_level
            parser.refresh_target_buff(buff_id, buff_level, buff_stack)
        for effect in self.begin_effects:
            effect(parser)

    def end(self, parser):
        for (buff_id, buff_level), buff_stack in self.end_buffs.items():
            buff_level = buff_level if buff_level else self.buff_level
            parser.refresh_buff(buff_id, buff_level, buff_stack)
        for (buff_id, buff_level), buff_stack in self.end_target_buffs.items():
            buff_level = buff_level if buff_level else self.buff_level
            parser.refresh_target_buff(buff_id, buff_level, buff_stack)
        for effect in self.end_effects:
            effect(parser)

    def add_all(self, attribute: Attribute, skill: Skill):
        return_tag = False
        for attr, value in self.attributes.items():
            if not value:
                continue
            setattr(attribute, attr, getattr(attribute, attr) + value)
            return_tag = True
        gain_tuple = (attribute, {skill.skill_id: skill}, {}, {})
        for gain in self.gains:
            if not gain:
                continue
            if gain.add(*gain_tuple):
                return_tag = True

        return return_tag

    def add_dot(self, attribute: Attribute, skill: Skill, snapshot: bool = True):
        return_tag = False
        for attr, value in self.attributes.items():
            if not value:
                continue
            if snapshot and any(snapshot_attr in attr for snapshot_attr in self.DOT_SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) + value)
                return_tag = True
            if not snapshot and all(snapshot_attr not in attr for snapshot_attr in self.DOT_SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) + value)
                return_tag = True
        if snapshot:
            gain_tuple = (attribute, {skill.skill_id: skill}, {}, {})
            for gain in self.gains:
                if gain.add(*gain_tuple):
                    return_tag = True

        return return_tag

    def add_pet(self, attribute: Attribute, skill: Skill):
        return_tag = False
        for attr, value in self.attributes.items():
            if not value:
                continue
            if any(snapshot_attr in attr for snapshot_attr in self.PET_SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) + value)
                return_tag = True
        gain_tuple = (attribute, {skill.skill_id: skill}, {}, {})
        for gain in self.gains:
            if gain.add(*gain_tuple):
                return_tag = True

        return return_tag

    def sub_all(self, attribute: Attribute, skill: Skill):
        for attr, value in self.attributes.items():
            if not value:
                continue
            setattr(attribute, attr, getattr(attribute, attr) - value)
        gain_tuple = (attribute, {skill.skill_id: skill}, {}, {})
        for gain in self.gains:
            gain.sub(*gain_tuple)

    def sub_dot(self, attribute: Attribute, skill: Skill, snapshot: bool = True):
        for attr, value in self.attributes.items():
            if not value:
                continue
            if snapshot and any(snapshot_attr in attr for snapshot_attr in self.DOT_SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) - value)
            if not snapshot and all(snapshot_attr not in attr for snapshot_attr in self.DOT_SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) - value)
        if snapshot:
            gain_tuple = (attribute, {skill.skill_id: skill}, {}, {})
            for gain in self.gains:
                gain.sub(*gain_tuple)

    def sub_pet(self, attribute: Attribute, skill: Skill):
        for attr, value in self.attributes.items():
            if not value:
                continue
            if any(snapshot_attr in attr for snapshot_attr in self.PET_SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) - value)
        gain_tuple = (attribute, {skill.skill_id: skill}, {}, {})
        for gain in self.gains:
            gain.sub(*gain_tuple)


class TargetBuff(Buff):
    def add_all(self, attribute: Attribute, skill: Skill):
        return super().add_all(attribute.target, skill)

    def sub_all(self, attribute: Attribute, skill: Skill):
        super().sub_all(attribute.target, skill)


class CustomBuff(Buff):
    pass
