from typing import List

from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from general.buffs import GENERAL_BUFFS


class FormationGain(Gain):
    attributes: List[dict] = None
    rates: List[float] = None

    def __init__(self, rates):
        super().__init__()
        self.rates = [1] + [rate / 100 for rate in rates]

    def add_attribute(self, attribute: Attribute):
        for attributes, rate in zip(self.attributes, self.rates):
            for attr, value in attributes.items():
                attribute[attr] += int(value * rate)

    def sub_attribute(self, attribute: Attribute):
        for attributes, rate in zip(self.attributes, self.rates):
            for attr, value in attributes.items():
                attribute[attr] -= int(value * rate)


def create_formation_gain(buff: Buff, attributes: List[dict]):
    return buff.buff_name, type(buff.buff_name, (FormationGain,), dict(attributes=attributes))


FORMATION_GAINS = [
    create_formation_gain(GENERAL_BUFFS[-918], [
        GENERAL_BUFFS[-919].get_attributes(level=6),
        {},
        GENERAL_BUFFS[920].get_attributes(stack=GENERAL_BUFFS[920].max_stack),
        GENERAL_BUFFS[940].attributes
    ]),
    create_formation_gain(GENERAL_BUFFS[-929], [
        GENERAL_BUFFS[-919].get_attributes(level=6),
        GENERAL_BUFFS[935].get_attributes(stack=GENERAL_BUFFS[935].max_stack),
        GENERAL_BUFFS[936].attributes,
        GENERAL_BUFFS[940].attributes
    ]),
    create_formation_gain(GENERAL_BUFFS[-933], [
        GENERAL_BUFFS[-934].get_attributes(level=6),
        GENERAL_BUFFS[937].attributes,
        {},
        {}
    ]),
    create_formation_gain(GENERAL_BUFFS[-931], [
        GENERAL_BUFFS[-938].get_attributes(level=6),
        {},
        GENERAL_BUFFS[943].get_attributes(stack=GENERAL_BUFFS[943].max_stack),
        GENERAL_BUFFS[949].attributes
    ]),
    create_formation_gain(GENERAL_BUFFS[-946], [
        GENERAL_BUFFS[-947].get_attributes(level=6),
        {},
        GENERAL_BUFFS[950].get_attributes(stack=GENERAL_BUFFS[950].max_stack),
        GENERAL_BUFFS[953].attributes
    ]),
    create_formation_gain(GENERAL_BUFFS[-951], [
        GENERAL_BUFFS[-952].get_attributes(level=6),
        GENERAL_BUFFS[954].attributes,
        GENERAL_BUFFS[955].attributes,
        GENERAL_BUFFS[956].attributes
    ]),
    create_formation_gain(GENERAL_BUFFS[-1923], [
        GENERAL_BUFFS[-1924].get_attributes(level=6),
        {},
        {},
        GENERAL_BUFFS[1926].attributes
    ]),
    create_formation_gain(GENERAL_BUFFS[-2511], [
        GENERAL_BUFFS[-2512].get_attributes(level=6),
        GENERAL_BUFFS[2513].attributes,
        GENERAL_BUFFS[2514].attributes,
        GENERAL_BUFFS[2510].attributes
    ]),
    create_formation_gain(GENERAL_BUFFS[-3302], [
        GENERAL_BUFFS[-3306].get_attributes(level=6),
        {},
        GENERAL_BUFFS[3308].attributes,
        GENERAL_BUFFS[3309].attributes
    ]),
    create_formation_gain(GENERAL_BUFFS[-3303], [
        GENERAL_BUFFS[-3307].get_attributes(level=6),
        {},
        GENERAL_BUFFS[3310].attributes,
        {}
    ]),
    create_formation_gain(GENERAL_BUFFS[-4577], [
        GENERAL_BUFFS[-4579].get_attributes(level=6),
        GENERAL_BUFFS[4584].attributes,
        GENERAL_BUFFS[4586].attributes,
        {}
    ]),
    create_formation_gain(GENERAL_BUFFS[-6340], [
        GENERAL_BUFFS[-6342].get_attributes(level=6),
        GENERAL_BUFFS[6343].attributes,
        GENERAL_BUFFS[6345].get_attributes(stack=GENERAL_BUFFS[6345].max_stack),
        GENERAL_BUFFS[6362].attributes
    ]),
    create_formation_gain(GENERAL_BUFFS[-8401], [
        GENERAL_BUFFS[-8402].attributes,
        GENERAL_BUFFS[8484].attributes,
        GENERAL_BUFFS[8403].get_attributes(stack=GENERAL_BUFFS[8403].max_stack),
        GENERAL_BUFFS[8404].attributes
    ]),
    create_formation_gain(GENERAL_BUFFS[-9484], [
        GENERAL_BUFFS[-9485].attributes,
        GENERAL_BUFFS[9486].attributes,
        GENERAL_BUFFS[9492].attributes,
        GENERAL_BUFFS[9489].attributes
    ]),
    create_formation_gain(GENERAL_BUFFS[-10953], [
        GENERAL_BUFFS[-10954].get_attributes(level=6),
        {},
        GENERAL_BUFFS[11158].attributes,
        GENERAL_BUFFS[11159].attributes
    ]),
    create_formation_gain(GENERAL_BUFFS[-14072], [
        GENERAL_BUFFS[-14074].get_attributes(level=6),
        GENERAL_BUFFS[14092].attributes,
        {},
        GENERAL_BUFFS[14095].attributes
    ]),
    create_formation_gain(GENERAL_BUFFS[-15955], [
        GENERAL_BUFFS[-15957].get_attributes(level=6),
        GENERAL_BUFFS[15960].attributes,
        GENERAL_BUFFS[15961].attributes,
        GENERAL_BUFFS[15963].attributes
    ]),
    create_formation_gain(GENERAL_BUFFS[-18334], [
        GENERAL_BUFFS[-18335].get_attributes(level=6),
        GENERAL_BUFFS[18336].get_attributes(weights=[1] * GENERAL_BUFFS[18336].max_level),
        {k: v / 2 for k, v in GENERAL_BUFFS[18337].attributes.items()},
        {}
    ]),
    create_formation_gain(GENERAL_BUFFS[-21034], [
        GENERAL_BUFFS[-21035].get_attributes(level=6),
        {},
        {},
        {}
    ]),
    create_formation_gain(GENERAL_BUFFS[-24577], [
        GENERAL_BUFFS[-24578].get_attributes(level=6),
        GENERAL_BUFFS[24581].attributes,
        {},
        {}
    ]),
    create_formation_gain(GENERAL_BUFFS[-27235], [
        GENERAL_BUFFS[-27236].get_attributes(level=6),
        {},
        GENERAL_BUFFS[27238].attributes,
        {}
    ]),
    create_formation_gain(GENERAL_BUFFS[-71338], [
        GENERAL_BUFFS[-71338].attributes,
        {},
        {},
        {}
    ])
]
FORMATION_GAINS = {k: v for k, v in FORMATION_GAINS}
