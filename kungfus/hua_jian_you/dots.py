from typing import Dict

from base.dot import Dot

DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {
        711: dict(tick_add=1),
        714: dict(tick_add=1),
        666: dict(tick_add=1)
    }
}
