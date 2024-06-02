from typing import Dict

from base.skill import Skill, Damage, DotDamage, DotSkill


class 盾压(Damage):
    def record(self, critical, parser):
        if parser.current_buff_stacks.get((8474, 13)):
            self.post_buffs[(-1, 1)] = 15 * 2
        else:
            self.post_buffs[(-1, 1)] = 15

        super().record(critical, parser)


class 绝刀(Damage):
    final_buff = -9052
    bind_buff = -1

    def record(self, critical, parser):
        current_rage = parser.current_buff_stacks.get((-1, 1), 0)
        cost_rage = min(current_rage, 50)
        buff_level = cost_rage // 10 - 1
        if buff_level > 0:
            parser.refresh_buff(self.final_buff, buff_level)
        if parser.current_buff_stacks.get((8451, 1)):
            self.post_buffs[(-1, 1)] = 0
        elif parser.current_buff_stacks.get((8474, 13)):
            self.post_buffs[(-1, 1)] = 0
        else:
            self.post_buffs[(-1, 1)] = -cost_rage
        super().record(critical, parser)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        32745: {}, 13039: {}, 36065: {}, 36482: {}, 37253: {}, 34673: {}, 34674: {}, 34714: {}, 37448: {}, 30925: {},
        30926: {}, 30857: {}, 30858: {}, 30859: {}, 23284: {}, 23285: {}, 23286: {}, 23287: {}, 23294: {}, 25780: {},
        **{skill_id: {"post_buffs": {(-1, 1): 10}} for skill_id in (13106, 13160, 13161)},
        13099: {"post_buffs": {(-1, 1): 15}},
        13463: {"post_target_buffs": {(-8248, 1): 1}},
        13044: {"post_buffs": {(-1, 1): 5}},
        13092: {"post_buffs": {(-1, 1): -15}},
        28479: {"post_buffs": {(-1, 1): -5}}
    },
    DotDamage: {8249: {}},
    DotSkill: {
        29188: {
            "bind_skill": 8249,
            "post_target_buffs": {(-8248, 1): -1}
        }
    },
    盾压: {19409: {}},
    绝刀: {13075: {}},
    Skill: {
        13040: {"post_buffs": {(-1, 1): 10 + 15}},
        16727: {"post_buffs": {(-1, 1): 3}}
    }
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
