from typing import Dict

from base.dot import Dot

SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {
        6218: {}, 2509: {}, 12557: {}, 2295: {}, 18882: {},
        2296: dict(tick_extra=1),
        25917: dict(tick_extra=1),
    }
}
DOTS: Dict[int, Dot] = {}
for dot_class, dots in SCHOOL_DOTS.items():
    for dot_id, attrs in dots.items():
        dot = dot_class(dot_id)
        for attr, value in attrs.items():
            setattr(dot, attr, value)
        dot.set_asset()
        DOTS[dot_id] = dot
