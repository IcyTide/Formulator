from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        24168: {}, 24553: {}, 24554: {},
        # 奇穴
        30304: {}, 24209: {},
        # 装备
        24752: {}
    }
}
