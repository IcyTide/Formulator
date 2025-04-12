from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        13039: dict(channel_interval=24), 38889: {}, 38971: {}, 32745: dict(physical_shield_gain=[0] * 8 + [-1024]),
        # 云城盾
        19409: {}, 13099: {}, 13044: {}, **{skill_id: {} for skill_id in (13106, 13160, 13161)},
        # 苍雪刀
        13453: {}, 13075: {}, 13092: {}, 28479: {}, 29188: dict(bind_dots={8249: 1}),
        # 破阵令
        13463: {}, 38973: {},
        # 奇穴
        29187: dict(bind_dots={8249: 1}), **{skill_id: {} for skill_id in (13110, 13107, 13108)},
        37253: {}, 37601: dict(bind_dots={8249: 1}), 37600: dict(bind_dots={8249: 1}), 34674: {}, 37448: {},
        36482: {}, 36065: {}, 38890: {}, **{skill_id: {} for skill_id in (30925, 30926, 30857)},
        # **{skill_id: {} for skill_id in range(13076, 13085 + 1)},
        # **{skill_id: {} for skill_id in range(18355, 18364 + 1)},
        # **{skill_id: {} for skill_id in range(28468, 28477 + 1)},
        # 装备
        25780: {},
    }
}
