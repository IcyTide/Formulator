from typing import Dict

from base.attribute import Attribute
from base.buff import Buff
from base.dot import Dot
from base.gain import Gain
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


TALENTS: Dict[int, Gain] = {
    28343: Gain("淮茵"),
    28338: Gain("怯邪"),
    27530: Gain("川谷", [DamageAdditionRecipe(102, 27551, 27551)]),
    28344: Gain("鸩羽", [鸩羽(1000, 27556, 27556)]),
    28361: Gain("结草"),
    29498: Gain("灵荆"),
    29499: Gain("苦苛"),
    28406: Gain("遍休"),
    28410: Gain("坚阴"),
    28413: Gain("相使"),
    28419: Gain("凄骨"),
    28432: Gain("疾根", [ExtraTickRecipe(1, 20052)]),
    28433: Gain("紫伏"),
    28431: Gain("避奚"),
    30734: Gain("折枝拂露"),
    28443: Gain("甘遂"),
    28458: Gain("炮阳"),
    28415: Gain("荆障"),
    32896: Gain("应理与药"),
    28426: Gain("养荣"),

    101419: Gain("鬼门", [鬼门()]),
    101422: Gain("神莹"),
    101423: Gain("济世"),
    101370: Gain("苍棘缚地"),
}

TALENT_CHOICES = [
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
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
