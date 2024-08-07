from typing import Dict

from base.buff import Buff
from base.gain import Gain
from base.recipe import MagicalCriticalRecipe
from base.skill import Skill
from base.talent import Talent
from schools.hua_jian_you.skills import 快雪时晴秘章


class 清流(Gain):
    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[-12588].activate = True

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[-12588].activate = False


class 陶然(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 快雪时晴秘章):
                skill.pre_buffs[(70161, 10)] = 1
                skill.post_buffs[(70161, 10)] = -1
                skill.pre_buffs[(70167, 10)] = 1
                skill.post_buffs[(70167, 10)] = -1

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 快雪时晴秘章):
                skill.pre_buffs.pop((70161, 10))
                skill.post_buffs.pop((70161, 10))
                skill.pre_buffs.pop((70167, 10))
                skill.post_buffs.pop((70167, 10))


class 忘机(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[100043].pre_target_buffs[(70188, 50)] = 1
        skills[100043].post_target_buffs[(70188, 50)] = -1
        skills[101593].pre_buffs[(70161, 30)] = 1
        skills[101593].post_buffs[(70161, 30)] = -1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[100043].pre_target_buffs.pop((70188, 50))
        skills[100043].post_target_buffs.pop((70188, 50))
        skills[101593].pre_buffs.pop((70161, 30))
        skills[101593].post_buffs.pop((70161, 30))


TALENT_GAINS: Dict[int, Talent] = {
    5756: Talent("烟霞", [MagicalCriticalRecipe((1000, 102), 179, 179)]),
    32489: Talent("青冠"),
    17510: Talent("倚天"),
    37267: Talent("墨海临源"),
    21744: Talent("折花"),
    32477: Talent("雪中行"),
    16855: Talent("清流", [清流()]),
    26692: Talent("钟灵"),
    6682: Talent("流离"),
    32480: Talent("雪弃"),
    32469: Talent("焚玉"),
    26669: Talent("故幽", [
        MagicalCriticalRecipe((1500, 154), skill_id, skill_recipe)
        for skill_id, skill_recipe in ((186, 186), (6134, 0), (6135, 0), (6136, 0), (0, 32409))
    ]),
    14643: Talent("涓流"),

    100488: Talent("陶然", [陶然()]),
    100489: Talent("忘机", [忘机()]),
    100491: Talent("渡泉"),
    100051: Talent("乱洒青荷")
}

TALENTS = [
    [5756, 100488],
    [32489, 100489],
    [17510, 100491],
    [37267, 100051],
    [21744],
    [32477],
    [16855],
    [26692],
    [6682],
    [32480],
    [32469, 26669],
    [14643]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
