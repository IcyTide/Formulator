from typing import Dict

from base.skill import Damage, DotDamage, DotSkill


class 杀机断魂增伤(Damage):
    final_buff = -24668

    def pre_record(self, parser):
        super().pre_record(parser)
        if buff_stack := parser.current_buff_stacks.get((27457, 1)):
            parser.refresh_buff(self.final_buff, 1, buff_stack)

    def post_record(self, parser):
        super().post_record(parser)
        parser.clear_buff(self.final_buff, 1)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        3105: {}, 3121: {}, 3223: {}, 3228: {}, 3313: {}, 3393: {}, 3480: {}, 25774: {}, 30727: {}, 30894: {},
        32885: {}, 36502: {}
    },
    杀机断魂增伤: {
        3401: {}, 3404: {}, 3819: {}, 3824: {}, 37384: {}
    },
    DotDamage: {14611: {"bind_skill": 21266}},
    DotSkill: {21266: {"bind_skill": 14611}},
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
