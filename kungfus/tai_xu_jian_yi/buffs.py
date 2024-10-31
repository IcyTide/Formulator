from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            378: {}, 2930: {}, 17933: {}, 2757: {}, 21865: {}, 29204: {}, 1915: {},
            6093: dict(end_frame_shift=1),
            29451: dict(max_stack=4, interval=80),
            -29451: dict(attributes=dict(all_damage_cof=0.5 * 1024), max_stack=4)
        }
    }
}
