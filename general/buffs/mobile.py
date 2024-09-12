from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Buff] = {}
for buff_id in (70161, 70167, 70162, 70163, 70345, 70729, 70188, 70973):
    BUFFS[buff_id] = buff = Buff(buff_id)
    buff.set_asset(dict(unique=True, max_stack=10))
