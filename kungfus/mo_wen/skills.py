from typing import Dict

from base.skill import Skill, NpcSkill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        14063: dict(channel_interval=16), 32738: {},
        # 音
        14474: {}, 18860: {}, 14311: {}, 14312: {}, 14227: {}, 14100: {}, 18859: {},
        18656: {}, 25225: {}, 40293: {}, 40285: {}, 18663: {}, 14455: {},
        # 曲
        14494: {}, 14070: {},
        # 影
        14082: {},
        **{skill_id: dict(bind_dots={9357: 1}) for skill_id in (14287, 17788)},
        **{skill_id: dict(bind_dots={9361: 1}) for skill_id in (14291, 17792)},
        # 奇穴
        **{skill_id: dict(bind_dots={9358: 1}) for skill_id in (14288, 17789)},
        **{skill_id: dict(bind_dots={9362: 1}) for skill_id in (14292, 17793)},
        34514: {}, 30799: {}, 38015: {}, 40330: {}, 40811: {}, 29077: {},
        34676: dict(global_damage_factor=1048576 * (0.25 * 0.5 * 1.3 * 1.2 * 0.5 * 1.11 * 0.9 * 0.9362 - 1)),
        # 装备
        25781: {}, 31008: {}, 31138: {}, **{skill_id: dict(bind_dots={23187: 1}) for skill_id in (31005, 40815)}
    },
    NpcSkill: {15076: {}}
}
