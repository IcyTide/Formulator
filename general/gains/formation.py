from typing import List

from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from general.buffs.formation import BUFFS


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
    create_formation_gain(BUFFS[-918], [
        BUFFS[-919].get_attributes(level=6),
        {},
        BUFFS[920].get_attributes(stack=BUFFS[920].max_stack),
        BUFFS[940].attributes
    ]),
    create_formation_gain(BUFFS[-929], [
        BUFFS[-919].get_attributes(level=6),
        BUFFS[935].get_attributes(stack=BUFFS[935].max_stack),
        BUFFS[936].attributes,
        BUFFS[940].attributes
    ]),
    create_formation_gain(BUFFS[-933], [
        BUFFS[-934].get_attributes(level=6),
        BUFFS[937].attributes,
        {},
        {}
    ]),
    create_formation_gain(BUFFS[-931], [
        BUFFS[-938].get_attributes(level=6),
        {},
        BUFFS[943].get_attributes(stack=BUFFS[943].max_stack),
        BUFFS[949].attributes
    ]),
    create_formation_gain(BUFFS[-946], [
        BUFFS[-947].get_attributes(level=6),
        {},
        BUFFS[950].get_attributes(stack=BUFFS[950].max_stack),
        BUFFS[953].attributes
    ]),
    create_formation_gain(BUFFS[-951], [
        BUFFS[-952].get_attributes(level=6),
        BUFFS[954].attributes,
        BUFFS[955].attributes,
        BUFFS[956].attributes
    ]),
    create_formation_gain(BUFFS[-1923], [
        BUFFS[-1924].get_attributes(level=6),
        {},
        {},
        BUFFS[1926].attributes
    ]),
    create_formation_gain(BUFFS[-2511], [
        BUFFS[-2512].get_attributes(level=6),
        BUFFS[2513].attributes,
        BUFFS[2514].attributes,
        BUFFS[2510].attributes
    ]),
    create_formation_gain(BUFFS[-3302], [
        BUFFS[-3306].get_attributes(level=6),
        {},
        BUFFS[3308].attributes,
        BUFFS[3309].attributes
    ]),
    create_formation_gain(BUFFS[-3303], [
        BUFFS[-3307].get_attributes(level=6),
        {},
        BUFFS[3310].attributes,
        {}
    ]),
    create_formation_gain(BUFFS[-4577], [
        BUFFS[-4579].get_attributes(level=6),
        BUFFS[4584].attributes,
        BUFFS[4586].attributes,
        {}
    ]),
    create_formation_gain(BUFFS[-6340], [
        BUFFS[-6342].get_attributes(level=6),
        BUFFS[6343].attributes,
        BUFFS[6345].get_attributes(stack=BUFFS[6345].max_stack),
        BUFFS[6362].attributes
    ]),
    create_formation_gain(BUFFS[-8401], [
        BUFFS[-8402].attributes,
        BUFFS[8484].attributes,
        BUFFS[8403].get_attributes(stack=BUFFS[8403].max_stack),
        BUFFS[8404].attributes
    ]),
    create_formation_gain(BUFFS[-9484], [
        BUFFS[-9485].attributes,
        BUFFS[9486].attributes,
        BUFFS[9492].attributes,
        BUFFS[9489].attributes
    ]),
    create_formation_gain(BUFFS[-10953], [
        BUFFS[-10954].get_attributes(level=6),
        {},
        BUFFS[11158].attributes,
        BUFFS[11159].attributes
    ]),
    create_formation_gain(BUFFS[-14072], [
        BUFFS[-14074].get_attributes(level=6),
        BUFFS[14092].attributes,
        {},
        BUFFS[14095].attributes
    ]),
    create_formation_gain(BUFFS[-15955], [
        BUFFS[-15957].get_attributes(level=6),
        BUFFS[15960].attributes,
        BUFFS[15961].attributes,
        BUFFS[15963].attributes
    ]),
    create_formation_gain(BUFFS[-18334], [
        BUFFS[-18335].get_attributes(level=6),
        BUFFS[18336].get_attributes(weights=[1] * BUFFS[18336].max_level),
        {k: v / 2 for k, v in BUFFS[18337].attributes.items()},
        {}
    ]),
    create_formation_gain(BUFFS[-21034], [
        BUFFS[-21035].get_attributes(level=6),
        {},
        {},
        {}
    ]),
    create_formation_gain(BUFFS[-24577], [
        BUFFS[-24578].get_attributes(level=6),
        BUFFS[24581].attributes,
        {},
        {}
    ]),
    create_formation_gain(BUFFS[-27235], [
        BUFFS[-27236].get_attributes(level=6),
        {},
        BUFFS[27238].attributes,
        {}
    ]),
    create_formation_gain(BUFFS[-71338], [
        BUFFS[-71338].attributes,
        {},
        {},
        {}
    ])
]
FORMATION_GAINS = {k: v for k, v in FORMATION_GAINS}
