from typing import Union, Dict

from base.attribute import Attribute
from base.skill import Skill


class Gain:
    def __init__(self, gain_name):
        self.gain_name = gain_name

    def add(self, other):
        pass

    def sub(self, other):
        pass

    def __radd__(self, other: Union[Attribute, Dict[int, Skill]]):
        self.add(other)
        return other

    def __rsub__(self, other: Union[Attribute, Dict[int, Skill]]):
        self.sub(other)
        return other
