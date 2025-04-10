from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        13039: dict(channel_interval=24), 38971: {}, 32745: dict(physical_shield_gain=[0] * 8 + [-1024]),
        # 云城盾
        19409: {}, 13099: {}, 13044: {}, 13244: {}, 13060: {}, 13119: {},
        **{skill_id: {} for skill_id in (13106, 13107, 13108, 13110, 13160, 13161)},
        # 苍雪刀
        13453: {}, 13075: {}, 13092: {}, 28479: {}, 29188: dict(bind_dots={8249: 1}),
        # 破阵令
        13463: {}, 38973: {},
        # 奇穴
        40721: {}, 29187: dict(bind_dots={8249: 1}), 26898: {},25215: {},
        # 装备
        25780: {}
    }
}
