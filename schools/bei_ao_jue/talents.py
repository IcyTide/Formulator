from typing import Dict

from base.attribute import Attribute
from base.gain import Gain
from base.recipe import DamageAdditionRecipe, ChannelIntervalRecipe
from base.skill import Skill
from base.talent import Talent
from schools.bei_ao_jue.skills import 项王击鼎秘章


class 冥鼓(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id in (16758, 16759, 16760, 16382, 20991):
            skill.physical_shield_gain_extra += self.value[0]
        skill.damage_addition_extra += self.value[1]

    def add_skills(self, skills: Dict[int, Skill]):
        skills[32823].physical_shield_gain = [self.value[0], 0, 0, self.value[0]]
        skills[37458].physical_shield_gain = self.value[0]
        return super().add_skills(skills)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (16758, 16759, 16760, 16382, 20991):
            skill.physical_shield_gain_extra -= self.value[0]
        skill.damage_addition_extra -= self.value[1]

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[32823].physical_shield_gain = 0
        skills[37458].physical_shield_gain = 0
        super().sub_skills(skills)


class 阳关(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id in (16800, 16801, 16802, 16803, 16804, 17043, 19423, 19424):
            skill.physical_shield_gain_extra += self.value[0]
        skill.damage_addition += self.value[1]

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (16800, 16801, 16802, 16803, 16804, 17043, 19423, 19424):
            skill.physical_shield_gain_extra -= self.value[0]
        skill.damage_addition -= self.value[1]


class 星火(Gain):
    def add_attribute(self, attribute: Attribute):
        attribute.strength_gain += 102

    def sub_attribute(self, attribute: Attribute):
        attribute.strength_gain -= 102


class 征踏(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id, skill in skills.items():
            if isinstance(skill, 项王击鼎秘章) or skill_id in [101108, 101109, 101110] + list(range(101256, 101260)):
                skill.pre_target_buffs[(70188, 10)] = 1
                skill.post_target_buffs[(70188, 10)] = -1

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id, skill in skills.items():
            if isinstance(skill, 项王击鼎秘章) or skill_id in [101108, 101109, 101110] + list(range(101256, 101260)):
                skill.pre_target_buffs.pop((70188, 10))
                skill.post_target_buffs.pop((70188, 10))


class 裁魂(Gain):
    @staticmethod
    def pre_effect(parser):
        if 70454 in parser.current_target_buff_stacks:
            parser.refresh_target_buff(70188, 20)

    @staticmethod
    def post_effect(parser):
        if 70454 in parser.current_target_buff_stacks:
            parser.refresh_target_buff(70188, 20, -1)

    def add_skills(self, skills: Dict[int, Skill]):
        skills[101080].pre_effects.append(self.pre_effect)
        skills[101080].post_effects.append(self.post_effect)
        skills[101198].post_target_buffs[(70454, 1)] = 1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[101080].pre_effects.remove(self.pre_effect)
        skills[101080].post_effects.remove(self.post_effect)
        skills[101198].post_target_buffs.pop((70454, 1))


TALENT_GAINS: Dict[int, Talent] = {
    16691: Talent("龙息"),
    16847: Talent("归酣"),
    26904: Talent("冥鼓", [冥鼓((-512, 205), skill_id, skill_id) for skill_id in (16601, 16602)]),
    17042: Talent("阳关", [阳关((-205, 154), 16627, 16627)]),
    16799: Talent("霜天"),
    25633: Talent("含风"),
    32857: Talent("见尘"),
    37982: Talent("临江"),
    17047: Talent("分疆"),
    25258: Talent("掠关"),
    16728: Talent("星火", [星火()]),
    34677: Talent("绝河", [DamageAdditionRecipe(154, 16602, 16602)]),
    16737: Talent("楚歌"),
    17056: Talent("绝期", [ChannelIntervalRecipe(1.7, 17058, 0)]),
    16893: Talent("重烟"),
    21858: Talent("降麒式"),

    101296: Talent("征踏", [征踏()]),
    101299: Talent("裁魂", [裁魂()]),
    101300: Talent("霸王"),
    101015: Talent("上将军印")
}

TALENTS = [
    [16691, 101296],
    [16847, 101299],
    [26904, 17042, 101300],
    [16799, 101015],
    [25633],
    [32857, 37982],
    [17047],
    [25258, 16728, 34677],
    [16737],
    [17056],
    [16893],
    [21858]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
