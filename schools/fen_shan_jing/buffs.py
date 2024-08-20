from typing import Dict

from base.buff import Buff, CustomBuff
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        1428: {}, 8244: {}, 17176: {}, 8267: {}, 14309: {}, 8451: {}, 27161: {}, 16957: {}, -9889: {},
        -8248: dict(interval=400),
        25937: dict(buff_name="祭血关山"),
        8627: dict(buff_name="锋鸣"),
        8474: dict(begin_buffs={-1: {1: 70}}, end_buffs={-1: {1: 70}}),
        26212: dict(begin_buffs={-1: {1: 45}}, begin_target_buffs={-8248: {1: 1}}),
        -9052: dict(buff_name="绝刀增伤")
    },
    CustomBuff: {-1: dict(buff_name="怒气", max_stack=100)}
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        buff.set_asset()
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
