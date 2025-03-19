from typing import Dict

from base.buff import Buff
from general.buffs import consumable, equipment, formation, team

BUFFS = [
    consumable.BUFFS,
    equipment.BUFFS,
    formation.BUFFS,
    team.BUFFS
]
GENERAL_BUFFS: Dict[int, Buff] = {}
for buffs in BUFFS:
    for buff_class, items in buffs.items():
        for buff_id, attrs in items.items():
            GENERAL_BUFFS[buff_id] = buff = Buff(buff_id)
            buff.activate = False
            buff.set_asset(attrs)
