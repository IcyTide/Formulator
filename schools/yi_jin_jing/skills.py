from typing import Dict

from base.skill import Skill, Damage, DotDamage


class 明法判定(Skill):
    final_buff = 19635
    bind_buff = 890

    def record(self, critical, parser):
        if buff_level := parser.current_target_buff_stacks.get((self.bind_buff, 1)):
            parser.refresh_target_buff(self.final_buff, buff_level)


class 明法移除(Skill):
    final_buff = 19635
    bind_buff = 890

    def record(self, critical, parser):
        buff_level = parser.current_target_buff_stacks.get((self.bind_buff, 1), 0)
        for level in range(buff_level):
            parser.clear_target_buff(self.final_buff, level + 1)


class 众嗔增伤(Damage):
    final_buff = -13910

    def pre_record(self, parser):
        super().pre_record(parser)
        if 743 in parser.current_dot_ticks:
            parser.refresh_buff(self.final_buff, 1)

    def post_record(self, parser):
        super().post_record(parser)
        parser.clear_buff(self.final_buff, 1)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        11: dict(damage_addition=205),
        236: {}, 271: {}, 14951: {}, 17641: {}, 19090: {}, 25766: {}, 28619: {}, 29516: {}, 32656: {}, 32659: {},
        32660: {}, 32887: {}, 3814: {}, 3817: {},
        3810: dict(bind_dot=743)
    },
    DotDamage: {743: dict(extra_tick=3)},
    众嗔增伤: {3848: {}, 3849: {}, 3850: {}, 13685: {}},
    明法判定: {26989: {}},
    明法移除: {26991: {}},
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
