from typing import Dict

from base.dot import Dot

SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {
        6218: {}, 2509: {}, 12557: {}, 2295: {}, 18882: {},
        2296: dict(tick_add=1),
        25917: dict(tick_add=1),
    }
}
DOTS: Dict[int, Dot] = {}
for dot_class, dots in SCHOOL_DOTS.items():
    for dot_id, attrs in dots.items():
        DOTS[dot_id] = dot = dot_class(dot_id)
        dot.set_asset(attrs)
