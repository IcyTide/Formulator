from typing import Dict

from base.skill import Skill
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        19712: dict(damage_addition=205),
        19766: {}, 19767: {}, 20014: {}, 19819: {}, 20016: {}, 20052: {}, 20054: {}, 20322: {}, 20323: {}, 20684: {},
        20685: {}, 20734: {}, 25273: {}, 25783: {}, 31250: {}, 32478: {}, 32815: {}, 36282: {},
        25640: dict(bind_dot=18386),
        26935: dict(bind_dot=19557)
    },
}


class 击水加成(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        parser.refresh_target_buff(70188, 30)
        super().record(actual_critical_strike, actual_damage, parser)
        parser.refresh_target_buff(70188, 30, -1)


class 逐波加成(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        parser.refresh_target_buff(70188, 80)
        super().record(actual_critical_strike, actual_damage, parser)
        parser.refresh_target_buff(70188, 80, -1)


MOBILE_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        102134: {}, 102173: {}, 102145: {}, 102111: {}, 102161: {}, 102228: {}, 102103: {}
    },
    击水加成: {
        102091: {}, 102092: {}, 102093: {}
    },
    逐波加成: {
        102104: {}
    }
}
SKILLS = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        skill.set_asset()
        SKILLS[skill_id] = skill
for skill_class, skills in MOBILE_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        skill.set_asset()
        SKILLS[skill_id] = skill
