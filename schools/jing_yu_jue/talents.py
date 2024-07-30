from typing import Dict

from base.dot import Dot
from base.gain import Gain
from base.recipe import PhysicalCriticalRecipe, ChannelIntervalRecipe
from base.skill import Skill
from base.talent import Talent


class 穿林打叶(Gain):
    def add_dots(self, dots: Dict[int, Dot]):
        dots[2237].interval_extra -= 16
        dots[2237].tick_extra = 5

    def sub_dots(self, dots: Dict[int, Dot]):
        dots[2237].interval_extra += 16
        dots[2237].tick_extra = 1


class 妙手连环(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id != 3096 and skill.skill_id != 18801:
            skill.physical_shield_gain_extra -= 512

    def sub_skill(self, skill: Skill):
        if skill.skill_id != 3096 and skill.skill_id != 18801:
            skill.physical_shield_gain_extra += 512


# class 逐一击破(Gain):
#     def add_skills(self, skills: Dict[int, Skill]):
#         for skill_id, skill in skills.items():
#             if skill.event_mask_2 & 65536:
#                 skills[skill_id].damage_addition += 103 + 103
#
#     def sub_skills(self, skills: Dict[int, Skill]):
#         for skill_id, skill in skills.items():
#             if skill.event_mask_2 & 65536:
#                 skills[skill_id].damage_addition -= 103 + 103


TALENT_GAINS: Dict[int, Talent] = {
    6437: Talent("迅电流光", [PhysicalCriticalRecipe((1000, 100), 3095, 3095)]),
    6473: Talent("千里无痕"),
    28366: Talent("寒江夜雨"),
    21724: Talent("掠影穹苍"),
    37324: Talent("蹑景追风"),
    6451: Talent("聚精凝神"),
    14851: Talent("逐一击破"),
    28903: Talent("穿林打叶", [穿林打叶(), ChannelIntervalRecipe(1.5, 3098, 3098)]),
    6461: Talent("秋风散影"),
    37325: Talent("牢甲利兵"),
    14850: Talent("妙手连环", [妙手连环(skill_id=3096, skill_recipe=3096)]),
    18672: Talent("百里追魂"),
    30588: Talent("凝形逐踪")
}

TALENTS = [
    [6437],
    [6473],
    [28366],
    [21724],
    [37324],
    [6451],
    [14851],
    [28903],
    [6461],
    [37325],
    [14850],
    [18672, 30588]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
