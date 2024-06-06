from typing import Dict

from base.skill import Skill


class 啸日(Skill):
    final_buff = -1

    def record(self, critical, parser):
        super().record(critical, parser)
        if parser.current_buff_stacks.get((self.final_buff, 1)):
            parser.clear_buff(self.final_buff, 1)
        else:
            parser.refresh_buff(self.final_buff, 1)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        **{skill_id: dict(damage_addition=205) for skill_id in (18381, 1795)},
        1594: {}, 1595: {}, 1598: {}, 1706: {}, 1707: {}, 2896: {}, 13471: {}, 18299: {}, 18317: {}, 18685: {},
        18991: {}, 25776: {}, 26673: {}, 30861: {}, 32821: {}, 32967: {}, 34984: {}, 35051: {}
    },
    啸日: {1656: {}},
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill