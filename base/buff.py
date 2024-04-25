from dataclasses import dataclass
from typing import Dict, List, Union

from base.attribute import Attribute
from base.skill import Skill

ATTR_DICT = Dict[str, Union[List[int], int]]


@dataclass
class Buff:
    buff_id: int
    buff_name: str
    buff_level: int = 0
    buff_stack: int = 1

    activate: bool = True

    gain_skills: Dict[int, ATTR_DICT] = None
    gain_attributes: ATTR_DICT = None

    SNAPSHOT_ATTRS = ["attack_power", "critical_strike", "critical_power", "strain", "damage_addition"]

    def __post_init__(self):
        if self.gain_skills is None:
            self.gain_skills = {}
        if self.gain_attributes is None:
            self.gain_attributes = {}

    @property
    def display_name(self):
        return f"{self.buff_name}#{self.buff_id}-{self.buff_level}-{self.buff_stack}"

    def level_value(self, value):
        if isinstance(value, list):
            return value[self.buff_level - 1]
        else:
            return value

    def add_all(self, attribute: Attribute, skill: Skill):
        for attr, value in self.gain_attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) + self.level_value(value) * self.buff_stack)
        for attr, value in self.gain_skills.get(skill.skill_id, {}).items():
            setattr(skill, attr, getattr(skill, attr) + self.level_value(value) * self.buff_stack)

    def add_dot(self, attribute: Attribute, skill: Skill, snapshot: bool = True):
        for attr, value in self.gain_attributes.items():
            if snapshot and any(snapshot_attr in attr for snapshot_attr in self.SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) + self.level_value(value) * self.buff_stack)
            elif not snapshot and all(snapshot_attr not in attr for snapshot_attr in self.SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) + self.level_value(value) * self.buff_stack)

        for attr, value in self.gain_skills.get(skill.skill_id, {}).items():
            if snapshot and any(snapshot_attr in attr for snapshot_attr in self.SNAPSHOT_ATTRS):
                setattr(skill, attr, getattr(skill, attr) + self.level_value(value) * self.buff_stack)
            elif not snapshot and all(snapshot_attr not in attr for snapshot_attr in self.SNAPSHOT_ATTRS):
                setattr(skill, attr, getattr(skill, attr) + self.level_value(value) * self.buff_stack)

    def sub_all(self, attribute: Attribute, skill: Skill):
        for attr, value in self.gain_attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) - self.level_value(value) * self.buff_stack)
        for attr, value in self.gain_skills.get(skill.skill_id, {}).items():
            setattr(skill, attr, getattr(skill, attr) - self.level_value(value) * self.buff_stack)

    def sub_dot(self, attribute: Attribute, skill: Skill, snapshot: bool = True):
        for attr, value in self.gain_attributes.items():
            if snapshot and any(snapshot_attr in attr for snapshot_attr in self.SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) - self.level_value(value) * self.buff_stack)
            elif not snapshot and all(snapshot_attr not in attr for snapshot_attr in self.SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) - self.level_value(value) * self.buff_stack)
        for attr, value in self.gain_skills.get(skill.skill_id, {}).items():
            if snapshot and any(snapshot_attr in attr for snapshot_attr in self.SNAPSHOT_ATTRS):
                setattr(skill, attr, getattr(skill, attr) - self.level_value(value) * self.buff_stack)
            elif not snapshot and all(snapshot_attr not in attr for snapshot_attr in self.SNAPSHOT_ATTRS):
                setattr(skill, attr, getattr(skill, attr) - self.level_value(value) * self.buff_stack)
