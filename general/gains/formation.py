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
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[919].attributes.items()},
        {},
        {k: v * BUFFS[920].max_stack for k, v in BUFFS[920].attributes.items()},
        BUFFS[940].attributes
    ]),
    create_formation_gain(GAINS[929], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[919].attributes.items()},
        {k: v * BUFFS[935].max_stack for k, v in BUFFS[935].attributes.items()},
        BUFFS[936].attributes,
        BUFFS[940].attributes
    ]),
    create_formation_gain(GAINS[933], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[934].attributes.items()},
        BUFFS[937].attributes,
        {},
        {}
    ]),
    create_formation_gain(GAINS[931], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[938].attributes.items()},
        {},
        {k: v * BUFFS[943].max_stack for k, v in BUFFS[943].attributes.items()},
        BUFFS[949].attributes
    ]),
    create_formation_gain(GAINS[946], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[947].attributes.items()},
        {},
        {k: v * BUFFS[950].max_stack for k, v in BUFFS[950].attributes.items()},
        BUFFS[953].attributes
    ]),
    create_formation_gain(GAINS[951], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[952].attributes.items()},
        BUFFS[954].attributes,
        BUFFS[955].attributes,
        BUFFS[956].attributes
    ]),
    create_formation_gain(GAINS[1923], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[1924].attributes.items()},
        {},
        {},
        BUFFS[1926].attributes
    ]),
    create_formation_gain(GAINS[2511], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[2512].attributes.items()},
        BUFFS[2513].attributes,
        BUFFS[2514].attributes,
        BUFFS[2510].attributes
    ]),
    create_formation_gain(GAINS[3302], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[3306].attributes.items()},
        {},
        BUFFS[3308].attributes,
        BUFFS[3309].attributes
    ]),
    create_formation_gain(GAINS[3303], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[3307].attributes.items()},
        {},
        BUFFS[3310].attributes,
        {}
    ]),
    create_formation_gain(GAINS[4577], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[4579].attributes.items()},
        BUFFS[4584].attributes,
        BUFFS[4586].attributes,
        {}
    ]),
    create_formation_gain(GAINS[6340], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[6342].attributes.items()},
        BUFFS[6343].attributes,
        {k: v * BUFFS[6345].max_stack for k, v in BUFFS[6345].attributes.items()},
        BUFFS[6362].attributes
    ]),
    create_formation_gain(GAINS[8401], [
        GAINS[8402].attributes,
        BUFFS[8484].attributes,
        {k: v * BUFFS[8403].max_stack for k, v in BUFFS[8403].attributes.items()},
        BUFFS[8404].attributes
    ]),
    create_formation_gain(GAINS[9484], [
        GAINS[9485].attributes,
        BUFFS[9486].attributes,
        BUFFS[9492].attributes,
        BUFFS[9489].attributes
    ]),
    create_formation_gain(GAINS[10953], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[10954].attributes.items()},
        {},
        BUFFS[11158].attributes,
        BUFFS[11159].attributes
    ]),
    create_formation_gain(GAINS[14072], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[14074].attributes.items()},
        BUFFS[14092].attributes,
        {},
        BUFFS[14095].attributes
    ]),
    create_formation_gain(GAINS[15955], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[15957].attributes.items()},
        BUFFS[15960].attributes,
        BUFFS[15961].attributes,
        BUFFS[15963].attributes
    ]),
    create_formation_gain(GAINS[18334], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[18335].attributes.items()},
        {k: sum(v) / len(v) for k, v in BUFFS[18336].attributes.items()},
        {k: v / 2 for k, v in BUFFS[18337].attributes.items()},
        {}
    ]),
    create_formation_gain(GAINS[21034], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[21035].attributes.items()},
        {},
        {},
        {}
    ]),
    create_formation_gain(GAINS[24577], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[24578].attributes.items()},
        BUFFS[24581].attributes,
        {},
        {}
    ]),
    create_formation_gain(GAINS[27235], [
        {k: v[6 - 1] if isinstance(v, list) else v for k, v in GAINS[27236].attributes.items()},
        {},
        BUFFS[27238].attributes,
        {}
    ])
]
FORMATION_GAINS = {k: v for k, v in FORMATION_GAINS}
