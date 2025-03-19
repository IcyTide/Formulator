from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    0: {
        Skill: {
            13039: dict(channel_interval=24), 38971: {}, 13463: {}, 19409: {}, 13099: {}, 13044: {}, 38973: {},
            13453: {}, 23284: {}, 23285: {}, 23286: {}, 23287: {}, 23294: {}, 16727: {},
            **{skill_id: {} for skill_id in list(range(13076, 13085 + 1)) + [13075]},
            **{skill_id: {} for skill_id in list(range(18355, 18364 + 1)) + [13092]},
            **{skill_id: {} for skill_id in list(range(28468, 28477 + 1)) + [28479]},
            **{skill_id: {} for skill_id in (13106, 13107, 13108, 13110, 13160, 13161)},
            32745: dict(physical_shield_gain=[0] * 8 + [-1024]),
            **{
                skill_id: dict(bind_dots={8249: 1})
                for skill_id in (29187, 29188, 37568, 37569, 37600, 37601)
            },
        }
    }
}
