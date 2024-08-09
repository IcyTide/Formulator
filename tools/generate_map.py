from collections import defaultdict

from general.buffs import GENERAL_BUFFS
from general.skills import GENERAL_SKILLS
from schools import SUPPORT_SCHOOLS
from tools import save_code


def prepare_skills():
    skills = defaultdict(lambda: defaultdict(list))
    dots = defaultdict(lambda: defaultdict(list))
    for school in SUPPORT_SCHOOLS.values():
        attribute = school.attribute()
        for skill_id, skill in school.skills.items():
            if skill_id in GENERAL_SKILLS:
                continue
            if skill.damage_call:
                for buff_id, buff in school.buffs.items():
                    if buff_id in GENERAL_BUFFS:
                        continue
                    if buff.add_all(attribute, skill):
                        skills[school.id][skill_id].append(abs(buff_id))
            if skill.bind_dot:
                dots[school.id][skill.bind_dot].append(skill_id)

    return skills, dots


SKILLS, DOTS = prepare_skills()
save_code("school_skill2buff", SKILLS)
save_code("school_dot2skill", DOTS)