from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        32908: {}, 32898: {}, 40264: {},
        # 打狗棒法
        13520: {},
        **{skill_id: {} for skill_id in range(6376, 6380 + 1)},
        13505: {}, **{skill_id: {} for skill_id in range(6381, 6391 + 1)},
        **{skill_id: {} for skill_id in range(13523, 13530 + 1)},
        **{skill_id: {} for skill_id in range(40184, 40187 + 1)},
        # 降龙掌
        13510: {},
        **{skill_id: {} for skill_id in range(8491, 8514 + 1)},
        **{skill_id: {} for skill_id in range(6351, 6374 + 1)},
        **{skill_id: dict(bind_dots={6367: 1}) for skill_id in (6853,)},
        # 奇穴
        26703: {}, 25201: {}, 25202: {}, **{skill_id: dict(bind_dots={6401: 1}) for skill_id in (6867,)},
        **{skill_id: {} for skill_id in range(19430, 19439 + 1)}, 38891: {}, 40335: {},
        # 装备
        25779: {},
    }
}
