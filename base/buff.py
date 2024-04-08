from dataclasses import dataclass
from typing import Dict, List, Union, Tuple

from base.attribute import Attribute
from base.skill import Skill

ATTR_DICT = Dict[str, Union[List[int], int]]


@dataclass
class Buff:
    buff_id: int
    buff_name: str
    buff_level: int = 0

    stack: int = 1

    gain_skills: Dict[str, ATTR_DICT] = None
    gain_attributes: ATTR_DICT = None

    def __post_init__(self):
        self.gain_skills = {}
        self.gain_attributes = {}

    def __radd__(self, other: Tuple[Attribute, Dict[str, Skill]]):
        attribute, skills = other
        for skill_id, gain in self.gain_skills.items():
            skill = skills[skill_id]
            for attr, value in gain.items():
                setattr(skill, attr, getattr(skill, attr) + value)
        for attr, value in self.gain_attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) + value)
        return attribute, skills

    def __rsub__(self, other: Tuple[Attribute, Dict[str, Skill]]):
        attribute, skills = other
        for skill_id, gain in self.gain_skills.items():
            skill = skills[skill_id]
            for attr, value in gain.items():
                setattr(skill, attr, getattr(skill, attr) - value)
        for attr, value in self.gain_attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) - value)
        return attribute, skills
