from typing import Dict

from base.dot import Dot
from base.gain import Gain
from base.recipe import PhysicalCriticalRecipe, ChannelIntervalRecipe
from base.skill import Skill


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


TALENTS: Dict[int, Gain] = {
    6437: Gain("迅电流光", [PhysicalCriticalRecipe((1000, 100), 3095, 3095)]),
    6473: Gain("千里无痕"),
    28366: Gain("寒江夜雨"),
    21724: Gain("掠影穹苍"),
    37324: Gain("蹑景追风"),
    6451: Gain("聚精凝神"),
    14851: Gain("逐一击破"),
    28903: Gain("穿林打叶", [穿林打叶(), ChannelIntervalRecipe(1.5, 3098, 3098)]),
    6461: Gain("秋风散影"),
    37325: Gain("牢甲利兵"),
    14850: Gain("妙手连环", [妙手连环(skill_id=3096, recipe_type=3096)]),
    18672: Gain("百里追魂"),
    30588: Gain("凝形逐踪")
}

TALENT_CHOICES = [
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
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
