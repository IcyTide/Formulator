from typing import Dict, Union

from base.skill import Skill, DotSkill, PhysicalDamage, MagicalDamage, MagicalDotDamage
from general.skills import GENERAL_SKILLS


class 明法判定(Skill):
    final_buff = 19635
    bind_buff = 890

    def record(self, critical, parser):
        if buff_level := parser.current_target_buff_stacks.get((self.bind_buff, 1)):
            parser.refresh_target_buff(self.final_buff, buff_level)


class 明法移除(Skill):
    final_buff = 19635
    bind_buff = 890

    def record(self, critical, parser):
        buff_level = parser.current_target_buff_stacks.get((self.bind_buff, 1), 0)
        for level in range(buff_level):
            parser.clear_target_buff(self.final_buff, level + 1)


class 众嗔判定(MagicalDamage):
    final_buff = -13910

    def pre_record(self, parser):
        super().pre_record(parser)
        if 743 in parser.current_dot_ticks:
            parser.refresh_buff(self.final_buff, 1)

    def post_record(self, parser):
        super().post_record(parser)
        parser.clear_buff(self.final_buff, 1)


SKILLS: Dict[int, Union[Skill, dict]] = {
    32887: {
        "skill_class": MagicalDamage,
        "skill_name": "破",
        "surplus_cof": [
            1048576 * (0.654075 - 1),
            1048576 * (0.654075 - 1)
        ]
    },
    11: {
        "skill_class": PhysicalDamage,
        "skill_name": "六合棍",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024,
        "skill_damage_addition": 205
    },
    26989: {
        "skill_class": 明法判定,
        "skill_name": "明法判定",
    },
    26991: {
        "skill_class": 明法移除,
        "skill_name": "明法移除"
    },
    19090: {
        "skill_class": PhysicalDamage,
        "skill_name": ["普渡四方", "韦陀献杵", "横扫六合", "摩诃无量"],
        "weapon_damage_cof": [1024, 2048, 1024, 1024, 2048],
    },
    17641: {
        "skill_class": MagicalDamage,
        "skill_name": "普渡四方",
        "damage_base": [23, 27, 31, 38, 43, 50, 54, 58] + [e * 0.5 for e in
                                                           [123, 133, 143, 153, 163, 173, 183, 193, 203, 213, 223, 233,
                                                            243, 253, 263, 273, 283, 293, 303, 313]],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5] + [10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15,
                                                   15, 15, 15],
        "attack_power_cof": [16 * 1.1 * 1.15 * 1.1 * 1.05 * 1.2] * 9 +
                            [(16 + (i - 9) * 6) * 1.1 * 1.15 * 1.1 * 1.05 * 1.2 for i in range(10, 28)] +
                            [128 * 1.1 * 1.15 * 1.1 * 1.05 * 1.2],
        "post_target_buffs": {(890, 1): 1}
    },
    236: {
        "skill_class": MagicalDamage,
        "skill_name": "摩诃无量",
        "damage_base": [11, 13, 15, 18, 20, 22],
        "damage_rand": 2,
        "attack_power_cof": 16,
    },
    743: {
        "skill_class": MagicalDotDamage,
        "skill_name": "横扫六合(DOT)",
        "damage_base": 45,
        "attack_power_cof": 70 * 1.2 * 1.65 * 1.15 * 1.15 * 1.05 * 1.25 * 1.1 * 1.1,
        "interval": 32,
        "tick": 6 + 3
    },
    3810: {
        "skill_class": type("Mixing", (MagicalDamage, DotSkill), {}),
        "skill_name": "横扫六合",
        "damage_base": [36, 39, 41, 43, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
                        66, 68, 71, 73, 75, 36, 39, 41, 43, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
                        60, 61, 62, 63, 64, 66, 68, 71, 73, 75],
        "attack_power_cof": 70 * 1.2 * 1.65 * 1.15 * 1.15 * 1.05 * 1.25 * 1.1 * 1.1,
        "bind_skill": 743
    },
    **{
        skill_id: {
            "skill_class": 众嗔判定,
            "skill_name": "韦陀献杵",
            "damage_base": [77, 83, 90, 94, 100, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144,
                            147,
                            150, 153, 156, 159, 162, 165, 168, 171, 174],
            "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                            10,
                            10],
            "damage_gain": damage_gain,
            "attack_power_cof": ap * 1.2 * 1.15 * 1.15 * 1.35 * 0.9 * 1.15 * 1.1 * 1.05 * 1.1
        } for skill_id, damage_gain, ap in [(3848, 1, 144), (3849, 0.4 / 3, 48), (3850, 0.4 * 2 / 3, 96)]
    },
    28619: {
        "skill_class": MagicalDamage,
        "skill_name": "千斤坠",
        "damage_base": 28,
        "damage_rand": 3,
        "attack_power_cof": [50, 50 * 1.5],
    },
    14951: {
        "skill_class": MagicalDamage,
        "skill_name": "捕风式",
        "damage_base": [49, 55, 61, 67, 73, 79, 85, 91, 97, 103, 109, 115, 121, 127, 133, 139, 145, 151, 157, 163, 169,
                        175, 181],
        "damage_rand": [5, 6, 7, 7, 8, 9, 9, 10, 10, 11, 12, 12, 13, 14, 14, 15, 15, 16, 17, 17, 18, 18, 19],
        "damage_gain": 1 / 3,
        "attack_power_cof": [36 * 1.15 * 1.5 * 1.05] * 9 +
                            [(36 + (i - 9) * 2) * 1.15 * 1.5 * 1.05 for i in range(10, 23)] +
                            [77 * 1.15 * 1.5 * 1.05],
    },
    3814: {
        "skill_class": 众嗔判定,
        "skill_name": "守缺式",
        "damage_base": [52, 62, 72, 82, 92, 102, 112, 122, 132, 142],
        "damage_rand": 5,
        "attack_power_cof": [(120 + i * 5) * 1.15 * 0.95 * 1.05 * 1.2 * 1.1 for i in range(9)] +
                            [200 * 1.2 * 1.15 * 0.95 * 1.05 * 1.2 * 1.1],
    },
    3816: {
        "skill_class": 众嗔判定,
        "skill_name": "守缺式",
        "damage_base": [52, 62, 72, 82, 92, 102, 112, 122, 132, 142],
        "damage_rand": 5,
        "attack_power_cof": [(120 + i * 5) * 1.15 * 0.95 * 1.05 * 1.1 for i in range(9)] +
                            [200 * 1.2 * 1.15 * 0.95 * 1.05 * 1.1],
    },
    13685: {
        "skill_class": 众嗔判定,
        "skill_name": "拿云式",
        "damage_base": [e * 0.95 for e in
                        [346, 370, 394, 418, 442, 466, 490, 514, 538, 562, 586, 610, 634, 658, 682, 706, 730, 754,
                         778]],
        "damage_rand": [e * 0.1 for e in
                        [346, 370, 394, 418, 442, 466, 490, 514, 538, 562, 586, 610, 634, 658, 682, 706, 730, 754,
                         778]],
        "damage_gain": 1 / 3,
        "attack_power_cof": 260 * 1.15 * 1.35 * 0.9 * 1.1 * 1.05,
    },
    271: {
        "skill_class": MagicalDamage,
        "skill_name": "降魔",
        "damage_rand": [6, 11, 16, 21, 26, 31, 36, 26],
        "attack_power_cof": [36 * 1.2 * 1.15 * 1.15 * 1.35 * 0.9 * 1.15 * 1.1, 128, 32 * 1.15, 48, 65 * 1.15 * 1.35, 64,
                             64, 130 * 0.5],
    },
    29516: {
        "skill_class": MagicalDamage,
        "skill_name": "金刚日轮",
        "damage_base": 28,
        "damage_rand": 3,
        "attack_power_cof": 600 * 0.8,
        "skill_shield_gain": -820
    },
    32656: {
        "skill_class": MagicalDamage,
        "skill_name": "金刚龙爪功",
        "attack_power_cof": 80 * 2.5 * 1.5,
    },
    32659: {
        "skill_class": MagicalDamage,
        "skill_name": "果报守缺",
        "attack_power_cof": 300 * 2 * 1.3 * 1.4 * 1.2,
    },
    32660: {
        "skill_class": MagicalDamage,
        "skill_name": "果报横扫",
        "damage_base": 28,
        "damage_rand": 3,
        "attack_power_cof": 200 * 2 * 1.3 * 1.4 * 1.2,
    },
    25766: {
        "skill_class": MagicalDamage,
        "skill_name": "守缺式·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 50
    }
}


