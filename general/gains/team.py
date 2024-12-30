from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from general.buffs import GENERAL_BUFFS


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
    create_team_gain(
        GENERAL_BUFFS[-673], TeamGain, GENERAL_BUFFS[-673].get_attributes(level=GENERAL_BUFFS[-673].max_level)
    ),
    create_team_gain(GENERAL_BUFFS[20938], TeamGain, GENERAL_BUFFS[20938].attributes),
    create_team_gain(GENERAL_BUFFS[23573], TeamGain, GENERAL_BUFFS[23573].attributes),
    create_team_gain(
        GENERAL_BUFFS[-362], TeamGain, GENERAL_BUFFS[-362].get_attributes(level=GENERAL_BUFFS[-362].max_level)
    ),
    create_team_gain(
        GENERAL_BUFFS[-661], TargetTeamGain, {
            GENERAL_BUFFS[-661].buff_name: GENERAL_BUFFS[-661].get_attributes(level=GENERAL_BUFFS[-661].max_level),
            GENERAL_BUFFS[-12717].buff_name: GENERAL_BUFFS[-12717].get_attributes(level=GENERAL_BUFFS[-12717].max_level)
        }
    ),
    create_team_gain(GENERAL_BUFFS[-3465], TargetTeamGain, GENERAL_BUFFS[-3465].attributes),
    create_team_gain(
        GENERAL_BUFFS[23107], TeamGain, {k: (v + v / 2) / 2 for k, v in GENERAL_BUFFS[23107].attributes.items()}
    ),
    create_team_gain(GENERAL_BUFFS[6363], TeamGain, GENERAL_BUFFS[6363].get_attributes()),
    create_team_gain(
        GENERAL_BUFFS[-566], TargetTeamGain, GENERAL_BUFFS[-566].get_attributes(level=GENERAL_BUFFS[-566].max_level)
    ),
    create_team_gain(GENERAL_BUFFS[10208], TeamGain, GENERAL_BUFFS[10208].attributes),
    create_team_gain(GENERAL_BUFFS[29294], TeamGain, GENERAL_BUFFS[29294].attributes),
    create_team_gain(GENERAL_BUFFS[24350], TeamGain, GENERAL_BUFFS[24350].attributes),
    create_team_gain(GENERAL_BUFFS[-378], TeamGain, GENERAL_BUFFS[-378].get_attributes(level=7)),
    create_team_gain(GENERAL_BUFFS[-375], TeamGain, GENERAL_BUFFS[-375].get_attributes(level=5)),
    create_team_gain(GENERAL_BUFFS[29354], TeamGain, GENERAL_BUFFS[29354].get_attributes(level=1)),
    create_team_gain(GENERAL_BUFFS[24742], TeamGain, GENERAL_BUFFS[24742].attributes),
    create_team_gain(GENERAL_BUFFS[-4058], TargetTeamGain, GENERAL_BUFFS[-4058].get_attributes(level=1)),
    create_team_gain(GENERAL_BUFFS[4246], TeamGain, {
        GENERAL_BUFFS[4246].buff_name: GENERAL_BUFFS[4246].attributes,
        GENERAL_BUFFS[9744].buff_name: GENERAL_BUFFS[9744].attributes
    }),
    create_team_gain(GENERAL_BUFFS[-7180], TeamGain, GENERAL_BUFFS[-7180].attributes),
    create_team_gain(GENERAL_BUFFS[-8248], TargetTeamGain, GENERAL_BUFFS[-8248].attributes),
    create_team_gain(GENERAL_BUFFS[8504], TeamGain, GENERAL_BUFFS[8504].attributes),
    create_team_gain(GENERAL_BUFFS[10031], TeamGain, GENERAL_BUFFS[10031].attributes),
    create_team_gain(GENERAL_BUFFS[23543], TeamGain, GENERAL_BUFFS[23543].attributes),
    create_team_gain(GENERAL_BUFFS[16911], TeamGain, GENERAL_BUFFS[16911].attributes),
    create_team_gain(GENERAL_BUFFS[11456], TeamGain, GENERAL_BUFFS[11456].attributes),
    create_team_gain(
        GENERAL_BUFFS[20877], TeamGain, GENERAL_BUFFS[20877].get_attributes(stack=GENERAL_BUFFS[20877].max_stack)
    ),
    create_team_gain(GENERAL_BUFFS[20854], TeamGain, GENERAL_BUFFS[20854].attributes)
]
TEAM_GAINS = {k: v for k, v in TEAM_GAINS}
