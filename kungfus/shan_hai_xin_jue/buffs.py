from typing import Dict

from base.buff import Buff, CustomBuff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        26857: {}, 27543: {},
        27099: dict(continuous=True)
    },
    CustomBuff: {
        -1: dict(max_stack=3)
    }
}
