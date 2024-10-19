from general.recipes import *


class 绝刀怒气消耗伤害提高(ChannelIntervalRecipe):
    values = {
        2004: 1.2,
        2006: 1.4,
        2007: 1.6,
        2008: 1.8,
        4918: 1.2,
        4919: 1.4,
        4920: 1.6,
        4921: 1.8,
        5725: 2.2
    }

    @property
    def value(self):
        return self.values[self.recipe_id]


class 绝刀加会心(PhysicalCriticalRecipe):
    value = (1500, 200)


class 绝刀无视防御(PhysicalShieldGainRecipe):
    value = -1024

    def add_skill(self, skill: Skill):
        if skill.skill_id != 13055:
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id != 13055:
            super().sub_skill(skill)


class 绝刀破招无视防御(PhysicalShieldGainRecipe):
    value = -1024


RECIPES: Dict[int, Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]]] = {
    0: {
        SkillRecipe: {
            1830: {}, 1831: {}, 1832: {},
            1838: {}, 1839: {}, 1840: {},
            1846: {}, 1847: {},
            1852: {}, 1853: {},
            1860: {}, 1861: {}, 1862: {},
            1953: {}, 1954: {},
            1941: {}, 5735: {},
            1932: {}, 1933: {}, 1937: {}, 1938: {}
        },
        CriticalStrikeRecipe_200: {
            1833: {},
            1841: {},
            1863: {},
            1955: {}
        },
        CriticalStrikeRecipe_300: {
            1834: {},
            1842: {},
            1848: {},
            1854: {},
            1864: {},
            1956: {}
        },
        CriticalStrikeRecipe_400: {
            1835: {},
            1843: {},
            1849: {},
            1855: {},
            1865: {}
        },
        CriticalStrikeRecipe_500: {
            1934: {}, 1936: {}
        },
        绝刀怒气消耗伤害提高: {
            2004: {}, 2006: {}, 2007: {}, 2008: {}, 4918: {}, 4919: {}, 4920: {}, 4921: {}, 5725: {},
        },
        绝刀加会心: {
            1823: {}
        },
        绝刀无视防御: {
            5745: {}
        },
        绝刀破招无视防御: {
            5746: {}
        }
    },
    1: {
        SkillRecipe: {
            17447: {}
        },
        CriticalStrikeRecipe_306: {
            17448: {}
        }
    }
}
RECIPE_CHOICES: Dict[int, Dict[str, Dict[str, int]]] = {
    0: {
        "劫刀": {
            "增加伤害5%": 1832,
            "增加伤害4%": 1831,
            "增加会心4%": 1835,
            "增加伤害3%": 1830,
            "增加会心3%": 1834,
            "增加会心2%": 1833,
        },
        "斩刀": {
            "增加伤害5%": 1840,
            "增加伤害4%": 1839,
            "增加会心4%": 1843,
            "增加伤害3%": 1838,
            "增加会心3%": 1842,
            "增加会心2%": 1841,
        },
        "绝刀": {
            "增加伤害5%": 1847,
            "增加伤害4%": 1846,
            "增加会心4%": 1849,
            "增加会心3%": 1848,
        },
        "盾压": {
            "增加伤害5%": 1853,
            "增加伤害4%": 1852,
            "增加会心4%": 1855,
            "增加会心3%": 1854,
        },
        "盾刀": {
            "增加伤害5%": 1862,
            "增加伤害4%": 1861,
            "增加会心4%": 1865,
            "增加伤害3%": 1860,
            "增加会心3%": 1864,
            "增加会心2%": 1863,
        },
        "盾飞": {
            "增加伤害4%": 1954,
            "增加伤害3%": 1953,
            "增加会心3%": 1956,
            "增加会心2%": 1955,
        }
    }
}
