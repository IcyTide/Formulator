from typing import Dict

from assets.setter import set_buff
from base.buff import Buff
from general.buffs import GENERAL_BUFFS
from schools.tai_xuan_jing.talents import 重山

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        18555: {}, 18002: {}, 18021: {}, 18174: {},
        **{
            buff_id: dict(gains=[重山(value, skill_id, skill_id) for skill_id in (24369, 24371, 24372)])
            for buff_id, value in ((28303, 1.074), (28304, 1.14815), (28305, 1.2223))
        }
    }
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        set_buff(buff)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
