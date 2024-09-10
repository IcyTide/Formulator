from general.recipes import *


class 商增加伤害3(ChannelIntervalRecipe):
    value = 1.03


class 商增加伤害4(ChannelIntervalRecipe):
    value = 1.04


class 商增加伤害5(ChannelIntervalRecipe):
    value = 1.05


class 阳春白雪_目标35减防(MagicalShieldGainRecipe):
    value = -307

    def add_skill(self, skill: Skill):
        if skill.skill_id in (14227, 14474):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (14227, 14474):
            super().sub_skill(skill)


class 阳春白雪_目标60减防(MagicalShieldGainRecipe):
    value = -614

    def add_skill(self, skill: Skill):
        if skill.skill_id in (14227, 14474):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (14227, 14474):
            super().sub_skill(skill)


class 阳春白雪_目标90减防(MagicalShieldGainRecipe):
    value = -921

    def add_skill(self, skill: Skill):
        if skill.skill_id in (14227, 14474):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (14227, 14474):
            super().sub_skill(skill)


class 书离伤害加百分之十五(ChannelIntervalRecipe):
    value = 1.2


class 飞帆_徵运功不被打退伤害提高10(ChannelIntervalRecipe):
    value = 1.1

    def add_skill(self, skill: Skill):
        if skill.skill_id not in (14067, 14299):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id not in (14067, 14299):
            super().sub_skill(skill)


class 师襄_羽60无视(MagicalShieldGainRecipe):
    value = -614

    def add_skill(self, skill: Skill):
        if skill.skill_id in (14100, 14101, 14102, 14511, 14512):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (14100, 14101, 14102, 14511, 14512):
            super().sub_skill(skill)


class 流照无视防御(MagicalShieldGainRecipe):
    value = -922


class 响壑徵无视防御秘籍脚本(MagicalShieldGainRecipe):
    value = -410

    def add_skill(self, skill: Skill):
        if skill.skill_id == 14227:
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 14227:
            super().sub_skill(skill)


RECIPES: Dict[int, Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]]] = {
    0: {
        SkillRecipe: {
            2045: {}, 2046: {},
            2074: {}, 2075: {},
            2089: {}, 2090: {},
            2927: {}, 2930: {}, 2931: {}, 5335: {}, 5336: {}, 5337: {}, 5338: {}, 5496: {},
            2209: {}, 2210: {}, 2401: {}, 2402: {}
        },
        CriticalStrikeRecipe_200: {
            2047: {},
            2063: {},
            2076: {}
        },
        CriticalStrikeRecipe_300: {
            2048: {},
            2064: {},
            2077: {},
            2091: {}
        },
        CriticalStrikeRecipe_400: {
            2049: {},
            2065: {},
            2078: {},
            2092: {}
        },
        商增加伤害3: {
            2058: {}
        },
        商增加伤害4: {
            2059: {}
        },
        商增加伤害5: {
            2060: {}
        },
        阳春白雪_目标35减防: {
            2136: {}, 2139: {}
        },
        阳春白雪_目标60减防: {
            2137: {}, 2140: {}
        },
        阳春白雪_目标90减防: {
            2138: {}, 2141: {}
        },
        书离伤害加百分之十五: {
            2928: {}, 2929: {}
        },
        飞帆_徵运功不被打退伤害提高10: {
            2039: {}, 4562: {}
        },
        师襄_羽60无视: {
            2974: {}
        },
        流照无视防御: {
            2975: {}, 2976: {}
        },
        响壑徵无视防御秘籍脚本: {
            5583: {}
        }
    },
    1: {
        SkillRecipe: {
            17306: {}
        },
        CriticalStrikeRecipe_306: {
            17314: {}
        }
    }
}
RECIPE_CHOICES: Dict[int, Dict[str, Dict[str, int]]] = {
    0: {
        "宫": {
            "增加伤害4%": 2046,
            "增加会心4%": 2049,
            "增加伤害3%": 2045,
            "增加会心3%": 2048,
            "增加会心2%": 2047,
        },
        "商": {
            "增加伤害5%": 2060,
            "增加伤害4%": 2059,
            "增加会心4%": 2065,
            "增加伤害3%": 2058,
            "增加会心3%": 2064,
            "增加会心2%": 2063,
        },
        "徵": {
            "增加伤害4%": 2075,
            "增加会心4%": 2078,
            "增加伤害3%": 2074,
            "增加会心3%": 2077,
            "增加会心2%": 2076,
        },
        "羽": {
            "增加伤害4%": 2090,
            "增加会心4%": 2092,
            "增加伤害3%": 2089,
            "增加会心3%": 2091,
        }
    },
    1: {}
}
