from typing import Dict

from base.skill import Skill, NpcSkill

SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            14063: dict(channel_interval=16),
            14100: {}, 14227: {}, 14311: {}, 14312: {}, 14494: {}, 18859: {}, 18860: {}, 25781: {}, 31008: {},
            31138: {}, 32624: {}, 32738: {}, 34514: {}, 38015: {}, 14082: {}, 30799: {},
            34676: dict(global_damage_factor=1048576 * (0.25 * 0.5 * 1.3 * 1.2 * 0.5 * 1.11 * 0.9 * 0.9362 - 1)),
            14070: dict(post_buffs={9437: {1: 1}}),
            **{skill_id: dict(post_buffs={-23167: {1: 1}}) for skill_id in (14299, 14067)},
            **{skill_id: dict(bind_dots={9357: 1}) for skill_id in (14287, 17788)},
            **{skill_id: dict(bind_dots={9361: 1}) for skill_id in (14291, 17792)},
            **{skill_id: dict(bind_dots={9358: 1}) for skill_id in (14288, 17789)},
            **{skill_id: dict(bind_dots={9362: 1}) for skill_id in (14292, 17793)},
            31005: dict(bind_dots={23187: 1})
        },
        NpcSkill: {15076: {}}
    }
}
