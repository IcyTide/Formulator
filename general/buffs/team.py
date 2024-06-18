from typing import Dict

from assets.setter import set_buff
from base.buff import Buff

GENERAL_BUFFS: Dict[int, dict] = {
    20938: {}, 23107: {}, 6363: {}, 10208: {}, 24350: {}, 21236: {}, 24742: {}, 4246: {}, 9744: {}, 8504: {}, 10031: {},
    23543: {}, 11456: {}, 20877: {},
    16911: dict(buff_name="弄梅"),
    15413: dict(buff_name="防御大附魔"),
    23573: dict(buff_name="泠风解怀"),
}

BUFFS = {}
for buff_id, attrs in GENERAL_BUFFS.items():
    buff = Buff(buff_id)
    buff.activate = False
    for attr, value in attrs.items():
        setattr(buff, attr, value)
    set_buff(buff)
    BUFFS[buff_id] = buff
