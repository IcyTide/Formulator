from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            3254: {}, 8210: {}, 9981: {}, 7659: {}, 3276: {}, -28225: {}, -28226: {}, -28227: {},
            10169: dict(buff_name="逐一击破"),
            17103: dict(buff_name="追命无声"),
        }
    }
}
