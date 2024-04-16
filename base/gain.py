from typing import Union, Dict

from base.attribute import Attribute
from base.buff import Buff
from base.skill import Skill


class Gain:
    def __init__(self, gain_name="NotImplemented"):
        self.gain_name = gain_name

    def add_attribute(self, attribute: Attribute):
        pass

    def add_skills(self, skills: Dict[int, Skill]):
        pass

    def add_buffs(self, buffs: Dict[int, Buff]):
        pass

    def add(self, attribute: Attribute, skills: Dict[int, Skill], buffs: Dict[int, Buff]):
        self.add_attribute(attribute)
        self.add_skills(skills)
        self.add_buffs(buffs)

    def sub_attribute(self, attribute: Attribute):
        pass

    def sub_skills(self, skills: Dict[int, Skill]):
        pass

    def sub_buffs(self, buffs: Dict[int, Buff]):
        pass

    def sub(self, attribute: Attribute, skills: Dict[int, Skill], buffs: Dict[int, Buff]):
        self.sub_attribute(attribute)
        self.sub_skills(skills)
        self.sub_buffs(buffs)
