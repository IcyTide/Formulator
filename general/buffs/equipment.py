from typing import Dict

from base.buff import Buff

GENERAL_BUFFS: Dict[int, dict] = {
    15436: dict(buff_name="大附魔帽"), 15455: dict(buff_name="大附魔腰"), 4761: {}, 6360: {}
}

BUFFS = {}
for buff_id, attrs in GENERAL_BUFFS.items():
    BUFFS[buff_id] = buff = Buff(buff_id)
    buff.activate = False
    buff.set_asset(attrs)
