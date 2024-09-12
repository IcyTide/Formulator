from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            29243: dict(buff_name="玉枕"), 29254: {}, 29237: {}, 28756: {},
        }
    },
    1: {
        Buff: {
            71388: {}, 71405: {}, 71382: {}
        }
    }
}
