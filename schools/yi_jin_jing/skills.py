from typing import Dict

from base.skill import Skill, Dot


class 明法判定(Skill):
    final_buff = 19635
    bind_buff_1 = 890
    bind_buff_2 = 12479

    def record(self, critical, parser):
        if buff_level := parser.current_target_buff_stacks.get((self.bind_buff_1, 1)):
            parser.refresh_target_buff(self.final_buff, buff_level)
        elif buff_level := parser.current_target_buff_stacks.get((self.bind_buff_2, 1)):
            parser.refresh_target_buff(self.final_buff, buff_level)


class 明法移除(Skill):
    final_buff = 19635

    def record(self, critical, parser):
        for buff_id, buff_level in parser.current_target_buff_stacks:
            if buff_id == self.final_buff:
                parser.clear_target_buff(self.final_buff, buff_level)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        11: dict(damage_addition=205),
        236: {}, 271: {}, 14951: {}, 17641: {}, 19090: {}, 25766: {}, 28619: {}, 29516: {}, 32656: {}, 32659: {},
        32660: {}, 32887: {}, 3814: {}, 3817: {},3848: {}, 3849: {}, 3850: {}, 13685: {}
        3810: dict(bind_dot=743)
    },
    Dot: {743: dict(extra_tick=3)},
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
