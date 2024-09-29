from typing import Dict

from base.buff import Buff, CustomBuff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            6121: {}, 6363: {}, 14981: {}, 7671: {}, 21638: {}, 2779: {}, 28169: {},
            -12608: dict(buff_name="风虎", activate=False, interval=4),
            -26008: dict(buff_name="战心"),
            1911: dict(begin_buffs={-1: {1: 5}}),
        },
        CustomBuff: {
            -1: dict(buff_name="战意", max_stack=5),
        }
    }
}
