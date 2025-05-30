from general.recipes import *


class 蚀肌弹_加会心(PhysicalCriticalRecipe):
    value = (1000, 100)


class 鬼斧无视防御(MagicalShieldGainRecipe):
    value = -512

    def add_skill(self, skill: Skill):
        if skill.skill_id in (3404, 3824, 3825, 3826, 3827, 3828):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (3404, 3824, 3825, 3826, 3827, 3828):
            super().sub_skill(skill)


class 连弩重弩伤害额外提高(ChannelIntervalRecipe):
    value = 1.75

    def add_skill(self, skill: Skill):
        if skill.skill_id != 3367:
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id != 3367:
            super().sub_skill(skill)


class 神机车连弩伤害额外提高(ChannelIntervalRecipe):
    value = 1.75

    def add_skill(self, skill: Skill):
        if skill.skill_id in (21854, 21850):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (21854, 21850):
            super().sub_skill(skill)


class 神机控制天绝地灭10(ChannelIntervalRecipe):
    value = 1.1


class 神机控制暗藏杀机伤害10(ChannelIntervalRecipe):
    value = 1.1


class 毒刹非侠士(PveAdditionRecipe):
    value = 8192


RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        # 通用
        834: {}, 835: {}, 836: {},
        868: {}, 869: {}, 870: {}, 871: {}, 872: {},
        884: {}, 885: {}, 886: {},
        1669: {}, 1670: {}, 1671: {},
        # 奇穴
        1219: {}, 2962: {}, 5920: {}, 2372: {}, 1223: {},
        # 装备
        947: {}, 4120: {}, 1532: {}, 1533: {}
    },
    CriticalStrikeRecipe_200: {
        1672: {}
    },
    CriticalStrikeRecipe_300: {
        837: {},
        873: {}
    },
    CriticalStrikeRecipe_400: {
        838: {},
        874: {}
    },
    CriticalStrikeRecipe_500: {
        1146: {}, 1978: {}
    },
    蚀肌弹_加会心: {
        1220: {}
    },
    鬼斧无视防御: {
        4677: {}
    },
    连弩重弩伤害额外提高: {
        5421: {}
    },
    神机车连弩伤害额外提高: {
        5459: {}
    },
    神机控制天绝地灭10: {
        2960: {}
    },
    神机控制暗藏杀机伤害10: {
        2961: {}
    },
    毒刹非侠士: {
        5830: {}
    }
}
RECIPE_CHOICES: Dict[str, Dict[str, int]] = {
    "暴雨梨花针": {
        "增加伤害5%": 836,
        "增加伤害4%": 835,
        "增加会心4%": 838,
        "增加伤害3%": 834,
        "增加会心3%": 837,
    },
    "蚀肌弹": {
        "运功减少0.125秒·1": 868,
        "运功减少0.125秒·2": 869,
        "增加伤害5%": 872,
        "增加伤害4%": 871,
        "增加会心4%": 874,
        "增加伤害3%": 870,
        "增加会心3%": 873,
    },
    "天绝地灭": {
        "增加伤害5%": 886,
        "增加伤害4%": 885,
        "增加伤害3%": 884,
    },
    "暗藏杀机": {
        "增加伤害5%": 1671,
        "增加伤害4%": 1670,
        "增加伤害3%": 1669,
        "增加会心2%": 1672,
    }
}
