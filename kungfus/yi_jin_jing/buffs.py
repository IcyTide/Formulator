from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            11979: {}, 2686: {}, 10023: {}, 24285: {}, 24453: {}, 21859: {}, 1919: {},
            29547: dict(buff_name="华香"),
            890: dict(max_stack=2, interval=352),
            12479: dict(max_stack=3, interval=352),
            -13910: dict(buff_name="众嗔", interval=4),
            12590: dict(buff_name="三生", continuous=True),
            19635: dict(buff_name="普渡", interval=4)
        }
    }
}
