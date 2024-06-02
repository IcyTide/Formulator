from typing import Dict

from base.skill import Damage, DotDamage, DotSkill


class 横刀断浪流血(DotSkill):
    bind_buff: int = -24222
    stack: int

    def record(self, critical, parser):
        bind_skill = parser.current_school.skills[self.bind_skill]
        bind_buff = self.bind_buff
        for level in range(self.stack):
            parser.clear_target_buff(bind_buff, level + 1)
        parser.refresh_target_buff(bind_buff, self.stack, 1)
        parser.current_dot_ticks[self.bind_skill] = bind_skill.tick
        parser.current_dot_stacks[self.bind_skill] = self.stack
        parser.current_dot_snapshot[self.bind_skill] = parser.current_buff_stacks.copy()


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        33146: {}, 32974: {}, 32975: {}, 32510: {}, 32246: {}, 32766: {}, 32149: {}, 32150: {}, 32151: {}, 32154: {},
        32167: {}, 32348: {}, 32602: {}, 32603: {}, 32604: {}, 32234: {}, 32235: {}, 32236: {}, 32237: {}, 32238: {},
        32239: {}, 32891: {}, 32892: {}, 32357: {}, 36118: {}, 33239: {}
    },
    DotDamage: {
        24443: {},
        27820: {"bind_skill": 36851}
    },
    DotSkill: {
        36851: {"bind_skill": 27820},
    },
    横刀断浪流血: {skill_id: {"bind_skill": 24443, "stack": 6 - i} for i, skill_id in enumerate(range(32869, 32874 + 1))}
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
