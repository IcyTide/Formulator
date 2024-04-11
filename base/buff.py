from dataclasses import dataclass
from typing import Dict, List, Union

from base.attribute import Attribute
from base.skill import Skill

ATTR_DICT = Dict[str, Union[List[int], int]]


@dataclass
class Buff:
    buff_id: int = 0
    buff_name: str = ""
    buff_level: int = 0
    buff_stack: int = 1

    gain_skills: Dict[int, ATTR_DICT] = None
    gain_attributes: ATTR_DICT = None

    def __post_init__(self):
        if self.gain_skills is None:
            self.gain_skills = {}
        if self.gain_attributes is None:
            self.gain_attributes = {}

    @property
    def display_name(self):
        return f"{self.buff_name}/{self.buff_id}-{self.buff_level}-{self.buff_stack}"

    def __radd__(self, other: Union[Attribute, Dict[int, Skill]]):
        if isinstance(other, Attribute):
            for attr, value in self.gain_attributes.items():
                setattr(other, attr, getattr(other, attr) + value * self.buff_stack)
        else:
            for skill_id, gain in self.gain_skills.items():
                skill = other[skill_id]
                for attr, value in gain.items():
                    if isinstance(value, list):
                        setattr(skill, attr, value)
                    else:
                        setattr(skill, attr, getattr(skill, attr) + value * self.buff_stack)

        return other

    def __rsub__(self, other: Union[Attribute, Dict[int, Skill]]):
        if isinstance(other, Attribute):
            for attr, value in self.gain_attributes.items():
                setattr(other, attr, getattr(other, attr) - value * self.buff_stack)
        else:
            for skill_id, gain in self.gain_skills.items():
                skill = other[skill_id]
                for attr, value in gain.items():
                    if isinstance(value, list):
                        setattr(skill, attr, value)
                    else:
                        value *= self.buff_stack
                        setattr(skill, attr, getattr(skill, attr) + value)
        return other

