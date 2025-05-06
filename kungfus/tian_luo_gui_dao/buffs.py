from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        3254: {}, 3316: {}, 3468: {},
        # 奇穴
        6105: {}, 23081: dict(buff_name="擘两分星"), 23082: dict(buff_name="擘两分星"), 8210: {},
        13165: dict(buff_name="雷甲三铉"), 27405: dict(buff_name="雷甲三铉"),
        -24668: dict(buff_name="杀机断魂"), 24669: {}, 16234: {}, 16235: {}, 16236: {}, 9981: {}, 10005: {},
    }
}
