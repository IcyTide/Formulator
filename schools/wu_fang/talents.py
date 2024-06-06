from typing import Dict

from base.gain import Gain
from base.skill import Skill
from base.talent import Talent
from base.recipe import ExtraTickRecipe


class 鸩羽(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id == 27557:
            skill.magical_critical_strike_rate_extra += 1000

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 27557:
            skill.magical_critical_strike_rate_extra -= 1000


class 疾根(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[20052].tick_extra += 1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[20052].tick_extra -= 1


TALENT_GAINS: Dict[int, Talent] = {
    28343: Talent("淮茵"),
    28338: Talent("怯邪"),
    28344: Talent("鸩羽", [鸩羽(skill_id=27556, skill_recipe=27556)]),
    28361: Talent("结草"),
    29498: Talent("灵荆"),
    29499: Talent("苦苛"),
    28406: Talent("遍休"),
    28410: Talent("坚阴"),
    28413: Talent("相使"),
    28419: Talent("凄骨"),
    28432: Talent("疾根", [ExtraTickRecipe(1, 20052, 0)]),
    28433: Talent("紫伏"),
    30734: Talent("折枝拂露"),
    28443: Talent("甘遂"),
    32896: Talent("应理与药"),
    28426: Talent("养荣")
}

TALENTS = [
    [28343, 28338],
    [28344],
    [28361],
    [29498],
    [29499, 28406],
    [28410],
    [28413],
    [28419],
    [28432],
    [28433, 30734],
    [28443],
    [32896, 28426]
]
TALENT_DECODER = {talent_id: talent.talent_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
