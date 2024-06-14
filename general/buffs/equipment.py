from typing import Dict

from base.buff import Buff

GENERAL_BUFFS: Dict[int, dict] = {
    15455: {}, 4761: {}, 6360: {}
}

BUFFS = {}
for buff_id, attrs in GENERAL_BUFFS.items():
    buff = Buff(buff_id)
    buff.activate = False
    for attr, value in attrs.items():
        setattr(buff, attr, value)
    BUFFS[buff_id] = buff
