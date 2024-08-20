from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from general.buffs.team import BUFFS


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
    create_team_gain(BUFFS[-673], TeamGain, BUFFS[-673].get_attributes(level=BUFFS[-673].max_level)),
    create_team_gain(BUFFS[20938], TeamGain, BUFFS[20938].attributes),
    create_team_gain(BUFFS[23573], TeamGain, BUFFS[23573].attributes),
    create_team_gain(BUFFS[-362], TeamGain, BUFFS[-362].get_attributes(level=BUFFS[-362].max_level)),
    create_team_gain(BUFFS[-661], TargetTeamGain, {
        BUFFS[-661].buff_name: BUFFS[-661].get_attributes(level=BUFFS[-661].max_level),
        BUFFS[-12717].buff_name: BUFFS[-12717].get_attributes(level=BUFFS[-12717].max_level)
    }),
    create_team_gain(BUFFS[-3465], TargetTeamGain, BUFFS[-3465].attributes),
    create_team_gain(BUFFS[23107], TeamGain, {k: (v + v / 2) / 2 for k, v in BUFFS[23107].attributes.items()}),
    create_team_gain(BUFFS[6363], TeamGain, BUFFS[6363].get_attributes()),
    create_team_gain(BUFFS[-566], TargetTeamGain,
                     BUFFS[-566].get_attributes(level=BUFFS[-566].max_level, stack=BUFFS[-566].max_stack)),
    create_team_gain(BUFFS[10208], TeamGain, BUFFS[10208].attributes),
    create_team_gain(BUFFS[-23305], TargetTeamGain, BUFFS[-23305].attributes),
    create_team_gain(BUFFS[24350], TeamGain, BUFFS[24350].attributes),
    create_team_gain(BUFFS[-378], TeamGain, BUFFS[-378].get_attributes(level=7)),
    create_team_gain(BUFFS[-375], TeamGain, BUFFS[-375].get_attributes(level=5)),
    create_team_gain(BUFFS[21236], TeamGain, BUFFS[21236].attributes),
    create_team_gain(BUFFS[24742], TeamGain, BUFFS[24742].attributes),
    create_team_gain(BUFFS[-4058], TargetTeamGain, BUFFS[-4058].get_attributes(level=1)),
    create_team_gain(BUFFS[4246], TeamGain, {
        BUFFS[4246].buff_name: BUFFS[4246].attributes,
        BUFFS[9744].buff_name: BUFFS[9744].attributes
    }),
    create_team_gain(BUFFS[-7180], TeamGain, BUFFS[-7180].attributes),
    create_team_gain(BUFFS[-8248], TargetTeamGain, BUFFS[-8248].attributes),
    create_team_gain(BUFFS[8504], TeamGain, BUFFS[8504].attributes),
    create_team_gain(BUFFS[10031], TeamGain, BUFFS[10031].attributes),
    create_team_gain(BUFFS[23543], TeamGain, BUFFS[23543].attributes),
    create_team_gain(BUFFS[16911], TeamGain, BUFFS[16911].attributes),
    create_team_gain(BUFFS[11456], TeamGain, BUFFS[11456].attributes),
    create_team_gain(BUFFS[20877], TeamGain, BUFFS[20877].get_attributes(stack=BUFFS[20877].max_stack))
]
TEAM_GAINS = {k: v for k, v in TEAM_GAINS}
