from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {  # 通用
        12: dict(channel_interval=27), 32820: {},
        # 羽林枪法
        18207: {}, 18208: {}, 18603: {}, 18591: dict(bind_dots={3442: 1}), 18773: {},
        # 奔雷枪术
        431: {}, 14882: {}, 701: {}, 702: {},
        # 游龙骑法
        409: {}, 13778: {}, 24009: {},
        # 奇穴
        402: {}, 37618: {}, 401: dict(bind_dots={12461: 1}), 36568: {}, 24894: {}, 32979: {}, 32980: {}, 24843: {},
        # 装备
        25772: {}, 31031: {},
    }
}
