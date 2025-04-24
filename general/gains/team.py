from typing import Dict

from base.attribute import Attribute, TankAttribute
from base.gain import Gain
from general.buffs import GENERAL_BUFFS


class TeamGain(Gain):
    attributes: dict = {}
    buff_id: int

    def __init__(self, rate=100, stack=1):
        super().__init__()
        self.rate = rate / 100
        self.stack = stack

    def add_attribute(self, attribute: Attribute):
        if GENERAL_BUFFS[self.buff_id].activate:
            return
        for attr, value in self.attributes.items():
            attribute[attr] += int(value * self.rate * self.stack)

    def sub_attribute(self, attribute: Attribute):
        if GENERAL_BUFFS[self.buff_id].activate:
            return
        for attr, value in self.attributes.items():
            attribute[attr] -= int(value * self.rate * self.stack)


class TargetTeamGain(TeamGain):
    def add_attribute(self, attribute: Attribute):
        super().add_attribute(attribute.target)

    def sub_attribute(self, attribute: Attribute):
        super().sub_attribute(attribute.target)


class TankGain(Gain):
    buff_id: int

    def add_attribute(self, attribute: Attribute):
        if not isinstance(attribute, TankAttribute):
            return
        if self.buff_id:
            attribute.tank_buff_id = self.buff_id

    def sub_attribute(self, attribute: Attribute):
        if not isinstance(attribute, TankAttribute):
            return
        if self.buff_id:
            attribute.tank_buff_id = 0


def create_team_gain(buff_id: int, base_class, level=0, stack=1, func=None, gain_name=None):
    buff = GENERAL_BUFFS[buff_id]
    buff.buff_level, buff.buff_stack = level, stack
    if not gain_name:
        gain_name = buff.buff_name
    attributes = buff.attributes
    if func:
        attributes = {k: func(v) for k, v in attributes.items()}

    return gain_name, type(gain_name, (base_class,), dict(attributes=attributes, buff_id=buff_id))


TEAM_GAINS: Dict[str, type(TeamGain) | type(TankGain)] = {k: v for k, v in [
    create_team_gain(-673, TeamGain),
    create_team_gain(20938, TeamGain),
    create_team_gain(23573, TeamGain),
    create_team_gain(-362, TeamGain),
    create_team_gain(-661, TargetTeamGain),
    create_team_gain(-12717, TargetTeamGain),
    create_team_gain(-3465, TargetTeamGain),
    create_team_gain(23107, TeamGain, func=lambda x: (x + x / 2) / 2),
    create_team_gain(6363, TeamGain),
    create_team_gain(-566, TargetTeamGain),
    create_team_gain(6214, TeamGain),
    create_team_gain(29294, TeamGain),
    create_team_gain(24350, TeamGain),
    create_team_gain(-378, TeamGain, level=7),
    create_team_gain(-375, TeamGain, level=5),
    create_team_gain(29354, TeamGain, level=1),
    create_team_gain(24742, TeamGain),
    create_team_gain(-4058, TargetTeamGain, level=1),
    create_team_gain(4246, TeamGain, level=1),
    create_team_gain(4246, TeamGain, level=2),
    create_team_gain(-8248, TargetTeamGain),
    create_team_gain(8504, TeamGain),
    create_team_gain(10031, TeamGain),
    create_team_gain(23543, TeamGain),
    create_team_gain(16911, TeamGain),
    create_team_gain(11456, TeamGain),
    create_team_gain(20877, TeamGain),
    create_team_gain(20854, TeamGain),

    create_team_gain(-29938, TankGain),
    create_team_gain(-17885, TankGain),
]}
