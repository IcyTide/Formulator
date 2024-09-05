from typing import Dict

from base.dot import Dot
from base.gain import Gain
from base.skill import Skill
from schools.wu_fang.skills import 鬼门加成


class 鬼门(Gain):
    @staticmethod
    def pre_effect(parser):
        if parser.current_dot_ticks.get(71171):
            parser.refresh_target_buff(70188, 10)

    @staticmethod
    def post_effect(parser):
        if parser.current_dot_ticks.get(71171):
            parser.refresh_target_buff(70188, 10, -1)

    def add_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 鬼门加成):
                skill.pre_effects.append(self.pre_effect)
                skill.post_effects.append(self.post_effect)

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 鬼门加成):
                skill.pre_effects.remove(self.pre_effect)
                skill.post_effects.remove(self.post_effect)


class 疾根(Gain):
    def add_dots(self, dots: Dict[int, Dot]):
        dots[20052].tick_add += 1

    def sub_dots(self, dots: Dict[int, Dot]):
        dots[20052].tick_add -= 1


TALENTS: Dict[int, Gain] = {
    28343: Gain("淮茵"),
    28338: Gain("怯邪"),
    27530: Gain("川谷", recipes=[(2541, 1)]),
    28344: Gain("鸩羽", recipes=[(2549, 1)]),
    28361: Gain("结草"),
    29498: Gain("灵荆"),
    29499: Gain("苦苛"),
    28406: Gain("遍休"),
    28410: Gain("坚阴"),
    28413: Gain("相使"),
    28419: Gain("凄骨"),
    28432: 疾根("疾根"),
    28433: Gain("紫伏"),
    28431: Gain("避奚"),
    30734: Gain("折枝拂露"),
    28443: Gain("甘遂"),
    28458: Gain("炮阳"),
    28415: Gain("荆障"),
    32896: Gain("应理与药"),
    28426: Gain("养荣"),

    101419: 鬼门("鬼门"),
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
