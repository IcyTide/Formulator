from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        8244: {}, 9052: dict(buff_name="绝刀增伤", begin_frame_shift=-2),
        # 奇穴
        18222: {}, 8276: {}, -9889: {}, 8423: {}, 8271: {}, 17772: {},
        # 装备
        8474: {}
    }
}