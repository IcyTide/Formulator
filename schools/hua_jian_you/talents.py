from typing import Dict

from base.buff import Buff
from base.gain import Gain
from base.skill import Skill
from schools.hua_jian_you.skills import 快雪时晴秘章


class 陶然(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 快雪时晴秘章):
                skill.pre_buffs[70161] = {10: 1}
                skill.post_buffs[70161] = {10: -1}
                skill.pre_buffs[70167] = {10: 1}
                skill.post_buffs[70167] = {10: -1}

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 快雪时晴秘章):
                skill.pre_buffs[70161].pop(10)
                skill.post_buffs[70161].pop(10)
                skill.pre_buffs[70167].pop(10)
                skill.post_buffs[70167].pop(10)


class 忘机(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[100043].pre_target_buffs[70188] = {50: 1}
        skills[100043].post_target_buffs[70188] = {50: -1}
        skills[101593].pre_buffs[70161] = {30: 1}
        skills[101593].post_buffs[70161] = {30: -1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[100043].pre_target_buffs[70188].pop(50)
        skills[100043].post_target_buffs[70188].pop(50)
        skills[101593].pre_buffs[70161].pop(30)
        skills[101593].post_buffs[70161].pop(30)


TALENTS: Dict[int, Gain] = {
    5756: Gain("烟霞", recipes=[(1295, 1)]),
    32489: Gain("青冠"),
    17510: Gain("倚天"),
    37267: Gain("墨海临源"),
    5762: Gain("青歌", recipes=[(5497, 1)]),
    21744: Gain("折花"),
    32477: Gain("雪中行"),
    16855: Gain("清流", buff_ids=[-12588]),
    26692: Gain("钟灵"),
    6682: Gain("流离"),
    32480: Gain("雪弃"),
    32469: Gain("焚玉"),
    26669: Gain("故幽", recipes=[(recipe_id, 1) for recipe_id in (2439, 2440, 2441, 2442, 2443, 3151)]),
    14643: Gain("涓流"),

    100488: 陶然("陶然"),
    100489: 忘机("忘机"),
    100491: Gain("渡泉"),
    100051: Gain("乱洒青荷")
}

TALENT_CHOICES = [
    [5756, 100488],
    [32489, 100489],
    [17510, 100491],
    [37267, 5762, 100051],
    [21744],
    [32477],
    [16855],
    [26692],
    [6682],
    [32480],
    [32469, 26669],
    [14643]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
