from general.recipes import *


class 断脉双会提高10(NeutralCriticalRecipe):
    value = (1000, 102)

    def add_skill(self, skill: Skill):
        if skill.skill_id == 38084:
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 38084:
            super().sub_skill(skill)


class 引窍增幅增加(PveAdditionRecipe):
    value = 994
    channel_interval: list

    def add_skill(self, skill: Skill):
        if skill.skill_id == 38438:
            super().add_skill(skill)
            new_channel_interval = [
                1000 * (1 + 0.04 * level) * 0.88 * 0.9 * 0.95 * 0.9 * 0.9 * 0.85 * 0.85
                for level in range(skill.max_level)
            ]
            self.channel_interval, skill.channel_interval = skill.all_channel_interval, new_channel_interval

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 38438:
            super().sub_skill(skill)
            skill.channel_interval = self.channel_interval


class 芒渺静止增伤(MoveStateDamageAdditionRecipe):
    value = 358


RECIPES: Dict[int, Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]]] = {
    0: {
        SkillRecipe: {
            5683: {}, 5684: {}, 5685: {},
            5691: {}, 5692: {}, 5693: {},
            5698: {}, 5699: {}, 5703: {},
            5706: {}, 5707: {},
            5712: {}, 5713: {},
            5716: {}, 5717: {},

            # 奇穴
            5845: {}, 5620: {},
            5737: {}, 5749: {}, 5750: {}
        },
        CriticalStrikeRecipe_200: {
            5576: {},
            5688: {},
            5696: {}
        },
        CriticalStrikeRecipe_300: {
            5681: {},
            5680: {},
            5697: {},
            5704: {},
            5714: {}
        },
        CriticalStrikeRecipe_400: {
            5682: {},
            5690: {},
            5702: {},
            5705: {},
            5715: {}
        },
        CriticalStrikeRecipe_500: {
            5751: {}
        },
        CriticalStrikeRecipe_306: {
            17514: {}
        },
        断脉双会提高10: {
            5578: {}
        },
        引窍增幅增加: {
            5617: {}
        },
        芒渺静止增伤: {
            5640: {}
        }
    },
    1: {
        SkillRecipe: {
            17511: {}, 17512: {}, 17513: {}
        }
    }
}
RECIPE_CHOICES: Dict[int, Dict[str, Dict[str, int]]] = {
    0: {
        "断脉": {
            "增加伤害5%": 5685,
            "增加伤害4%": 5684,
            "增加会心4%": 5682,
            "增加伤害3%": 5683,
            "增加会心3%": 5681,
            "增加会心2%": 5576
        },
        "截阳": {
            "增加伤害5%": 5693,
            "增加伤害4%": 5692,
            "增加会心4%": 5690,
            "增加伤害3%": 5691,
            "增加会心3%": 5689,
            "增加会心2%": 5688
        },
        "破穴": {
            "增加伤害5%": 5703,
            "增加伤害4%": 5699,
            "增加会心4%": 5702,
            "增加伤害3%": 5698,
            "增加会心3%": 5697,
            "增加会心2%": 5696
        },
        "引窍": {
            "增加伤害5%": 5707,
            "增加伤害4%": 5706,
            "增加会心4%": 5705,
            "增加会心3%": 5704
        },
        "抟风令": {
            "增加伤害4%": 5713,
            "增加伤害3%": 5712,
        },
        "劈风令": {
            "增加伤害5%": 5717,
            "增加伤害4%": 5716,
            "增加会心4%": 5715,
            "增加会心3%": 5714
        },
    }
}
