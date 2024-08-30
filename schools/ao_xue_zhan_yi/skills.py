from typing import Dict

from base.skill import Skill
from general.skills import GENERAL_SKILLS


class 战意判定(Skill):
    final_buff = -12608
    bind_buff = -1

    def record(self, actual_critical_strike, actual_damage, parser):
        if buff_level := parser.current_buff_stacks[self.bind_buff].get(1):
            parser.refresh_buff(self.final_buff, buff_level)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        12: dict(channel_interval=27),
        431: {}, 701: {}, 702: {}, 6525: {}, 6526: {}, 423: {}, 14882: {}, 15002: {}, 24898: {}, 25772: {}, 32820: {},
        37618: {}, 36568: {}, 18207: {}, 18208: {},
        400: dict(post_buffs={-1: {1: 1}}),
        18603: dict(post_buffs={-1: {1: 2}}),
        409: dict(post_buffs={-1: {1: 3}}),
        18773: dict(post_buffs={-1: {1: -3}}),
        31031: dict(post_buffs={-1: {1: 5}}),
        401: dict(bind_dot=12461),
        18591: dict(bind_dot=3442),
    },
    战意判定: {
        18740: {}
    }
}
SKILLS: Dict[int, Skill] = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        SKILLS[skill_id] = skill = skill_class(skill_id)
        skill.set_asset(attrs)
