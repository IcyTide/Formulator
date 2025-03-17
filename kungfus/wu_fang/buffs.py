from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            # 通用
            21168: dict(buff_name="植物温性", continuous=True),
            # 奇穴
            20680: {}, 30352: dict(buff_name="凄骨"), 20699: dict(buff_name="养荣"),
        }
    },
    1: {
        Buff: {
            71230: {}, 71258: {}, 70529: {}
        }
    }
}
