from typing import Dict

from base.buff import Buff

GENERAL_BUFFS: Dict[int, dict] = {
    920: {},
    935: {}, 936: {}, 940: {},
    937: {},
    943: {}, 949: {},
    950: {}, 953: {},
    954: {}, 955: {}, 956: {},
    1926: {},
    2513: {}, 2514: {}, 2510: {},
    3308: {}, 3309: {},
    3310: {},
    4584: {}, 4586: {},
    6343: {}, 6345: {}, 6362: {},
    8484: {}, 8403: {}, 8404: {},
    9486: {}, 9492: {}, 9489: {},
    11158: {}, 11159: {},
    14092: {}, 14095: {},
    15960: {}, 15961: {}, 15963: {},
    18336: {}, 18337: {},
    24581: {},
    27238: {},
}

BUFFS = {}
for buff_id, attrs in GENERAL_BUFFS.items():
    buff = Buff(buff_id)
    buff.activate = False
    for attr, value in attrs.items():
        setattr(buff, attr, value)
    BUFFS[buff_id] = buff
