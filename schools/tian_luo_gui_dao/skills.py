from typing import Dict

from base.skill import Skill, Dot


class 杀机断魂移除(Skill):
    final_buff = -24668

    def record(self, critical, parser):
        parser.clear_buff(self.final_buff, 1)


class 杀机断魂千机变(杀机断魂移除):
    def record(self, critical, parser):
        if buff_stack := parser.current_buff_stacks.get((27457, 1)):
            parser.refresh_buff(self.final_buff, 1, buff_stack)


class 杀机断魂天绝地灭(杀机断魂移除):
    def record(self, critical, parser):
        if parser.current_buff_stacks.get((16236, 1)):
            parser.refresh_buff(self.final_buff, 1, 6)
        elif parser.current_buff_stacks.get((16235, 1)):
            parser.refresh_buff(self.final_buff, 1, 4)
        elif parser.current_buff_stack.get((16234, 1)):
            parser.refresh_buff(self.final_buff, 1, 2)


class 杀机断魂暗藏杀机(杀机断魂移除):
    def record(self, critical, parser):
        parser.refresh_buff(self.final_buff, 1, 3)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        3121: dict(damage_addition=205),
        3105: {}, 3223: {}, 3228: {}, 3313: {}, 3393: {}, 3480: {}, 25774: {}, 30727: {}, 30894: {}, 32885: {},
        36502: {}, 3401: {}, 3404: {}, 3819: {}, 3824: {}, 37384: {},
        21266: dict(bind_dot=14611)
    },
    Dot: {14611: {}},
    杀机断魂移除: {33145: {}},
    杀机断魂千机变: {33142: {}},
    杀机断魂天绝地灭: {33143: {}},
    杀机断魂暗藏杀机: {33144: {}}

}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
