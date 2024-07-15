from typing import Dict

from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from base.recipe import ExtraTickRecipe, DamageAdditionRecipe
from base.skill import Skill
from base.dot import Dot
from base.talent import Talent
from schools.wu_fang.skills import 鬼门加成


class 鸩羽(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id == 27557:
            skill.poison_critical_strike_rate += self.value

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 27557:
            skill.poison_critical_strike_rate -= self.value


class 鬼门(Gain):
    def add(self, attribute: Attribute, skills: Dict[int, Skill], dots: Dict[int, Dot], buffs: Dict[int, Buff]):
        鬼门加成.talent_activate = True

    def sub(self, attribute: Attribute, skills: Dict[int, Skill], dots: Dict[int, Dot], buffs: Dict[int, Buff]):
        鬼门加成.talent_activate = False


TALENT_GAINS: Dict[int, Talent] = {
    28343: Talent("淮茵"),
    28338: Talent("怯邪"),
    27530: Talent("川谷", [DamageAdditionRecipe(102, 27551, 27551)]),
    101419: Talent("鬼门", [鬼门()]),
    28344: Talent("鸩羽", [鸩羽(1000, 27556,27556)]),
    101422: Talent("神莹"),
    28361: Talent("结草"),
    101423: Talent("济世"),
    29498: Talent("灵荆"),
    101370: Talent("苍棘缚地"),
    29499: Talent("苦苛"),
    28406: Talent("遍休"),
    28410: Talent("坚阴"),
    28413: Talent("相使"),
    28419: Talent("凄骨"),
    28432: Talent("疾根", [ExtraTickRecipe(1, 20052)]),
    28433: Talent("紫伏"),
    28431: Talent("避奚"),
    30734: Talent("折枝拂露"),
    28443: Talent("甘遂"),
    28458: Talent("炮阳"),
    28415: Talent("荆障"),
    32896: Talent("应理与药"),
    28426: Talent("养荣")
}

TALENTS = [
    [28343, 28338, 27530, 101419],
    [28344, 101422],
    [28361, 101423],
    [29498, 101370],
    [29499, 28406],
    [28410],
    [28413],
    [28419],
    [28432],
    [28433, 30734, 28431],
    [28443, 28458, 28415],
    [32896, 28426]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
