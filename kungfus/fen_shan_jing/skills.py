from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        13039: dict(channel_interval=24), 38889: {}, 38971: {}, 32745: dict(physical_shield_gain=[0] * 8 + [-1024]),
        **{skill_id: dict(bind_dots={8249: 1}) for skill_id in (29187, 29188, 37568, 37569, 37600, 37601)},
        # 云城盾
        19409: {}, 13099: {}, 13044: {}, **{skill_id: {} for skill_id in (13106, 13107, 13108, 13110, 13160, 13161)},
        # 苍雪刀
        13453: {}, 13075: {}, 13092: {}, 28479: {},
        # 破阵令
        13463: {}, 38973: {},
        # 奇穴
        37253: {}, 34674: {}, 34714: {}, 37448: {}, 36482: {}, 36065: {}, 38890: {}, 30925: {}, 30926: {}, 30857: {},
        **{skill_id: {} for skill_id in range(13076, 13085 + 1)},
        **{skill_id: {} for skill_id in range(18355, 18364 + 1)},
        **{skill_id: {} for skill_id in range(28468, 28477 + 1)},
        # 装备
        25780: {},
    }
}
