from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            15893: {}, 15932: {}, 15926: {}, **{buff_id: dict(buff_name="百节") for buff_id in (15927, 15928, 15929)},
            16596: dict(buff_name="崔嵬鬼步"),
            15832: dict(buff_name="星旗"),
            21588: dict(buff_name="孤路")
        }
    }
}
