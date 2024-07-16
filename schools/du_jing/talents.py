from typing import Dict

from base.buff import Buff
from base.gain import Gain
from base.recipe import ChannelIntervalRecipe, ExtraTickRecipe
from base.skill import Skill
from base.talent import Talent


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


class 曲致(Gain):
    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[-17988].activate = True

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[-17988].activate = False


TALENT_GAINS: Dict[int, Talent] = {
    6620: Talent("蝎毒"),
    6649: Talent("食髓"),
    6629: Talent("黯影", [
        ChannelIntervalRecipe(1.25, skill_id, 0)
        for skill_id in (6237, 6238, 6236, 13476, 26226, 18700, 34643, 37352)
    ]),
    6879: Talent("虫兽", [虫兽()]),
    34388: Talent("重蛊"),
    37952: Talent("不鸣"),
    34640: Talent("忘情"),
    30088: Talent("嗜蛊"),
    25040: Talent("曲致", [曲致(), ExtraTickRecipe(2, 25917, 0)]),
    25018: Talent("荒息"),
    29545: Talent("篾片蛊"),
    18325: Talent("引魂", [引魂()]),
    25043: Talent("连缘蛊")
}

TALENTS = [
    [6620],
    [6649],
    [6629],
    [6879],
    [34388],
    [34640, 37952],
    [30088],
    [25040],
    [25018],
    [29545],
    [18325],
    [25043]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
