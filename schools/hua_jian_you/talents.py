from typing import Dict

from base.attribute import Attribute
from base.buff import Buff
from base.dot import Dot
from base.gain import Gain
from base.recipe import MagicalCriticalRecipe
from base.skill import Skill
from base.talent import Talent
from schools.hua_jian_you.skills import 忘机加成


class 清流(Gain):
    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[-12588].activate = True

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[-12588].activate = False


class 忘机(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[100041].pre_buffs[(70161, 30)] = 1
        skills[100041].post_buffs[(70161, 30)] = -1

    def add(self, attribute: Attribute, skills: Dict[int, Skill], dots: Dict[int, Dot], buffs: Dict[int, Buff]):
        忘机加成.talent_activate = True
        super().add(attribute, skills, dots, buffs)

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[100041].pre_buffs.pop((70161, 30))
        skills[100041].post_buffs.pop((70161, 30))

    def sub(self, attribute: Attribute, skills: Dict[int, Skill], dots: Dict[int, Dot], buffs: Dict[int, Buff]):
        忘机加成.talent_activate = False
        super().sub(attribute, skills, dots, buffs)


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

    100488: Talent("陶然"),
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
