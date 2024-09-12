from typing import Dict

from base.constant import GLOBAL_DAMAGE_COF
from base.skill import Skill, NpcSkill


class 知音妙意判定(Skill):
    final_buff = 25997

    def record(self, actual_critical_strike, actual_damage, parser):
        if self.skill_level <= 18:
            parser.refresh_buff(self.final_buff, 2)
        else:
            parser.refresh_buff(self.final_buff, 3)
        super().record(actual_critical_strike, actual_damage, parser)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            14063: dict(channel_interval=16), 14100: {}, 14227: {}, 14311: {}, 14312: {}, 14494: {}, 18859: {},
            18860: {},
            25781: {}, 31008: {}, 31138: {}, 32624: {}, 32738: {}, 34514: {}, 38015: {}, 14082: {}, 30799: {},
            14070: dict(post_buffs={9437: {1: 1}}),
            **{skill_id: dict(post_buffs={-23167: {1: 1}}) for skill_id in (14299, 14067)},
            **{skill_id: dict(bind_dot=9357) for skill_id in (14287, 17788)},
            **{skill_id: dict(bind_dot=9361) for skill_id in (14291, 17792)},
            31005: dict(bind_dot=23187)
        },
        知音妙意判定: {
            34676: dict(
                global_damage_factor=GLOBAL_DAMAGE_COF(1048576 * (0.25 * 0.5 * 1.3 * 1.2 * 0.5 * 1.11 * 0.9 - 1))
            )
        },
        NpcSkill: {15076: {}}
    }
}
