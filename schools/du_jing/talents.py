from typing import Dict

from base.buff import Buff
from base.gain import Gain, Gains
from base.recipe import ChannelIntervalRecipe, ExtraTickRecipe
from base.skill import Skill


class 引魂(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2223].pet_buffs[(16102, 1)] = 1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2223].pet_buffs.pop((16102, 1))


class 虫兽(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2223].pre_buffs[(12497, 1)] = 1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2223].pre_buffs.pop((12497, 1))


class 嗜蛊(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2226].pre_buffs[(22232, 1)] = 1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2226].pre_buffs.pop((22232, 1))


class 曲致(Gain):
    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[-17988].activate = True

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[-17988].activate = False


TALENT_GAINS: Dict[int, Gains] = {
    6620: Gains("蝎毒"),
    6649: Gains("食髓"),
    6629: Gains("黯影", [
        ChannelIntervalRecipe(1.25, skill_id, 0)
        for skill_id in (6237, 6238, 6236, 13476, 26226, 18700, 34643, 37352)
    ]),
    6879: Gains("虫兽", [虫兽()]),
    34388: Gains("重蛊"),
    37952: Gains("不鸣"),
    34640: Gains("忘情"),
    30088: Gains("嗜蛊", [嗜蛊()]),
    25040: Gains("曲致", [曲致(), *[ExtraTickRecipe(2, skill_id, 0) for skill_id in (2296, 25917)]]),
    18330: Gains("固灵"),
    25018: Gains("荒息"),
    29545: Gains("篾片蛊"),
    18325: Gains("引魂", [引魂()]),
    25043: Gains("连缘蛊")
}

TALENTS = [
    [6620],
    [6649],
    [6629],
    [6879],
    [34388],
    [34640, 37952],
    [30088],
    [25040, 18330],
    [25018],
    [29545],
    [18325],
    [25043]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
