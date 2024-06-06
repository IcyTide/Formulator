from typing import List, Dict

from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from base.skill import Skill


class Talent(Gain):
    gains: List[Gain]

    def __init__(self, name: str = None, gains: List[Gain] = None):
        super().__init__(name=name)
        if gains:
            self.gains = gains
        else:
            self.gains = []

    def add(self, attribute: Attribute, skills: Dict[int, Skill], buffs: Dict[int, Buff]):
        for gain in self.gains:
            gain.add(attribute, skills, buffs)

    def sub(self, attribute: Attribute, skills: Dict[int, Skill], buffs: Dict[int, Buff]):
        for gain in self.gains:
            gain.sub(attribute, skills, buffs)
