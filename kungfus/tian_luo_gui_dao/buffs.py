from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            3254: {}, 3316: {}, 6105: {}, 3468: {}, 8210: {}, 9981: {}, 6112: {}, 3426: {},
            -10005: dict(stackable=False, max_stack=2),
            13165: dict(buff_name="雷甲三铉"),
            27405: dict(buff_name="雷甲三铉"),
            23081: dict(buff_name="擘两分星"),
            23082: dict(buff_name="擘两分星")
        }
    }
}
