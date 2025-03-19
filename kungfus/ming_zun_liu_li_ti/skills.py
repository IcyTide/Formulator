from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    0: {
        Skill: {
            4326: dict(channel_interval=16), 32816: {}, 19055: {}, 13468: {}, 3963: {}, 3980: {}, 4035: {}, 4036: {},
            4476: {}, 6750: {}, 18280: {}, 18281: {}, 26708: {}, 26709: {}, 35065: {}, 14701: {}, 25172: {}, 29128: {},
            **{skill_id: {} for skill_id in range(4024, 4026 + 1)},
            **{skill_id: {} for skill_id in range(4028, 4030 + 1)},
            13359: dict(bind_dots={4202: 1})
        }
    }
}
