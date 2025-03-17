from typing import Dict

from base.dot import Dot

DOTS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Dot: {
            2509: {}, 2295: {}, 2296: dict(tick_add=1),
            # 奇穴
            25917: dict(tick_add=1), 12557: {}, 28210: {}
        }
    }
}
