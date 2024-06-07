from typing import Dict

from base.buff import Buff

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        16025: {}, 26857: {}, -27099: {},
        27406: dict(buff_name="朱厌")
    }
}
BUFFS: Dict[int, Buff] = {}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
