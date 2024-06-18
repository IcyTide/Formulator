from typing import Dict

from assets.setter import set_buff
from base.buff import Buff

GENERAL_BUFFS: Dict[int, dict] = {
    15436: dict(buff_name="大附魔帽"), 15455: dict(buff_name="输出伤害波动"), 4761: {}, 6360: {}
}

BUFFS = {}
for buff_id, attrs in GENERAL_BUFFS.items():
    buff = Buff(buff_id)
    buff.activate = False
    for attr, value in attrs.items():
        setattr(buff, attr, value)
    set_buff(buff)
    BUFFS[buff_id] = buff
