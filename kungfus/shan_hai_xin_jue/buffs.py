from typing import Dict

from base.buff import Buff, CustomBuff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        26857: {},
        # 奇穴
        26952: {}, 27099: dict(continuous=True),
        # 装备
        27543: {}
    },
    CustomBuff: {
        -1: dict(max_stack=3)
    }
}
