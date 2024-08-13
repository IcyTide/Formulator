from typing import Dict

from base.attribute import Attribute
from base.buff import Buff
from base.dot import Dot
from base.gain import Gain, Gains
from base.recipe import ExtraTickRecipe, DamageAdditionRecipe
from base.skill import Skill
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


TALENT_GAINS: Dict[int, Gains] = {
    28343: Gains("淮茵"),
    28338: Gains("怯邪"),
    27530: Gains("川谷", [DamageAdditionRecipe(102, 27551, 27551)]),
    28344: Gains("鸩羽", [鸩羽(1000, 27556, 27556)]),
    28361: Gains("结草"),
    29498: Gains("灵荆"),
    29499: Gains("苦苛"),
    28406: Gains("遍休"),
    28410: Gains("坚阴"),
    28413: Gains("相使"),
    28419: Gains("凄骨"),
    28432: Gains("疾根", [ExtraTickRecipe(1, 20052)]),
    28433: Gains("紫伏"),
    28431: Gains("避奚"),
    30734: Gains("折枝拂露"),
    28443: Gains("甘遂"),
    28458: Gains("炮阳"),
    28415: Gains("荆障"),
    32896: Gains("应理与药"),
    28426: Gains("养荣"),

    101419: Gains("鬼门", [鬼门()]),
    101422: Gains("神莹"),
    101423: Gains("济世"),
    101370: Gains("苍棘缚地"),
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
