from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        409: {}, 10240: {}, 538: {},
        # 奇穴
        5788: {}, 17010: dict(buff_name="广陵月"), 25902: {}, 12549: dict(buff_name="元君"), 17969: {}, 25435: {},
        30274: dict(buff_name="霜降")
    }
}
