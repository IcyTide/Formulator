from typing import Dict

from base.skill import Skill, Dot


class 逐一击破增伤(Skill):
    bind_buff = 1
    final_buff = -1

    def record(self, critical, parser):
        parser.refresh_buff(self.final_buff, 1)
        super().record(critical, parser)
        parser.clear_buff(self.final_buff, 1)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        3121: dict(damage_addition=205),
        3222: {}, 3227: {}, 22789: {}, 25775: {}, 32884: {}, 37616: {},
        3478: dict(bind_dot=19625)
    },
    Dot: {
        2237: dict(tick_extra=1),
        19625: {}
    },
    逐一击破增伤: {
        3095: {}, 3187: {}, 6920: {}, 33870: {}, 37504: {},
        3125: dict(bind_dot=2237)
    }
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
