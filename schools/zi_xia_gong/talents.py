from typing import Dict

from base.buff import Buff
from base.gain import Gain
from base.recipe import DamageAdditionRecipe, MagicalCriticalRecipe
from base.skill import Skill


class 跬步(Gain):
    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[-12550].activate = True
        buffs[-12551].activate = True

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[-12550].activate = False
        buffs[-12551].activate = False


class 固本(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2681].post_buffs.pop((2757, 1))
        skills[2681].post_buffs[(2757, 3)] = 1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2681].post_buffs.pop((2757, 3))
        skills[2681].post_buffs[(2757, 1)] = 1


class 若水(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2681].post_buffs.pop((2757, 1))
        skills[2681].post_buffs[(2757, 2)] = 1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2681].post_buffs.pop((2757, 2))
        skills[2681].post_buffs[(2757, 1)] = 1


class 破势(Gain):
    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[17918].activate = True

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[17918].activate = False


TALENTS: Dict[int, Gain] = {
    5840: Gain("雾锁", [DamageAdditionRecipe(102, 367, 367)]),
    5827: Gain("白虹", [MagicalCriticalRecipe((1000, 102), 367, 367)]),
    5823: Gain("心固"),
    5828: Gain("霜锋", [DamageAdditionRecipe(102, skill_id, skill_id) for skill_id in (301, 368)]),
    357: Gain("化三清"),
    5846: Gain("无形"),
    23614: Gain("归元"),
    5819: Gain("同尘"),
    18695: Gain("跬步", [跬步()]),
    32411: Gain("正气"),
    14834: Gain("抱阳"),
    18679: Gain("浮生"),
    24945: Gain("破势", [破势()]),
    18669: Gain("重光", [
        DamageAdditionRecipe(value, skill_id, 0)
        for skill_id, value in ((18650, 154), (18651, 307), (18652, 461), (18653, 614))
    ]),
    14613: Gain("固本", [固本()]),
    14598: Gain("若水", [若水()])
}

TALENT_CHOICES = [
    [5840, 5827],
    [5823, 5828],
    [357, 5846],
    [23614],
    [5819],
    [18695],
    [32411],
    [14834],
    [18679],
    [24945],
    [18669],
    [14613, 14598]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
