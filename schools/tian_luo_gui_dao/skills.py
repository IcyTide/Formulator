from typing import Dict

from base.skill import Skill
from general.skills import GENERAL_SKILLS


class 杀机断魂移除(Skill):
    final_buff = -24668

    def record(self, actual_critical_strike, actual_damage, parser):
        parser.clear_buff(self.final_buff, 1)


class 杀机断魂千机变(杀机断魂移除):
    def record(self, actual_critical_strike, actual_damage, parser):
        if buff_stack := parser.current_buff_stacks[27457].get(1):
            parser.refresh_buff(self.final_buff, 1, buff_stack)


class 杀机断魂天绝地灭(杀机断魂移除):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[16236].get(1):
            parser.refresh_buff(self.final_buff, 1, 6)
        elif parser.current_buff_stacks[16235].get(1):
            parser.refresh_buff(self.final_buff, 1, 4)
        elif parser.current_buff_stacks[16234].get(1):
            parser.refresh_buff(self.final_buff, 1, 2)


class 杀机断魂暗藏杀机(杀机断魂移除):
    def record(self, actual_critical_strike, actual_damage, parser):
        parser.refresh_buff(self.final_buff, 1, 3)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        3121: {}, 32885: {}, 3105: {}, 18776: {}, 3223: {}, 3228: {}, 3313: {}, 3393: {}, 3480: {}, 25774: {},
        30727: {}, 30894: {}, 36502: {}, 3401: {}, 3404: {}, 3819: {}, 3824: {}, 37384: {}, 18677: {}, 28441: {},
        21266: dict(bind_dot=14611)
    },
    杀机断魂移除: {33145: {}},
    杀机断魂千机变: {33142: {}},
    杀机断魂天绝地灭: {33143: {}},
    杀机断魂暗藏杀机: {33144: {}}
}
SKILLS: Dict[int, Skill] = {**GENERAL_SKILLS}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        SKILLS[skill_id] = skill = skill_class(skill_id)
        skill.set_asset(attrs)
