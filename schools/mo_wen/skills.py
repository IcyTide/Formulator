from typing import Dict

from base.constant import GLOBAL_DAMAGE_COF
from base.skill import Skill, NpcSkill
from general.skills import GENERAL_SKILLS


class 知音妙意判定(Skill):
    final_buff = 25997

    def record(self, actual_critical_strike, actual_damage, parser):
        if self.skill_level <= 18:
            parser.refresh_buff(self.final_buff, 2)
        else:
            parser.refresh_buff(self.final_buff, 3)
        super().record(actual_critical_strike, actual_damage, parser)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        14063: {}, 14100: {}, 14227: {}, 14311: {}, 14312: {}, 14494: {}, 18859: {}, 18860: {}, 25781: {}, 31008: {},
        31138: {}, 32624: {}, 32738: {}, 34514: {}, 38015: {}, 14082: {},
        14070: dict(post_buffs={9437: {1: 1}}),
        30799: dict(lunar_shield_gain_extra=-922),  # BUFF-23167
        **{skill_id: dict(bind_dot=9357) for skill_id in (14287, 17788)},
        **{skill_id: dict(bind_dot=9361) for skill_id in (14291, 17792)},
        31005: dict(bind_dot=23187)
    },
    知音妙意判定: {
        34676: dict(
            global_damage_factor_extra=GLOBAL_DAMAGE_COF(1048576 * (0.25 * 0.5 * 1.3 * 1.2 * 0.5 * 1.11 * 0.9 - 1))
        )
    },
    NpcSkill: {15076: {}}
}
SKILLS: Dict[int, Skill] = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        SKILLS[skill_id] = skill = skill_class(skill_id)
        skill.set_asset(attrs)
