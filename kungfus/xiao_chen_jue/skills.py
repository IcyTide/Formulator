from typing import Dict

from base.skill import Skill

SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            32908: {}, 13520: {}, 34916: {}, 6337: {}, 26703: {}, 32898: {}, 14927: {}, 14928: {}, 36570: {}, 28819: {},
            25779: {}, 34998: {}, 28952: {},
            **{skill_id: {} for skill_id in range(6355, 6374 + 1)},
            **{skill_id: {} for skill_id in range(13523, 13530 + 1)},
            **{skill_id: dict(bind_dot=6367) for skill_id in (6853, 14930)},
            **{skill_id: dict(bind_dot=6401) for skill_id in (6867, 14931)}
        }
    },
    1: {}
}
