from typing import Dict

from base.dot import Dot

SCHOOL_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {
        20052: {}
    }
}
MOBILE_DOTS: Dict[type, Dict[int, dict]] = {
    Dot: {
        71171: {}
    }
}
DOTS: Dict[int, Dot] = {}
for dot_class, dots in SCHOOL_DOTS.items():
    for dot_id, attrs in dots.items():
        DOTS[dot_id] = dot = dot_class(dot_id)
        dot.set_asset(attrs)
for dot_class, dots in MOBILE_DOTS.items():
    for dot_id, attrs in dots.items():
        DOTS[dot_id] = dot = dot_class(dot_id)
        dot.set_asset(attrs)
