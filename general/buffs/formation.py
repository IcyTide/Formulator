from typing import Dict, Tuple

from assets.setter import set_buff
from base.buff import Buff

FORMATION_BUFFS: Dict[int, Tuple[int, int, int, int]] = {
    918: (919, 0, 920, 940),
    929: (930, 935, 936, 940),
    933: (934, 937, 0, 0),
    931: (938, 0, 943, 949),
    946: (947, 0, 950, 953),
    951: (952, 954, 955, 956),
    1923: (1924, 0, 1925, 1926),
    2511: (2512, 2513, 2514, 2510),
    3302: (3306, 0, 3308, 3309),
    3303: (3307, 0, 3310, 0),
    4577: (4579, 4584, 4586, 0),
    6340: (6342, 6343, 6345, 6362),
    8401: (8402, 8484, 8403, 8404),
    9484: (9485, 9486, 9492, 9489),
    10953: (10954, 0, 11158, 11159),
    14072: (14074, 14092, 0, 14095),
    15955: (15957, 15960, 15961, 15963),
    18334: (18335, 18336, 18337, 0),
    21034: (21035, 0, 0, 0),
    24577: (24578, 24581, 0, 0),
    27235: (27236, 0, 27238, 0)
}

BUFFS: Dict[int, Buff] = {}
GAINS: Dict[int, Buff] = {}
for buff_id, buff_ids in FORMATION_BUFFS.items():
    for sub_buff_id in (buff_id, buff_ids[0]):
        buff = Buff(sub_buff_id)
        buff.activate = False
        set_buff(buff)
        GAINS[sub_buff_id] = buff
    for sub_buff_id in buff_ids[1:]:
        if not sub_buff_id:
            continue
        buff = Buff(sub_buff_id)
        buff.activate = False
        set_buff(buff)
        BUFFS[sub_buff_id] = buff
