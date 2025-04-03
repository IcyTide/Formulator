from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        3121: dict(channel_interval=16), 32885: {},
        # 九宫飞星
        3105: {}, 18776: {}, 3393: {}, 3126: dict(bind_dots={3221: 1}), 3313: {}, 36502: {},
        3401: {}, 3404: {}, 3819: {}, 3824: {},
        # 乾坤一掷
        3223: {}, 3228: {},
        # 奇穴
        30894: {}, 30727: {}, 21266: dict(bind_dots={14611: 1}), 38760: dict(bind_dots=[{}, {29549: 1}]),
        15049: dict(post_buffs={10005: {1: 1}}), 31026: {}, 31027: {}, 18677: {}, 28441: {},
        29687: dict(consume_dots={dot_id: (3, 3) for dot_id in (3221, 14611)}),
        # 装备
        25774: {}, 3480: {},
    }
}
