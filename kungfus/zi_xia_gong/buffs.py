from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        375: {}, 1908: {}, 2757: {}, 1916: {},
        # 奇穴
        **{buff_id: {} for buff_id in range(12779, 12783 + 1)},
        9966: dict(buff_name="同尘"),
        17918: dict(activate=False),
        -12550: dict(buff_name="跬步", activate=False, interval=4),
        -12551: dict(buff_name="跬步", activate=False, interval=4)
    }
}
