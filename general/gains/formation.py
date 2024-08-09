from typing import List

from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from general.buffs.formation import BUFFS, GAINS


class FormationGain(Gain):
    attributes: List[dict] = None
    rates: List[float] = None

    def __init__(self, rates):
        super().__init__()
        self.rates = [1] + [rate / 100 for rate in rates]

    def add_attribute(self, attribute: Attribute):
        for attributes, rate in zip(self.attributes, self.rates):
            for attr, value in attributes.items():
                setattr(attribute, attr, getattr(attribute, attr) + int(value * rate))

    def sub_attribute(self, attribute: Attribute):
        for attributes, rate in zip(self.attributes, self.rates):
            for attr, value in attributes.items():
                setattr(attribute, attr, getattr(attribute, attr) - int(value * rate))


def create_formation_gain(buff: Buff, attributes: List[dict]):
    return buff.buff_name, type(buff.buff_name, (FormationGain,), dict(attributes=attributes))


FORMATION_GAINS = [
    create_formation_gain(GAINS[918], [
        GAINS[919].get_attributes(level=6),
        {},
        BUFFS[920].get_attributes(stack=BUFFS[920].max_stack),
        BUFFS[940].attributes
    ]),
    create_formation_gain(GAINS[929], [
        GAINS[919].get_attributes(level=6),
        BUFFS[935].get_attributes(stack=BUFFS[935].max_stack),
        BUFFS[936].attributes,
        BUFFS[940].attributes
    ]),
    create_formation_gain(GAINS[933], [
        GAINS[934].get_attributes(level=6),
        BUFFS[937].attributes,
        {},
        {}
    ]),
    create_formation_gain(GAINS[931], [
        GAINS[938].get_attributes(level=6),
        {},
        BUFFS[943].get_attributes(stack=BUFFS[943].max_stack),
        BUFFS[949].attributes
    ]),
    create_formation_gain(GAINS[946], [
        GAINS[947].get_attributes(level=6),
        {},
        BUFFS[950].get_attributes(stack=BUFFS[950].max_stack),
        BUFFS[953].attributes
    ]),
    create_formation_gain(GAINS[951], [
        GAINS[952].get_attributes(level=6),
        BUFFS[954].attributes,
        BUFFS[955].attributes,
        BUFFS[956].attributes
    ]),
    create_formation_gain(GAINS[1923], [
        GAINS[1924].get_attributes(level=6),
        {},
        {},
        BUFFS[1926].attributes
    ]),
    create_formation_gain(GAINS[2511], [
        GAINS[2512].get_attributes(level=6),
        BUFFS[2513].attributes,
        BUFFS[2514].attributes,
        BUFFS[2510].attributes
    ]),
    create_formation_gain(GAINS[3302], [
        GAINS[3306].get_attributes(level=6),
        {},
        BUFFS[3308].attributes,
        BUFFS[3309].attributes
    ]),
    create_formation_gain(GAINS[3303], [
        GAINS[3307].get_attributes(level=6),
        {},
        BUFFS[3310].attributes,
        {}
    ]),
    create_formation_gain(GAINS[4577], [
        GAINS[4579].get_attributes(level=6),
        BUFFS[4584].attributes,
        BUFFS[4586].attributes,
        {}
    ]),
    create_formation_gain(GAINS[6340], [
        GAINS[6342].get_attributes(level=6),
        BUFFS[6343].attributes,
        BUFFS[6345].get_attributes(stack=BUFFS[6345].max_stack),
        BUFFS[6362].attributes
    ]),
    create_formation_gain(GAINS[8401], [
        GAINS[8402].attributes,
        BUFFS[8484].attributes,
        BUFFS[8403].get_attributes(stack=BUFFS[8403].max_stack),
        BUFFS[8404].attributes
    ]),
    create_formation_gain(GAINS[9484], [
        GAINS[9485].attributes,
        BUFFS[9486].attributes,
        BUFFS[9492].attributes,
        BUFFS[9489].attributes
    ]),
    create_formation_gain(GAINS[10953], [
        GAINS[10954].get_attributes(level=6),
        {},
        BUFFS[11158].attributes,
        BUFFS[11159].attributes
    ]),
    create_formation_gain(GAINS[14072], [
        GAINS[14074].get_attributes(level=6),
        BUFFS[14092].attributes,
        {},
        BUFFS[14095].attributes
    ]),
    create_formation_gain(GAINS[15955], [
        GAINS[15957].get_attributes(level=6),
        BUFFS[15960].attributes,
        BUFFS[15961].attributes,
        BUFFS[15963].attributes
    ]),
    create_formation_gain(GAINS[18334], [
        GAINS[18335].get_attributes(level=6),
        BUFFS[18336].get_attributes(weights=[1] * BUFFS[18336].max_level),
        {k: v / 2 for k, v in BUFFS[18337].attributes.items()},
        {}
    ]),
    create_formation_gain(GAINS[21034], [
        GAINS[21035].get_attributes(level=6),
        {},
        {},
        {}
    ]),
    create_formation_gain(GAINS[24577], [
        GAINS[24578].get_attributes(level=6),
        BUFFS[24581].attributes,
        {},
        {}
    ]),
    create_formation_gain(GAINS[27235], [
        GAINS[27236].get_attributes(level=6),
        {},
        BUFFS[27238].attributes,
        {}
    ]),
    create_formation_gain(GAINS[71338], [
        GAINS[71338].attributes,
        {},
        {},
        {}
    ])
]
FORMATION_GAINS = {k: v for k, v in FORMATION_GAINS}
