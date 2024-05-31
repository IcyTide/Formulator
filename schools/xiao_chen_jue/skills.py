from typing import Dict, Union

from base.skill import Skill, DotSkill, PhysicalDamage, PhysicalDotDamage
from general.skills import GENERAL_SKILLS

SKILLS: Dict[int, Union[Skill, dict]] = {
    32908: {
        "skill_class": PhysicalDamage,
        "skill_name": "破",
        "surplus_cof": -1048576 * 7.075 / 10,
    },
    6401: {
        "skill_class": PhysicalDotDamage,
        "skill_name": "亢龙有悔(DOT)",
        "damage_base": 33,
        "attack_power_cof": 144 * 1.1 * 1.1 * 1.1,
        "interval": 48,
        "max_stack": 10,
        "tick": 10
    },
    **{
        skill_id: {
            "skill_class": DotSkill,
            "skill_name": "亢龙有悔",
            "bind_skill": 6401,
        } for skill_id in (6867, 14931)
    },
    13520: {
        "skill_class": PhysicalDamage,
        "skill_name": "恶狗拦路",
        "damage_base": [e * 0.95 for e in [69, 77, 85, 93, 101, 109, 117, 125, 101, 109, 117, 125]],
        "damage_rand": [e * 0.1 for e in [69, 77, 85, 93, 101, 109, 117, 125, 101, 109, 117, 125]],
        "attack_power_cof": [70] * 3 +
                            [70 + (i - 3) * 14 for i in range(4, 8)] +
                            [140]
    },
    13523: {
        "skill_class": PhysicalDamage,
        "skill_name": "犬牙交错",
        "damage_base": [e * 0.95 for e in [86, 45, 53, 61, 69, 77, 85, 93, 101, 109, 117, 125]],
        "damage_rand": [e * 0.1 for e in [86, 45, 53, 61, 69, 77, 85, 93, 101, 109, 117, 125]],
        "attack_power_cof": 192
    },
    6358: {
        "skill_class": PhysicalDamage,
        "skill_name": "蛟龙翻江",
        "damage_base": [e * 0.95 for e in [23, 63, 103, 143, 183, 223, 263, 303, 343, 383, 423, 463]],
        "damage_rand": [e * 0.1 for e in [23, 63, 103, 143, 183, 223, 263, 303, 343, 383, 423, 463]],
        "damage_gain": 1 / 5,
        "attack_power_cof": [26 * 1.15] * 4 +
                            [26 + (i - 4) * 3 * 1.15 for i in range(5, 12)] +
                            [50 * 1.07 * 1.15]
    },
    6359: {
        "skill_class": PhysicalDamage,
        "skill_name": "蛟龙翻江",
        "damage_base": [e * 0.95 for e in [23, 63, 103, 143, 183, 223, 263, 303, 343, 383, 423, 463]],
        "damage_rand": [e * 0.1 for e in [23, 63, 103, 143, 183, 223, 263, 303, 343, 383, 423, 463]],
        "damage_gain": 1 / 5,
        "attack_power_cof": [17 * 1.15] * 4 +
                            [17 + (i - 4) * 3 * 1.15 for i in range(5, 12)] +
                            [41 * 1.07 * 1.15]
    },
    13526: {
        "skill_class": PhysicalDamage,
        "skill_name": "蛟龙翻江",
        "damage_base": [e * 0.95 for e in [23, 63, 103, 143, 183, 223, 263, 303, 343, 383, 423, 463]],
        "damage_rand": [e * 0.1 for e in [23, 63, 103, 143, 183, 223, 263, 303, 343, 383, 423, 463]],
        "attack_power_cof": [24] * 4 +
                            [24 + (i - 4) * 4 for i in range(5, 12)] +
                            [56 * 1.07]
    },
    13527: {
        "skill_class": PhysicalDamage,
        "skill_name": "双龙取水",
        "damage_base": [e * 0.95 for e in
                        [31, 55, 79, 103, 127, 151, 175, 199, 223, 247, 271, 295, 319, 343, 367, 391, 415, 439, 463]],
        "damage_rand": [e * 0.1 for e in
                        [31, 55, 79, 103, 127, 151, 175, 199, 223, 247, 271, 295, 319, 343, 367, 391, 415, 439, 463]],
        "damage_gain": 1 / 2 * 0.6,
        "attack_power_cof": [57 * 1.15] * 4 +
                            [57 + (i - 4) * 5 * 1.15 for i in range(5, 19)] +
                            [132 * 1.07 * 1.15]
    },
    6362: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙游天地",
        "damage_base": [e * 0.95 * 2.5 for e in [40, 87, 134, 181, 228, 275, 322, 369, 416, 463]],
        "damage_rand": [e * 0.1 for e in [40, 87, 134, 181, 228, 275, 322, 369, 416, 463]],
        "damage_gain": 1 / 6,
        "attack_power_cof": [52 * 1.15] * 4 +
                            [52 + (i - 4) * 6 * 1.15 for i in range(5, 10)] +
                            [88 * 1.07 * 1.15]
    },
    6363: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙游天地",
        "damage_base": [e * 0.95 * 2.5 for e in [40, 87, 134, 181, 228, 275, 322, 369, 416, 463]],
        "damage_rand": [e * 0.1 for e in [40, 87, 134, 181, 228, 275, 322, 369, 416, 463]],
        "attack_power_cof": [48 * 1.15] * 4 +
                            [48 + (i - 4) * 7 * 1.15 for i in range(5, 10)] +
                            [90 * 1.07 * 1.15]
    },
    13528: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙游天地",
        "damage_base": [e * 0.95 * 2.5 for e in [40, 87, 134, 181, 228, 275, 322, 369, 416, 463]],
        "damage_rand": [e * 0.1 for e in [40, 87, 134, 181, 228, 275, 322, 369, 416, 463]],
        "attack_power_cof": [62 * 1.15] * 4 +
                            [62 + (i - 4) * 11 * 1.15 for i in range(5, 10)] +
                            [128 * 1.07 * 1.15]
    },
    13529: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙腾五岳",
        "damage_base": [e * 0.95 for e in [63, 103, 143, 183, 223, 263, 303, 343, 383, 423, 463]],
        "damage_rand": [e * 0.1 for e in [63, 103, 143, 183, 223, 263, 303, 343, 383, 423, 463]],
        "damage_gain": 1 / 2,
        "attack_power_cof": [175 * 1.2 * 1.3] * 4 +
                            [175 + (i - 4) * 15 * 1.2 * 1.3 for i in range(5, 11)] +
                            [280 * 1.07 * 1.2 * 1.3]
    },
    34916: {
        "skill_class": PhysicalDamage,
        "skill_name": ["蛟影·一重", "蛟影·二重", "蛟影·三重", "蛟影·四重"],
        "damage_base": [399, 599, 1367, 1461],
        "damage_rand": [e * 0.1 for e in [399, 599, 1367, 1461]],
        "damage_gain": 1.14,
        "attack_power_cof": [145 * 1.2 * 1.05 * 1.14,
                             140 * 1.2 * 1.1 * 1.14,
                             320 * 1.2 * 1.05 * 1.14,
                             318 * 1.2 * 1.1 * 1.14]
    },
    6355: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙跃于渊",
        "damage_base": [e * 0.95 for e in [24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]],
        "damage_rand": 50 * 0.1,
        "attack_power_cof": 56
    },
    6356: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙跃于渊",
        "damage_base": [e * 0.95 for e in [24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]],
        "damage_rand": 50 * 0.1,
        "attack_power_cof": 40
    },
    6357: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙跃于渊",
        "damage_base": [e * 0.95 for e in [17, 24, 28, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]],
        "damage_rand": 50 * 0.1,
        "attack_power_cof": 48
    },
    6366: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙战于野",
        "damage_base": [e * 0.95 for e in [17, 24, 28, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]],
        "damage_rand": 50 * 0.1,
        "attack_power_cof": [32 * 1.1 * 1.2] * 9 +
                            [(32 + (i - 9) * 3) * 1.1 * 1.2 for i in range(10, 17)] +
                            [56 * 1.2 * 1.1 * 1.2]
    },
    6367: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙战于野",
        "damage_base": [e * 0.95 for e in [17, 24, 28, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]],
        "damage_rand": 50 * 0.1,
        "attack_power_cof": [32 * 1.1 * 1.2] * 9 +
                            [(32 + (i - 9) * 2.5) * 1.1 * 1.2 for i in range(10, 17)] +
                            [52 * 1.2 * 1.1 * 1.2]
    },
    6368: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙战于野",
        "damage_base": [e * 0.95 for e in [17, 24, 28, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]],
        "damage_rand": 50 * 0.1,
        "attack_power_cof": [90 * 1.1 * 1.2] * 9 +
                            [(90 + (i - 9) * 6.5) * 1.1 * 1.2 for i in range(10, 17)] +
                            [150 * 1.2 * 1.1 * 1.2]
    },
    **{
        skill_id: {
            "skill_class": PhysicalDamage,
            "skill_name": "亢龙有悔",
            "damage_base": [e * 0.95
                            for e in [11, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]],
            "damage_rand": 30 * 0.1,
            "damage_gain": 1.05 * 1.05,
            "attack_power_cof": [14 * 1.9 * 0.9 * 1.07 * 1.05 * 1.05 * 1.1] * 9 +
                                [(14 + (i - 9) * 2) * 1.9 * 0.9 * 1.07 * 1.05 * 1.05 * 1.1 for i in range(10, 20)] +
                                [36 * 1.9 * 0.9 * 1.07 * 1.05 * 1.05 * 1.1]
        } for skill_id in (6369, 6370, 6371, 6372, 6373)
    },
    6374: {
        "skill_class": PhysicalDamage,
        "skill_name": "亢龙有悔",
        "damage_base": [e * 0.95
                        for e in [11, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]],
        "damage_rand": 30 * 0.1,
        "damage_gain": 1.05,
        "attack_power_cof": [(64 + i * 36.6) * 1.9 * 1.4 * 0.9 * 1.07 * 1.05 * 1.05 * 1.1 for i in range(20)]
    },
    6337: {
        "skill_class": PhysicalDamage,
        "skill_name": "斜打狗背",
        "damage_base": 37 * 0.95 * 1.25,
        "damage_rand": 37 * 0.1 * 1.25,
        "attack_power_cof": 144 * 1.25,
        "weapon_damage_cof": 1024,
    },
    26703: {
        "skill_class": PhysicalDamage,
        "skill_name": "灵隼击",
        "damage_base": [e * 0.95 for e in [16, 22, 16, 22, 16, 22]],
        "damage_rand": [e * 0.1 for e in [16, 22, 16, 22, 16, 22]],
        "attack_power_cof": 100
    },
    32898: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙战于野·醉影",
        "damage_base": 160 * 0.95,
        "damage_rand": 160 * 0.1,
        "attack_power_cof": 288 * 3.3 * 1.52 * 0.5 * 1.6 * 1.3
    },
    14927: {
        "skill_class": PhysicalDamage,
        "skill_name": "御鸿于天",
        "damage_base": 100,
        "damage_rand": 20,
        "attack_power_cof": 144,
        "weapon_damage_cof": 1024
    },
    14928: {
        "skill_class": PhysicalDamage,
        "skill_name": "御鸿于天",
        "damage_base": 100,
        "damage_rand": 20,
        "attack_power_cof": 144,
        "weapon_damage_cof": 1024
    },
    36570: {
        "skill_class": PhysicalDamage,
        "skill_name": "御鸿于天",
        "damage_rand": 55,
        "attack_power_cof": 416.8
    },
    28819: {
        "skill_class": PhysicalDamage,
        "skill_name": "温酒",
        "damage_base": 140,
        "damage_rand": 280,
        "damage_gain": 1.15,
        "attack_power_cof": 30 * 1.15
    },
    25779: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙战于野·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 60
    }
}


