from typing import Dict, List

from base.gain import Gain
from base.skill import Skill
from kungfus.hua_jian_you.skills import 快雪时晴秘章


class 钟灵(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[182].pre_buffs[28116] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[182].pre_buffs.pop(28116)


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
            32477: Gain("雪中行")
        },
        {
            17510: Gain("倚天"),
            5751: Gain("定式黑白")
        },
        {
            26692: 钟灵("钟灵")
        },
        {
            38954: Gain("焚玉"),
        },
        {
            21744: Gain("折花")
        },
        {
            24912: Gain("丹鼎", recipes=[(4661, 1)])
        },
        {
            16855: Gain("清流")
        },
        {
            38972: Gain("青冠", attributes=dict(neutral_attack_power_gain=102, strain_gain=102))
        },
        {
            6682: Gain("流离"),
            26694: Gain("碎玉")
        },
        {
            30650: Gain("丹青")
        },
        {
            37267: Gain("墨海临源"),
            26669: Gain("故幽", recipes=[(recipe_id, 1) for recipe_id in (2439, 2440, 2441, 2442, 2443, 3151)])
        },
        {
            14643: Gain("涓流")
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
