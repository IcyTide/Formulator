from typing import Dict

from base.buff import Buff

GENERAL_BUFFS: Dict[int, dict] = {
    20938: {}, 23107: {}, 6363: {}, 10208: {}, 24350: {}, 21236: {}, 24742: {}, 4246: {}, 8504: {}, 10031: {},
    23543: {}, 11456: {}, 20877: {},
    9744: dict(buff_name="圣浴明心"),
    16911: dict(buff_name="弄梅"),
    15413: dict(buff_name="防御大附魔"),
    23573: dict(buff_name="泠风解怀"),
}
GENERAL_GAINS: Dict[int, dict] = {
    673: {}, 362: {}, 661: {}, 3465: {}, 566: {}, 378: {}, 375: {}, 23305: {}, 4058: {}, 7180: {}, 8248: {},
    12717: dict(buff_name="劲风")
}

BUFFS: Dict[int, Buff] = {}
for buff_id, attrs in GENERAL_BUFFS.items():
    buff = Buff(buff_id)
    buff.activate = False
    buff.set_asset()
    for attr, value in attrs.items():
        setattr(buff, attr, value)
    BUFFS[buff_id] = buff
GAINS: Dict[int, Buff] = {}
for buff_id, attrs in GENERAL_GAINS.items():
    buff = Buff(buff_id)
    buff.activate = False
    buff.set_asset()
    for attr, value in attrs.items():
        setattr(buff, attr, value)
    GAINS[buff_id] = buff
