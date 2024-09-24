from typing import Dict

from base.skill import Skill


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            3121: dict(channel_interval=16), 32885: {}, 3105: {}, 18776: {}, 3223: {}, 3228: {}, 3313: {}, 3393: {},
            3480: {}, 25774: {}, 30727: {}, 30894: {}, 36502: {}, 3401: {}, 3404: {}, 3819: {}, 3824: {}, 37384: {},
            18677: {}, 28441: {},
            15049: dict(post_buffs={10005: {1: 2}}),
            21266: dict(bind_dot=14611)
        }
    }
}
