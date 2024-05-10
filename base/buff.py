from dataclasses import dataclass
from typing import Dict, List, Union

from base.attribute import Attribute
from base.skill import Skill

ATTR_DICT = Dict[str, Union[List[int], int]]


@dataclass
class Buff:
    buff_id: int
    _buff_name: Union[List[str], str] = ""
    buff_level: int = 0
    buff_stack: int = 1

    frame_shift: int = 0
    second_shift: int = 0
    activate: bool = True

    max_stack: int = 1

    gain_skills: Dict[int, ATTR_DICT] = None
    gain_attributes: ATTR_DICT = None

    SNAPSHOT_ATTRS = ["attack_power", "critical_strike", "critical_power", "strain", "damage_addition", "pve_addition"]

    def __post_init__(self):
        if self.gain_skills is None:
            self.gain_skills = {}
        if self.gain_attributes is None:
            self.gain_attributes = {}

    @property
    def shifted(self):
        return self.second_shift or self.frame_shift

    @property
    def buff_name(self):
        if not isinstance(self._buff_name, list):
            return ""

        if self.buff_level > len(self._buff_name):
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
    def display_name(self):
        return f"{self.buff_name}#{self.buff_id}-{self.buff_level}-{self.buff_stack}"

    def value(self, values, stackable):
        if isinstance(values, list):
            value = values[self.buff_level - 1]
        else:
            value = values

        if stackable:
            value = value * self.buff_stack

        return value

    def attribute_value(self, values):
        return self.value(values, True)

    def skill_value(self, values):
        return self.value(values, False)

    def add_all(self, attribute: Attribute, skill: Skill):
        for attr, values in self.gain_attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) + self.attribute_value(values))
        for attr, values in self.gain_skills.get(skill.skill_id, {}).items():
            value = self.skill_value(values)
            if isinstance(value, float):
                setattr(skill, attr, getattr(skill, attr) * value)
            else:
                setattr(skill, attr, getattr(skill, attr) + value)

    def add_dot(self, attribute: Attribute, skill: Skill, snapshot: bool = True):
        return_tag = False
        for attr, values in self.gain_attributes.items():
            if snapshot and any(snapshot_attr in attr for snapshot_attr in self.SNAPSHOT_ATTRS):
                return_tag = True
                setattr(attribute, attr, getattr(attribute, attr) + self.attribute_value(values))
            elif not snapshot and all(snapshot_attr not in attr for snapshot_attr in self.SNAPSHOT_ATTRS):
                return_tag = True
                setattr(attribute, attr, getattr(attribute, attr) + self.attribute_value(values))
        for attr, values in self.gain_skills.get(skill.skill_id, {}).items():
            value = self.skill_value(values)
            if snapshot and any(snapshot_attr in attr for snapshot_attr in self.SNAPSHOT_ATTRS):
                return_tag = True
                if isinstance(value, float):
                    setattr(skill, attr, getattr(skill, attr) * value)
                else:
                    setattr(skill, attr, getattr(skill, attr) + value)
            elif not snapshot and all(snapshot_attr not in attr for snapshot_attr in self.SNAPSHOT_ATTRS):
                return_tag = True
                if isinstance(value, float):
                    setattr(skill, attr, getattr(skill, attr) * value)
                else:
                    setattr(skill, attr, getattr(skill, attr) + value)

        return return_tag

    def sub_all(self, attribute: Attribute, skill: Skill):
        for attr, values in self.gain_attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) - self.attribute_value(values))
        for attr, values in self.gain_skills.get(skill.skill_id, {}).items():
            value = self.skill_value(values)
            if isinstance(value, float):
                setattr(skill, attr, getattr(skill, attr) / value)
            else:
                setattr(skill, attr, getattr(skill, attr) - value)

    def sub_dot(self, attribute: Attribute, skill: Skill, snapshot: bool = True):
        for attr, values in self.gain_attributes.items():
            if snapshot and any(snapshot_attr in attr for snapshot_attr in self.SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) - self.attribute_value(values))
            elif not snapshot and all(snapshot_attr not in attr for snapshot_attr in self.SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) - self.attribute_value(values))
        for attr, values in self.gain_skills.get(skill.skill_id, {}).items():
            value = self.skill_value(values)
            if snapshot and any(snapshot_attr in attr for snapshot_attr in self.SNAPSHOT_ATTRS):
                if isinstance(value, float):
                    setattr(skill, attr, getattr(skill, attr) / value)
                else:
                    setattr(skill, attr, getattr(skill, attr) - value)
            elif not snapshot and all(snapshot_attr not in attr for snapshot_attr in self.SNAPSHOT_ATTRS):
                if isinstance(value, float):
                    setattr(skill, attr, getattr(skill, attr) / value)
                else:
                    setattr(skill, attr, getattr(skill, attr) - value)
