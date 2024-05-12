from typing import Dict

from base.gain import Gain
from base.skill import Skill


class 黯影(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (6218, 25917, 2509, 2295):
            skills[skill_id].attack_power_cof_gain *= 1.25

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (6218, 25917, 2509, 2295):
            skills[skill_id].attack_power_cof_gain /= 1.25


class 重蛊(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (29573, 25044, 30918):
            skills[skill_id].skill_damage_addition += 154

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (29573, 25044, 30918):
            skills[skill_id].skill_damage_addition -= 154


class 曲致(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[25917].tick += 2

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[25917].tick -= 2


class 引魂(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2223].bind_buffs.append(16102)  # type: ignore

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2223].bind_buffs.remove(16102)  # type: ignore


TALENT_GAINS: Dict[int, Gain] = {
    6620: Gain("蝎毒"),
    6649: Gain("食髓"),
    6629: 黯影("黯影"),
    6879: Gain("虫兽"),
    34388: 重蛊("重蛊"),
    34640: Gain("忘情"),
    30088: Gain("嗜蛊"),
    25040: 曲致("曲致"),
    25018: Gain("荒息"),
    29545: Gain("篾片蛊"),
    18325: 引魂("引魂"),
    25043: Gain("连缘蛊")
}

TALENTS = [
    [6620],
    [6649],
    [6629],
    [6879],
    [34388],
    [34640],
    [30088],
    [25040],
    [25018],
    [29545],
    [18325],
    [25043]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
