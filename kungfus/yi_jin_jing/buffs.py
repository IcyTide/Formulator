from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        # 通用
        2686: {}, 10023: {}, 24285: {}, 24453: {},
        890: dict(max_stack=2, interval=352),
        19635: dict(buff_name="普渡", interval=4),
        # 奇穴
        12479: dict(max_stack=3, interval=352), 11979: {}, 21859: {},
        13910: dict(buff_name="众嗔"), 12590: dict(buff_name="三生", continuous=True), 29547: dict(buff_name="华香"),
        # 装备
        1919: {}
    }
}
