from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        22126: dict(channel_interval=24), 32822: {},
        # 断水刃
        **{skill_id: {} for skill_id in (22170, 22550, 22551, 22298)}, 22620: {}, 22621: {},
        # 隐雷鞭
        **{skill_id: {} for skill_id in (22610, 22611, 22552, 22612, 36269, 36270)},
        **{skill_id: {} for skill_id in (22328, 22329, 22604, 22605, 36267, 36268)},
        **{skill_id: {} for skill_id in (22489, 22490, 22553, 22554, 36265, 36266)},
        22359: {},
        # 冲云链
        22787: dict(pre_buffs={15932: {1: 1}}),
        # 奇穴
        25314: {}, 34981: {}, 22330: dict(bind_dots={15568: 1}), 29751: {}, 40156: {}, 22761: {},
        # 装备
        25784: {}, 26980: dict(bind_dots={19626: 1}),
    }
}
