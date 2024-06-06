from typing import Dict, Union

from base.skill import Skill, DotSkill, PhysicalDamage, PhysicalDotDamage, DotConsumeSkill
from general.skills import GENERAL_SKILLS

SKILLS: Dict[int, Union[Skill, dict]] = {
    32814: {
        "skill_class": PhysicalDamage,
        "skill_name": "破",
        "surplus_cof": [
            1048576 * (0.100464 - 1),
            1048576 * (0.35 - 1),
            1048576 * (0.63 - 1)
        ]
    },
    18121: {
        "skill_class": PhysicalDamage,
        "skill_name": "三柴剑法",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024,
        "skill_damage_addition": 205
    },
    748: {
        "skill_class": PhysicalDotDamage,
        "skill_name": "叠刃(DOT)",
        "damage_base": 10,
        "attack_power_cof": 58 * 1.15 * 1.1 * 1.1,
        "interval": 48,
        "max_stack": 5,
        "tick": 8
    },
    600: {
        "skill_class": DotSkill,
        "skill_name": "叠刃",
        "bind_skill": 748
    },
    **{
        skill_id: {
            "skill_class": PhysicalDamage,
            "skill_name": "无我无剑",
            "damage_base": [80, 254, 328, 402, 476, 550, 624, 698, 772, 846, 920, 994, 1068, 1142, 1216, 1290, 1364,
                            1438, 1512, 1586, 1660, 1734, 1808, 1882, 1956, 2030, 2104, 2178, 2252, 2326, 2400, 2474,
                            2548, 2622, 2696],
            "damage_rand": [7, 15, 24, 32, 40, 48, 56, 65, 73, 81, 89, 97, 106, 114, 122, 130, 138, 147, 155, 163, 171,
                            179, 188, 196, 204, 212, 220, 229, 237, 245, 253, 261, 270, 278, 286],
            "damage_gain": (i + 2) / 10 / 12,
            "attack_power_cof": [4 * 1.1 * 1.1 * 1.1 * 1.1 * 1.05 * 1.1 * 1.1 * 1.15] * 9 +
                                [(0.5 * (j - 9) + 4) * 1.1 * 1.1 * 1.1 * 1.1 * 1.05 * 1.1 * 1.1 * 1.15
                                 for j in range(10, 35)] +
                                [19 * 1.1 * 1.1 * 1.1 * 1.1 * 1.05 * 1.1 * 1.1 * 1.15],
            "attack_power_cof_gain": i + 2,
            "weapon_damage_cof": 2048
        } for i, skill_id in enumerate([386, 387, 388, 389, 390, 391, 392, 393, 394])
    },
    32408: {
        "skill_class": type("Mixing", (PhysicalDamage, DotConsumeSkill), {}),
        "skill_name": "三环套月",
        "bind_skill": 748,
        "damage_base": [40, 77, 114, 151, 189, 226, 263, 301, 338, 375, 413, 450, 487, 524, 562, 599, 636, 674, 711,
                        748, 786, 823, 860, 897, 935, 972, 1009, 1047, 1084, 1121, 1159, 1196, 1233],
        "damage_rand": [17, 21, 25, 28, 32, 36, 40, 43, 47, 51, 54, 58, 62, 66, 69, 73, 77, 81, 84, 88, 92, 95, 99, 103,
                        107, 110, 114, 118, 122, 125, 129, 133, 137],
        "damage_gain": 0.1,
        "attack_power_cof": [16 * 1.1 * 1.05 * 1.1] * 9 +
                            [(16 + (i - 9) * 4) * 1.1 * 1.05 * 1.1 for i in range(10, 33)] +
                            [120 * 1.1 * 1.05 * 1.1],
        "weapon_damage_cof": 1024,
    },
    13853: {
        "skill_class": PhysicalDamage,
        "skill_name": "八荒归元",
        "damage_base": [556, 639, 722, 805, 888, 971, 1054, 1137, 1220, 1303, 1386, 1469, 1552, 1635, 1718, 1801],
        "damage_rand": [40, 46, 52, 58, 64, 70, 76, 82, 88, 94, 100, 106, 112, 118, 124, 130],
        "damage_gain": 1.1 * 1.05 / 15,
        "attack_power_cof": 16 * 1.4 * 1.2,
    },
    4954: {
        "skill_class": PhysicalDamage,
        "skill_name": "八荒归元",
        "damage_base": [690 / 3, 690 / 2, 690],
        "damage_rand": [70 / 3, 70 / 2, 70],
        "damage_gain": 1 / 3,
        "attack_power_cof": [(128 + 16 * 6) * 1.1 * 1.1 * 1.05 * 1.4 * 1.2] +
                            [(128 + 16 * 8) * 1.1 * 1.1 * 1.05 * 1.4 * 1.2] +
                            [(128 + 16 * 10) * 1.1 * 1.1 * 1.05 * 1.4 * 1.2],
        "weapon_damage_cof": 2048,
    },
    589: {
        "skill_class": PhysicalDamage,
        "skill_name": "人剑合一",
        "damage_base": [538, 573, 608, 643, 678, 713, 748, 783, 818, 853, 888, 923, 958, 993, 1028, 1063, 1098, 1133,
                        1168, 1203, 1238, 1273],
        "damage_gain": 1 / 20,
        "attack_power_cof": 40,
    },
    889: {
        "skill_class": PhysicalDotDamage,
        "skill_name": "人剑合一(DOT)",
        "damage_base": 16,
        "attack_power_cof": 450,
        "interval": 48,
        "tick": 4
    },
    37453: {
        "skill_class": DotSkill,
        "skill_name": "人剑合一",
        "bind_skill": 889
    },
    21979: {
        "skill_class": PhysicalDamage,
        "skill_name": ["云中剑·生太极", "云中剑·碎星辰", "云中剑·吞日月"],
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": 70 * 1.1 * 1.1,
    },
    6076: {
        "skill_class": PhysicalDamage,
        "skill_name": "无我无剑",
        "damage_base": [84, 162, 239, 317, 395, 473, 550, 628, 706, 783, 861, 939, 1016, 1094, 1172, 1250, 1327, 1405,
                        1483, 1560, 1638, 1716, 1793, 1871, 1949, 2027, 2104, 2182, 2260, 2337, 2415, 2493, 2570, 2648,
                        2726],
        "damage_rand": [9, 17, 25, 33, 41, 50, 58, 66, 74, 82, 90, 99, 107, 115, 123, 131, 139, 147, 156, 164, 172, 180,
                        188, 196, 205, 213, 221, 229, 237, 245, 253, 262, 270, 278, 286],
        "damage_gain": 1 / 20 * 0.5,
        "attack_power_cof": 19 * 0.75
    },
    6077: {
        "skill_class": PhysicalDamage,
        "skill_name": "无我无剑",
        "damage_base": [84, 162, 239, 317, 395, 473, 550, 628, 706, 783, 861, 939, 1016, 1094, 1172, 1250, 1327, 1405,
                        1483, 1560, 1638, 1716, 1793, 1871, 1949, 2027, 2104, 2182, 2260, 2337, 2415, 2493, 2570, 2648,
                        2726],
        "damage_rand": [9, 17, 25, 33, 41, 50, 58, 66, 74, 82, 90, 99, 107, 115, 123, 131, 139, 147, 156, 164, 172, 180,
                        188, 196, 205, 213, 221, 229, 237, 245, 253, 262, 270, 278, 286],
        "damage_gain": 1 / 20 * 0.5,
        "attack_power_cof": 19 * 2 * 0.75
    },
    6078: {
        "skill_class": PhysicalDamage,
        "skill_name": "无我无剑",
        "damage_base": [84, 162, 239, 317, 395, 473, 550, 628, 706, 783, 861, 939, 1016, 1094, 1172, 1250, 1327, 1405,
                        1483, 1560, 1638, 1716, 1793, 1871, 1949, 2027, 2104, 2182, 2260, 2337, 2415, 2493, 2570, 2648,
                        2726],
        "damage_rand": [9, 17, 25, 33, 41, 50, 58, 66, 74, 82, 90, 99, 107, 115, 123, 131, 139, 147, 156, 164, 172, 180,
                        188, 196, 205, 213, 221, 229, 237, 245, 253, 262, 270, 278, 286],
        "damage_gain": 1 / 19 * 0.5,
        "attack_power_cof": 19 * 3 * 0.75
    },
    6079: {
        "skill_class": PhysicalDamage,
        "skill_name": "无我无剑",
        "damage_base": [84, 162, 239, 317, 395, 473, 550, 628, 706, 783, 861, 939, 1016, 1094, 1172, 1250, 1327, 1405,
                        1483, 1560, 1638, 1716, 1793, 1871, 1949, 2027, 2104, 2182, 2260, 2337, 2415, 2493, 2570, 2648,
                        2726],
        "damage_rand": [9, 17, 25, 33, 41, 50, 58, 66, 74, 82, 90, 99, 107, 115, 123, 131, 139, 147, 156, 164, 172, 180,
                        188, 196, 205, 213, 221, 229, 237, 245, 253, 262, 270, 278, 286],
        "damage_gain": 1 / 19 * 0.5,
        "attack_power_cof": 19 * 4 * 0.75
    },
    6080: {
        "skill_class": PhysicalDamage,
        "skill_name": "无我无剑",
        "damage_base": [84, 162, 239, 317, 395, 473, 550, 628, 706, 783, 861, 939, 1016, 1094, 1172, 1250, 1327, 1405,
                        1483, 1560, 1638, 1716, 1793, 1871, 1949, 2027, 2104, 2182, 2260, 2337, 2415, 2493, 2570, 2648,
                        2726],
        "damage_rand": [9, 17, 25, 33, 41, 50, 58, 66, 74, 82, 90, 99, 107, 115, 123, 131, 139, 147, 156, 164, 172, 180,
                        188, 196, 205, 213, 221, 229, 237, 245, 253, 262, 270, 278, 286],
        "damage_gain": 1 / 18 * 0.5,
        "attack_power_cof": 19 * 5 * 0.75
    },
    6081: {
        "skill_class": PhysicalDamage,
        "skill_name": "无我无剑",
        "damage_base": [84, 162, 239, 317, 395, 473, 550, 628, 706, 783, 861, 939, 1016, 1094, 1172, 1250, 1327, 1405,
                        1483, 1560, 1638, 1716, 1793, 1871, 1949, 2027, 2104, 2182, 2260, 2337, 2415, 2493, 2570, 2648,
                        2726],
        "damage_rand": [9, 17, 25, 33, 41, 50, 58, 66, 74, 82, 90, 99, 107, 115, 123, 131, 139, 147, 156, 164, 172, 180,
                        188, 196, 205, 213, 221, 229, 237, 245, 253, 262, 270, 278, 286],
        "damage_gain": 1 / 18 * 0.5,
        "attack_power_cof": 19 * 6 * 0.75
    },
    6082: {
        "skill_class": PhysicalDamage,
        "skill_name": "无我无剑",
        "damage_base": [84, 162, 239, 317, 395, 473, 550, 628, 706, 783, 861, 939, 1016, 1094, 1172, 1250, 1327, 1405,
                        1483, 1560, 1638, 1716, 1793, 1871, 1949, 2027, 2104, 2182, 2260, 2337, 2415, 2493, 2570, 2648,
                        2726],
        "damage_rand": [9, 17, 25, 33, 41, 50, 58, 66, 74, 82, 90, 99, 107, 115, 123, 131, 139, 147, 156, 164, 172, 180,
                        188, 196, 205, 213, 221, 229, 237, 245, 253, 262, 270, 278, 286],
        "damage_gain": 1 / 17 * 0.5,
        "attack_power_cof": 19 * 7 * 0.75
    },
    6083: {
        "skill_class": PhysicalDamage,
        "skill_name": "无我无剑",
        "damage_base": [84, 162, 239, 317, 395, 473, 550, 628, 706, 783, 861, 939, 1016, 1094, 1172, 1250, 1327, 1405,
                        1483, 1560, 1638, 1716, 1793, 1871, 1949, 2027, 2104, 2182, 2260, 2337, 2415, 2493, 2570, 2648,
                        2726],
        "damage_rand": [9, 17, 25, 33, 41, 50, 58, 66, 74, 82, 90, 99, 107, 115, 123, 131, 139, 147, 156, 164, 172, 180,
                        188, 196, 205, 213, 221, 229, 237, 245, 253, 262, 270, 278, 286],
        "damage_gain": 1 / 17 * 0.5,
        "attack_power_cof": 19 * 8 * 0.75
    },
    6084: {
        "skill_class": PhysicalDamage,
        "skill_name": "无我无剑",
        "damage_base": [84, 162, 239, 317, 395, 473, 550, 628, 706, 783, 861, 939, 1016, 1094, 1172, 1250, 1327, 1405,
                        1483, 1560, 1638, 1716, 1793, 1871, 1949, 2027, 2104, 2182, 2260, 2337, 2415, 2493, 2570, 2648,
                        2726],
        "damage_rand": [9, 17, 25, 33, 41, 50, 58, 66, 74, 82, 90, 99, 107, 115, 123, 131, 139, 147, 156, 164, 172, 180,
                        188, 196, 205, 213, 221, 229, 237, 245, 253, 262, 270, 278, 286],
        "damage_gain": 1 / 16 * 0.5,
        "attack_power_cof": 19 * 9 * 0.75
    },
    6085: {
        "skill_class": PhysicalDamage,
        "skill_name": "无我无剑",
        "damage_base": [84, 162, 239, 317, 395, 473, 550, 628, 706, 783, 861, 939, 1016, 1094, 1172, 1250, 1327, 1405,
                        1483, 1560, 1638, 1716, 1793, 1871, 1949, 2027, 2104, 2182, 2260, 2337, 2415, 2493, 2570, 2648,
                        2726],
        "damage_rand": [9, 17, 25, 33, 41, 50, 58, 66, 74, 82, 90, 99, 107, 115, 123, 131, 139, 147, 156, 164, 172, 180,
                        188, 196, 205, 213, 221, 229, 237, 245, 253, 262, 270, 278, 286],
        "damage_gain": 1 / 15 * 10 * 0.5 / 10,
        "attack_power_cof": 19 * 10 * 0.75
    },
    21726: {
        "skill_class": PhysicalDamage,
        "skill_name": "持盈",
        "damage_base": 40,
        "damage_rand": 17,
        "attack_power_cof": 127
    },
    34693: {
        "skill_class": PhysicalDamage,
        "skill_name": "剑入",
        "damage_base": 77,
        "damage_rand": 25,
        "attack_power_cof": 84 * 1.2 * 1.1 * 2,
        "skill_pve_addition": 1075
    },
    34694: {
        "skill_class": PhysicalDamage,
        "skill_name": "剑入",
        "damage_base": 77,
        "damage_rand": 25,
        "attack_power_cof": 616,
        "skill_pve_addition": 1075
    },
    25771: {
        "skill_class": PhysicalDamage,
        "skill_name": "八荒归元·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 65
    },
    23170: {
        "skill_class": PhysicalDotDamage,
        "skill_name": "万象归元(DOT)",
        "damage_base": 10,
        "attack_power_cof": 450,
        "interval": 48,
        "max_stack": 3,
        "tick": 10
    },
    30944: {
        "skill_class": DotSkill,
        "skill_name": "万象归元",
        "bind_skill": 23170
    }
}

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id)
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)

for skill_id, skill in GENERAL_SKILLS.items():
    SKILLS[skill_id] = skill
