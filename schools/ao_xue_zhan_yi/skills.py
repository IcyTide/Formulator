from typing import Dict

from base.skill import Skill, DotSkill, DotDamage, Damage
from general.skills import GENERAL_SKILLS


class 战意判定(Skill):
    final_buff = -12608
    bind_buff = -1

    def record(self, critical, parser):
        if buff_level := parser.current_buff_stacks.get((self.bind_buff, 1)):
            parser.refresh_buff(self.final_buff, buff_level)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        12: {}, 431: {}, 6526: {}, 14882: {}, 15002: {}, 24898: {}, 25772: {}, 31031: {}, 32820: {}, 37618: {},
        18207: {"post_buffs": {(-1, 1): 1}},
        18603: {"post_buffs": {(-1, 1): 2}},
        409: {"post_buffs": {(-1, 1): 3}},
        18773: {"post_buffs": {(-1, 1): -3}},
    },
    DotDamage: {
        3442: {"bind_skill": 702}
    },
    type("", (Damage, DotSkill), {}): {
        702: {"bind_skill": 3442}
    },
    DotSkill: {
        18591: {"bind_skill": 3442}
    },
    战意判定: {18740: {}},
    Skill: {
        skill_id: {"post_buffs": {(-1, 1): 5}} for skill_id in (1850, 1861)
    }
}
SKILLS = {}
SKILLS.update(GENERAL_SKILLS)
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
