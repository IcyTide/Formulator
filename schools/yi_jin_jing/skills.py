from typing import Dict

from base.skill import Skill, BuffSkill, DotSkill, PhysicalDamage, MagicalDamage, MagicalDotDamage
from general.skills import GENERAL_SKILLS


class 明法判定(Skill):
    final_buff = 19635

    def record(self, skill_level, critical, parser):
        buff_level = parser.current_status[(self.bind_buff, 1)]
        if buff_level:
            parser.current_status[(self.final_buff, buff_level)] = 1


class 明法移除(Skill):
    final_buff = 19635

    def record(self, skill_level, critical, parser):
        for level in range(3):
            parser.current_status.pop((self.final_buff, level + 1), None)


SKILLS: Dict[int, Skill | dict] = {
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
        "bind_buff": 890,
    },
    26991: {
        "skill_class": 明法移除,
        "skill_name": "明法移除",
        "bind_buff": 890,
    },
    743: {
        "skill_class": MagicalDotDamage,
        "skill_name": "横扫六合(DOT)",
        "damage_base": 45,
        "attack_power_cof": 70 * 1.2 * 1.65 * 1.15 * 1.15 * 1.05 * 1.25 * 1.1 * 1.1,
        "interval": 32
    },
    19090: {
        "skill_class": PhysicalDamage,
        "skill_name": ["普渡四方", "韦陀献杵", "横扫六合", "摩诃无量"],
        "weapon_damage_cof": [1024, 2048, 1024, 1024, 2048],
    },
    17641: {
        "skill_class": type("Mixing", (MagicalDamage, BuffSkill), {}),
        "skill_name": "普渡四方",
        "damage_base": [23, 27, 31, 38, 43, 50, 54, 58] + [e * 0.5 for e in
                                                           [123, 133, 143, 153, 163, 173, 183, 193, 203, 213, 223, 233,
                                                            243, 253, 263, 273, 283, 293, 303, 313]],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5] + [10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15,
                                                   15, 15, 15],
        "attack_power_cof": [16 * 1.1 * 1.15 * 1.1 * 1.05 * 1.2] * 10 +
                            [(16 + (i - 9) * 6) * 1.1 * 1.15 * 1.1 * 1.05 * 1.2 for i in range(10, 28)] +
                            [128 * 1.1 * 1.15 * 1.1 * 1.05 * 1.2],
        "bind_buff": 890,
        "duration": 352
    },
    236: {
        "skill_class": MagicalDamage,
        "skill_name": "摩诃无量",
        "damage_base": [11, 13, 15, 18, 20, 22],
        "damage_rand": 2,
        "attack_power_cof": 16,
    },
    3810: {
        "skill_class": type("Mixing", (MagicalDamage, DotSkill), {}),
        "skill_name": "横扫六合",
        "damage_base": [36, 39, 41, 43, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
                        66, 68, 71, 73, 75, 36, 39, 41, 43, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
                        60, 61, 62, 63, 64, 66, 68, 71, 73, 75],
        "attack_power_cof": 70 * 1.2 * 1.65 * 1.15 * 1.15 * 1.05 * 1.25 * 1.1 * 1.1,
        "bind_skill": 743,
        "tick": 6 + 3
    },
    3848: {
        "skill_class": type("Mixing", (MagicalDamage, BuffSkill), {}),
        "skill_name": "韦陀献杵",
        "damage_base": [77, 83, 90, 94, 100, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144, 147,
                        150, 153, 156, 159, 162, 165, 168, 171, 174],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                        10],
        "attack_power_cof": 144 * 1.2 * 1.15 * 1.15 * 1.35 * 0.9 * 1.15 * 1.1 * 1.05 * 1.1,
        "bind_buff": 0,
        "duration": 352
    },
    3849: {
        "skill_class": type("Mixing", (MagicalDamage, BuffSkill), {}),
        "skill_name": "韦陀献杵",
        "damage_base": [73, 87, 100, 114, 127, 141, 154, 168, 181, 195, 208, 222, 235, 249, 262, 276, 289, 303, 316,
                        330, 343, 357, 370, 384, 397, 411, 424, 438, 451],
        "damage_gain": 0.4 / 3,
        "attack_power_cof": 48 * 1.2 * 1.15 * 1.15 * 1.35 * 0.9 * 1.15 * 1.1 * 1.05 * 1.1,
        "bind_buff": 0,
        "duration": 352
    },
    3850: {
        "skill_class": type("Mixing", (MagicalDamage, BuffSkill), {}),
        "skill_name": "韦陀献杵",
        "damage_base": [73, 87, 100, 114, 127, 141, 154, 168, 181, 195, 208, 222, 235, 249, 262, 276, 289, 303, 316,
                        330, 343, 357, 370, 384, 397, 411, 424, 438, 451],
        "damage_gain": 0.4 * 2 / 3,
        "attack_power_cof": 96 * 1.2 * 1.15 * 1.15 * 1.35 * 0.9 * 1.15 * 1.1 * 1.05 * 1.1,
        "bind_buff": 0,
        "duration": 352
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
        "skill_class": MagicalDamage,
        "skill_name": "守缺式",
        "damage_base": [52, 62, 72, 82, 92, 102, 112, 122, 132, 142],
        "damage_rand": 5,
        "attack_power_cof": [(120 + (i - 1) * 5) * 1.15 * 0.95 * 1.05 * 1.2 * 1.1 for i in range(10)] +
                            [200 * 1.2 * 1.15 * 0.95 * 1.05 * 1.2 * 1.1],
    },
    3816: {
        "skill_class": MagicalDamage,
        "skill_name": "守缺式",
        "damage_base": [52, 62, 72, 82, 92, 102, 112, 122, 132, 142],
        "damage_rand": 5,
        "attack_power_cof": [(120 + (i - 1) * 5) * 1.15 * 0.95 * 1.05 * 1.1 for i in range(10)] +
                            [200 * 1.2 * 1.15 * 0.95 * 1.05 * 1.1],
    },
    13685: {
        "skill_class": MagicalDamage,
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

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id)
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)

for skill_id, skill in GENERAL_SKILLS.items():
    SKILLS[skill_id] = skill
