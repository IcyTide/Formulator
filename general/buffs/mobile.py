from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        buff_id: dict(unique=True, max_stack=10) for buff_id in (70161, 70167, 70162, 70163, 70345, 70188)
    }
}
