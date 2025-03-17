from typing import Dict

from base.dot import Dot

DOTS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Dot: {
            711: dict(tick_add=1),
            714: dict(tick_add=1),
            666: dict(tick_add=1)
        }
    },
    1: {
        Dot: {
            70041: {}
        }
    }
}
