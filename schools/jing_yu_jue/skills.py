from typing import Dict, Union

from base.skill import Skill, DotSkill, PhysicalDamage, PhysicalDotDamage
from general.skills import GENERAL_SKILLS

SKILLS: Dict[int, Union[Skill, dict]] = {
    32884: {
        "skill_class": PhysicalDamage,
        "skill_name": "破",
        "surplus_cof": [
            1048576 * (0.78 - 1),
            1048576 * (0.5328765 - 1)
        ]
    },
    3121: {
        "skill_class": PhysicalDamage,
        "skill_name": "罡风镖法",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024,
        "skill_damage_addition": 205
    },
    2237: {
        "skill_class": PhysicalDotDamage,
        "skill_name": "穿心(DOT)",
        "damage_base": 48,
        "attack_power_cof": 245 * 1.05 * 1.15 * 0.67 * 1.1 * 1.1 * 1.1,
        "interval": 48,
        "tick": 6 + 1,
        "max_stack": 2
    },
    3125: {
        "skill_class": DotSkill,
        "skill_name": "穿心",
        "bind_skill": 2237,
    },
    3222: {
        "skill_class": PhysicalDamage,
        "skill_name": "孔雀翎",
        "damage_base": [e * 0.95 for e in [310, 41, 69, 99, 144, 189, 260, 310]],
        "damage_rand": [e * 0.1 for e in [310, 41, 69, 99, 144, 189, 260, 310]],
        "damage_gain": 1 / 2,
        "attack_power_cof": 130
    },
    3227: {
        "skill_class": PhysicalDamage,
        "skill_name": "暴雨梨花针",
        "damage_base": [64, 81, 98, 115, 132, 149, 166, 183, 200, 217, 234, 251, 268, 285, 302, 319, 336, 353, 370, 387,
                        404, 421, 438, 455, 472, 489, 506, 523],
        "damage_rand": [e * 0.1 for e in
                        [64, 81, 98, 115, 132, 149, 166, 183, 200, 217, 234, 251, 268, 285, 302, 319, 336, 353, 370,
                         387, 404, 421, 438, 455, 472, 489, 506, 523]],
        "attack_power_cof": 30 * 1.05 * 1.1 * 1.1 * 1.1
    },
    3187: {
        "skill_class": PhysicalDamage,
        "skill_name": "逐星箭",
        "damage_base": [e * 0.95 for e in
                        [50, 53, 56, 60, 63, 66, 69, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100,
                         102, 104, 106, 108, 110]],
        "damage_rand": [e * 0.1 for e in
                        [33, 35, 38, 40, 43, 45, 48, 50, 53, 55, 58, 60, 63, 65, 68, 70, 73, 75, 78, 80, 83, 85, 88, 90,
                         93, 95, 98, 100]],
        "attack_power_cof": [50] * 9 +
                            [50 + (i - 9) * 3 for i in range(10, 28)] +
                            [120],
        "weapon_damage_cof": 1024
    },
    3095: {
        "skill_class": PhysicalDamage,
        "skill_name": "夺魄箭",
        "damage_base": [e - 10 for e in
                        [44, 55, 64, 76, 85, 94, 107, 118, 125, 135, 145, 155, 165, 175, 185, 190, 200, 205, 210, 215,
                         220, 225, 230, 235, 240, 245, 250, 255]],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20,
                        20, 20],
        "attack_power_cof": [32 * 1.15 * 1.15 * 1.1 * 1.05 * 1.1 * 1.1 * 1.1 * 1.1] * 6 +
                            [(32 + (i - 6) * 5) * 1.15 * 1.15 * 1.1 * 1.05 * 1.1 * 1.1 * 1.1 * 1.1
                             for i in range(7, 28)] +
                            [155 * 1.15 * 1.15 * 1.1 * 1.05 * 1.1 * 1.1 * 1.1 * 1.1],
        "interval": 28,
        "weapon_damage_cof": 2048
    },
    6920: {
        "skill_class": PhysicalDamage,
        "skill_name": "追命箭",
        "damage_base": [e * 0.95 / 4 + 15 for e in
                        [250, 270, 290, 310, 330, 350, 370, 390, 424, 465, 506, 547, 588, 629, 670, 711, 752, 793, 834,
                         875, 916, 957, 998, 1039, 1080, 1121, 1162, 1203]],
        "damage_rand": [e * 0.1 / 4 for e in
                        [96, 137, 178, 219, 260, 301, 342, 383, 424, 465, 506, 547, 588, 629, 670, 711, 752, 793, 834,
                         875, 916, 957, 998, 1039, 1080, 1121, 1162, 1203]],
        "attack_power_cof": [100 * 1.1 * 1.1 * 1.05 * 1.05 * 1.2 * 1.1] * 9 +
                            [(100 + (i - 9) * 6) * 1.1 * 1.1 * 1.05 * 1.05 * 1.2 * 1.1 for i in range(10, 28)] +
                            [272 * 1.1 * 1.1 * 1.05 * 1.05 * 1.2 * 1.1],
        "weapon_damage_cof": 3072
    },

    37504: {
        "skill_class": PhysicalDamage,
        "skill_name": "夺魄箭",
        "damage_base": [e - 10 for e in
                        [44, 55, 64, 76, 85, 94, 107, 118, 125, 135, 145, 155, 165, 175, 185, 190, 200, 205, 210, 215,
                         220, 225, 230, 235, 240, 245, 250, 255]],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20,
                        20, 20],
        "attack_power_cof": [2.1 * 32 * 1.15 * 1.15 * 1.1 * 1.05 * 1.1 * 1.1 * 1.1 * 1.1] * 6 +
                            [2.1 * (32 + (i - 6) * 5) * 1.15 * 1.15 * 1.1 * 1.05 * 1.1 * 1.1 * 1.1 * 1.1
                             for i in range(7, 28)] +
                            [2.1 * 155 * 1.15 * 1.15 * 1.1 * 1.05 * 1.1 * 1.1 * 1.1 * 1.1],
        "interval": 28,
        "weapon_damage_cof": 2048
    },
    22789: {
        "skill_class": PhysicalDamage,
        "skill_name": "掠影穹苍",
        "damage_base": [e * 0.95 for e in [327, 37, 63, 90, 131, 172, 236, 282, 327]],
        "damage_rand": [e * 0.1 for e in [327, 37, 63, 90, 131, 172, 236, 282, 327]],
        "attack_power_cof": 180 * 1.2
    },
    37616: {
        "skill_class": PhysicalDamage,
        "skill_name": "穿林打叶",
        "damage_base": [e * 0.95 for e in [327, 37, 63, 90, 131, 172, 236, 282, 327]],
        "damage_rand": [e * 0.1 for e in [327, 37, 63, 90, 131, 172, 236, 282, 327]],
        "attack_power_cof": 540
    },
    33870: {
        "skill_class": PhysicalDamage,
        "skill_name": "百里追魂",
        "damage_base": [e * 0.95 for e in [16, 22, 16, 22, 16, 22]],
        "damage_rand": [e * 0.1 for e in [16, 22, 16, 22, 16, 22]],
        "damage_gain": 1.5,
        "attack_power_cof": [(216 + 160 * (i + 1)) * 1.5 * 1.1 * 1.2 for i in range(6)],
        "weapon_damage_cof": [(1024 * (0.6 + 0.4 * (i + 1))) * 1.5 for i in range(6)],
        "skill_critical_strike": [1500 * 1.5 * (i + 1) for i in range(6)],
        "skill_shield_gain": [-256 * (i + 1) for i in range(6)]
    },
    25775: {
        "skill_class": PhysicalDamage,
        "skill_name": "夺魄箭·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 50
    },
    19625: {
        "skill_class": PhysicalDotDamage,
        "skill_name": "星斗阑干(DOT)",
        "damage_base": 25,
        "attack_power_cof": 600*1.1,
        "interval": 48,
        "max_stack": 3,
        "tick": 10
    },
    3478: {
        "skill_class": DotSkill,
        "skill_name": "星斗阑干",
        "bind_skill": 19625,
    }
}

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id)
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)

for skill_id, skill in GENERAL_SKILLS.items():
    SKILLS[skill_id] = skill
