from typing import Dict

from base.skill import Skill
from general.skills import GENERAL_SKILLS

SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        32823: {}, 16419: {}, 16820: {}, 16822: {}, 16599: {}, 16631: {}, 16787: {}, 16794: {}, 16610: {}, 16760: {},
        16382: {}, 20991: {}, 19424: {}, 36486: {}, 30645: {}, 34585: {}, 32859: {}, 37458: {}, 37984: {}, 25782: {},
        **{skill_id: {} for skill_id in range(16933, 16944 + 1)},
        **{skill_id: {} for skill_id in (16803, 16802, 16801, 16800, 17043, 19423)},
        **{skill_id: dict(bind_dot=11447) for skill_id in (17058, 17060)},
        26934: dict(bind_dot=19555)
    }
}


class 项王击鼎秘章(Skill):
    damage_addition_extra = 256


class 霸王加成(项王击鼎秘章):
    def record(self, actual_critical_strike, actual_damage, parser):
        if stack := parser.current_buff_stacks.get((71047, 1)):
            parser.refresh_target_buff(70188, 10 * stack)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 10 * stack, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 闹须弥秘章(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_dot_ticks.get(70364):
            parser.refresh_target_buff(70188, 50)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 50, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


MOBILE_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        101198: {}, 101200: {}, 101080: {}, 101110: {}, 101109: {}, 101108: {}, 101260: {}, 101259: {}, 101257: {},
        101258: {}, 101256: {},
    },
    项王击鼎秘章: {
        101001: {}, 101000: {}, 100999: {}
    },
    霸王加成: {
        101050: {}
    },
    闹须弥秘章: {
        101068: dict(bind_dot=70364)
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
