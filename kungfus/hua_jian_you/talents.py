from typing import Dict, List

from base.gain import Gain
from base.skill import Skill
from kungfus.hua_jian_you.skills import 快雪时晴秘章


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


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            5756: Gain("烟霞", recipes=[(1295, 1)])
        },
        {
            17510: Gain("倚天")
        },
        {
            26692: Gain("钟灵")
        },
        {
            32469: Gain("焚玉"),
            5762: Gain("青歌", recipes=[(5497, 1)])
        },
        {
            14635: Gain("踏莲"),
            21744: Gain("折花")
        },
        {
            32477: Gain("雪中行")
        },
        {
            16855: Gain("清流")
        },
        {
            38972: Gain("青冠", recipes=[(5743, 1), (5744, 1)])
        },
        {
            6682: Gain("流离")
        },
        {
            30650: Gain("丹青"),
            32480: Gain("雪弃"),
            37065: Gain("活络")
        },
        {
            37267: Gain("墨海临源"),
            26669: Gain("故幽", recipes=[(recipe_id, 1) for recipe_id in (2439, 2440, 2441, 2442, 2443, 3151)])
        },
        {
            14643: Gain("涓流"),
            14965: Gain("南风吐月")
        }
    ],

    1: [
        {
            100488: 陶然("陶然")
        },
        {
            100489: 忘机("忘机")
        },
        {
            100491: Gain("渡泉")
        },
        {
            100051: Gain("乱洒青荷")
        }
    ]
}
