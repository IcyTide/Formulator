from collections import defaultdict

from general.buffs import GENERAL_BUFFS
from general.skills import GENERAL_SKILLS
from schools import SUPPORT_SCHOOLS
from tools import save_code


def prepare_skills():
    school_buffs = {}
    skill_buffs = {}
    dot_buffs = {}
    dot_bind_skills = {}
    dot_consume_skills = {}
    for school in SUPPORT_SCHOOLS.values():
        school_buffs[school.id] = defaultdict(list)
        skill_buffs[school.id] = {}
        dot_buffs[school.id] = {}
        dot_bind_skills[school.id] = {}
        dot_consume_skills[school.id] = {}
        for buff_id, buff in school.buffs.items():
            if buff_id in GENERAL_BUFFS:
                continue
            for buff_level in range(buff.max_level):
                buff.buff_level = buff_level + 1
                if buff.attributes:
                    school_buffs[school.id][buff_id].append(buff.buff_level)
        for dot_id, dot in school.dots.items():
            dot_bind_skills[school.id][dot_id] = defaultdict(list)
            dot_consume_skills[school.id][dot_id] = defaultdict(list)

        for skill_id, skill in school.skills.items():
            if skill_id in GENERAL_SKILLS:
                continue
            if skill.damage_call:
                skill_buffs[school.id][skill_id] = defaultdict(list)
                for buff_id, buff in school.buffs.items():
                    if buff_id in GENERAL_BUFFS:
                        continue
                    if buff_id in school_buffs[school.id]:
                        continue
                    for buff_level in range(buff.max_level):
                        buff.buff_level = buff_level + 1
                        for recipe_key in buff.recipes.items():
                            recipe = school.recipes[recipe_key]
                            if recipe.check_skill(skill):
                                skill_buffs[school.id][skill_id][buff_id].append(buff.buff_level)
                                break
            if skill.bind_dot:
                dot_buffs[school.id][skill_id] = defaultdict(list)
                for buff_id, buff in school.buffs.items():
                    if buff_id in GENERAL_BUFFS:
                        continue
                    if buff_id in school_buffs[school.id]:
                        continue
                    for buff_level in range(buff.max_level):
                        buff.buff_level = buff_level + 1
                        for recipe_key in buff.recipes.items():
                            recipe = school.recipes[recipe_key]
                            if recipe.check_skill(skill):
                                dot_buffs[school.id][skill_id][buff_id].append(buff.buff_level)
                                break
            for skill_level in range(skill.max_level):
                skill.skill_level = skill_level + 1
                if skill.bind_dot:
                    dot_bind_skills[school.id][skill.bind_dot][skill_id].append(skill.skill_level)
                if skill.consume_dot:
                    dot_consume_skills[school.id][skill.consume_dot][skill_id].append(skill.skill_level)
    return school_buffs, skill_buffs, dot_buffs, dot_bind_skills, dot_consume_skills


SCHOOL_BUFFS, SKILL_BUFFS, DOT_BUFFS, DOT_BIND_SKILLS, DOT_CONSUME_SKILLS = prepare_skills()
save_code("school_buffs", SCHOOL_BUFFS)
# save_code("skill_buffs", SKILL_BUFFS)
# save_code("dot_buffs", DOT_BUFFS)
save_code("dot_bind_skills", DOT_BIND_SKILLS)
save_code("dot_consume_skills", DOT_CONSUME_SKILLS)
