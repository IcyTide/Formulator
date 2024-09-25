from general.recipes import *


class 追命箭_忽视20外防(PhysicalShieldGainRecipe):
    value = -205

    def add_skill(self, skill: Skill):
        if skill.skill_id not in (3096, 18801):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id not in (3096, 18801):
            super().sub_skill(skill)


class 唐门_穿心弩_加伤害1(ChannelIntervalRecipe):
    value = 1.05


class 唐门_穿心弩_加伤害2(ChannelIntervalRecipe):
    value = 1.1


class 蹑景追风120非侠士效果(PveAdditionRecipe):
    value = 1229


class 蹑景追风80非侠士效果(PveAdditionRecipe):
    value = 820


class 蹑景追风60非侠士效果(PveAdditionRecipe):
    value = 615


class 夺魄箭_加会心会伤(PhysicalCriticalRecipe):
    value = (1000, 100)


class 唐门_新声若惊雷无视防御(PhysicalShieldGainRecipe):
    value = -410

    def add_skill(self, skill: Skill):
        if skill.skill_id not in (3093, 6444):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id not in (3093, 6444):
            super().sub_skill(skill)


class 穿林打叶伤害修正(ChannelIntervalRecipe):
    value = 1.5


class 唐门_追命箭_忽视50外防(PhysicalShieldGainRecipe):
    value = -512

    def add_skill(self, skill: Skill):
        if skill.skill_id not in (3096, 18801):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id not in (3096, 18801):
            super().sub_skill(skill)


RECIPES: Dict[int, Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]]] = {
    0: {
        DotRecipe: {
            -154: {}, -155: {}
        },
        SkillRecipe: {
            834: {}, 835: {}, 836: {},
            843: {}, 844: {}, 845: {}, 846: {},
            853: {}, 854: {}, 855: {},
            1661: {}, 1662: {}, 1663: {},
            5090: {}, 5145: {},
            1201: {},
            946: {}, 1969: {}, 1534: {}, 1535: {}
        },
        CriticalStrikeRecipe_300: {
            837: {},
            848: {},
            856: {},
        },
        CriticalStrikeRecipe_400: {
            838: {},
            849: {},
            857: {},
        },
        CriticalStrikeRecipe_500: {
            850: {},
            1145: {}, 1978: {}
        },
        追命箭_忽视20外防: {
            858: {}
        },
        唐门_穿心弩_加伤害1: {
            859: {}
        },
        唐门_穿心弩_加伤害2: {
            860: {}
        },
        蹑景追风120非侠士效果: {
            5533: {}
        },
        蹑景追风80非侠士效果: {
            5534: {}
        },
        蹑景追风60非侠士效果: {
            5535: {}
        },
        夺魄箭_加会心会伤: {
            1200: {}
        },
        唐门_新声若惊雷无视防御: {
            3167: {}
        },
        穿林打叶伤害修正: {
            2864: {}
        },
        唐门_追命箭_忽视50外防: {
            4588: {}
        }
    },
    1: {
        SkillRecipe: {
            17435: {}
        },
        CriticalStrikeRecipe_306: {
            17436: {}
        }
    }
}
RECIPE_CHOICES: Dict[int, Dict[str, Dict[str, int]]] = {
    0: {
        "暴雨梨花针": {
            "增加伤害5%": 836,
            "增加伤害4%": 835,
            "增加会心4%": 838,
            "增加伤害3%": 834,
            "增加会心3%": 837,
        },
        "夺魄箭": {
            "运功减少0.125秒·1": 843,
            "运功减少0.125秒·2": 844,
            "增加会心5%": 850,
            "增加伤害4%": 845,
            "增加会心4%": 849,
            "增加伤害3%": 846,
            "增加会心3%": 848,
        },
        "追命箭": {
            "无视防御20%": 858,
            "增加伤害5%": 855,
            "增加伤害4%": 854,
            "增加会心4%": 857,
            "增加伤害3%": 853,
            "增加会心3%": 856,
        },
        "穿心弩": {
            "增加伤害10%": 859,
            "增加伤害5%": 860
        },
        "逐星箭": {
            "增加伤害5%": 1663,
            "增加伤害4%": 1662,
            "增加伤害3%": 1661,
        }
    }
}
