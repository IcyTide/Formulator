from typing import Dict

from base.dot import Dot
from general.dots import equipment

DOTS = [
    equipment.DOTS
]
GENERAL_DOTS: Dict[int, Dot] = {}
for dots in DOTS:
    for dot_class, items in dots.items():
        for dot_id, attrs in items.items():
            GENERAL_DOTS[dot_id] = dot = Dot(dot_id)
            dot.activate = False
            dot.set_asset(attrs)
