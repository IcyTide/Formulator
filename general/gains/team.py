from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from general.buffs.team import BUFFS, GAINS


class TeamGain(Gain):
    attributes: dict = {}

    def __init__(self, rate=100, stack=1, variety=None):
        super().__init__()
        self.rate = rate / 100
        self.stack = stack
        self.variety = variety

    def add_attribute(self, attribute: Attribute):
        if self.variety:
            attributes = self.attributes.get(self.variety, {})
        else:
            attributes = self.attributes
        for attr, value in attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) + int(value * self.rate * self.stack))

    def sub_attribute(self, attribute: Attribute):
        if self.variety:
            attributes = self.attributes.get(self.variety, {})
        else:
            attributes = self.attributes
        for attr, value in attributes.items():
            setattr(attribute, attr, getattr(attribute, attr) - int(value * self.rate * self.stack))


class TargetTeamGain(TeamGain):
    def add_attribute(self, attribute: Attribute):
        super().add_attribute(attribute.target)

    def sub_attribute(self, attribute: Attribute):
        super().sub_attribute(attribute.target)


def create_team_gain(buff: Buff, base_class, attributes):
    return buff.buff_name, type(buff.buff_name, (base_class,), dict(attributes=attributes))


TEAM_GAINS = [
    create_team_gain(GAINS[673], TeamGain, {k: v[-1] for k, v in GAINS[673].attributes.items()}),
    create_team_gain(BUFFS[20938], TeamGain, BUFFS[20938].attributes),
    create_team_gain(BUFFS[23573], TeamGain, BUFFS[23573].attributes),
    create_team_gain(GAINS[362], TeamGain, {k: v[-1] for k, v in GAINS[362].attributes.items()}),
    create_team_gain(GAINS[661], TargetTeamGain, {
        GAINS[661].buff_name: {k: v[-1] for k, v in GAINS[661].attributes.items()},
        GAINS[12717].buff_name: {k: v[-1] for k, v in GAINS[12717].attributes.items()}
    }),
    create_team_gain(GAINS[3465], TargetTeamGain, GAINS[3465].attributes),
    create_team_gain(BUFFS[23107], TeamGain, {k: (v + v / 2) / 2 for k, v in BUFFS[23107].attributes.items()}),
    create_team_gain(BUFFS[6363], TeamGain, {k: v[0] for k, v in BUFFS[6363].attributes.items()}),
    create_team_gain(GAINS[566], TargetTeamGain, {
        k: v[-1] * GAINS[566].max_stack for k, v in GAINS[566].attributes.items()
    }),
    create_team_gain(BUFFS[10208], TeamGain, BUFFS[10208].attributes),
    create_team_gain(GAINS[23305], TargetTeamGain, GAINS[23305].attributes),
    create_team_gain(BUFFS[24350], TeamGain, BUFFS[24350].attributes),
    create_team_gain(GAINS[378], TeamGain, {k: v[7 - 1] for k, v in GAINS[378].attributes.items()}),
    create_team_gain(GAINS[375], TeamGain, {k: v[5 - 1] for k, v in GAINS[375].attributes.items()}),
    create_team_gain(BUFFS[21236], TeamGain, BUFFS[21236].attributes),
    create_team_gain(BUFFS[24742], TeamGain, BUFFS[24742].attributes),
    create_team_gain(GAINS[4058], TargetTeamGain, {k: v[0] for k, v in GAINS[4058].attributes.items()}),
    create_team_gain(BUFFS[4246], TeamGain, {
        BUFFS[4246].buff_name: BUFFS[4246].attributes,
        BUFFS[9744].buff_name: BUFFS[9744].attributes
    }),
    create_team_gain(GAINS[7180], TeamGain, GAINS[7180].attributes),
    create_team_gain(GAINS[8248], TargetTeamGain, GAINS[8248].attributes),
    create_team_gain(BUFFS[8504], TeamGain, BUFFS[8504].attributes),
    create_team_gain(BUFFS[10031], TeamGain, BUFFS[10031].attributes),
    create_team_gain(BUFFS[23543], TeamGain, BUFFS[23543].attributes),
    create_team_gain(BUFFS[16911], TeamGain, BUFFS[16911].attributes),
    create_team_gain(BUFFS[11456], TeamGain, BUFFS[11456].attributes),
    create_team_gain(BUFFS[20877], TeamGain, BUFFS[20877].attributes)
]
TEAM_GAINS = {k: v for k, v in TEAM_GAINS}
