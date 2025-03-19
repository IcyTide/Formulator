from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        **{skill_id: dict(channel_interval=24) for skill_id in (32974, 32975)}, 33146: {}, 32510: {},
        # 骤雨劲
        32246: {}, 32766: {},
        # 流云势法
        32149: {}, 32150: {}, 32151: {}, 32154: {}, 32167: {}, 32348: {},
        # 破浪三式
        32602: {}, 32603: {}, 32604: {}, 32891: {}, 32892: {},
        **{skill_id: {} for skill_id in range(32234, 32239 + 1)},
        **{skill_id: dict(bind_dots={24132: i + 1}) for i, skill_id in enumerate(range(32372, 32369 - 1, -1))},
        # 游风步
        32357: {},
        # 奇穴
        34695: {}, 36118: {},
        # 装备
        33239: {}, 33133: dict(bind_dots={24650: 1}),
    }
}
