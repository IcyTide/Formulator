from typing import Dict

from base.skill import Skill, DotSkill, PhysicalDamage, MixingDamage, MixingDotDamage
from general.skills import GENERAL_SKILLS

SKILLS: Dict[int, Skill | dict] = {
    32885: {
        "skill_class": MixingDamage,
        "skill_name": "破",
        "surplus_cof": 1048576 * (1.2144 - 1)
    },
    3121: {
        "skill_class": PhysicalDamage,
        "skill_name": "罡风镖法",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024,
        "skill_damage_addition": 205
    },
    3306: {
        "skill_class": MixingDamage,
        "skill_name": "铁爪",
        "damage_rand": 20
    },
    3401: {
        "skill_class": MixingDamage,
        "skill_name": "连弩",
        "damage_base": 37,
        "damage_rand": 5,
        "attack_power_cof": 94 * 1.1 * 0.9 * 1.05
    },
    3404: {
        "skill_class": MixingDamage,
        "skill_name": "连弩",
        "damage_base": 50,
        "damage_rand": 10,
        "attack_power_cof": 144 * 1.1 * 1.15 * 0.9 * 1.05
    },
    3819: {
        "skill_class": MixingDamage,
        "skill_name": "重弩",
        "damage_base": 267,
        "damage_rand": 34,
        "damage_gain": 0.2,
        "attack_power_cof": 59 * 1.1 * 0.9 * 1.15 * 1.8 * 1.05
    },
    3824: {
        "skill_class": MixingDamage,
        "skill_name": "重弩",
        "damage_base": 397,
        "damage_rand": 34,
        "damage_gain": 0.2,
        "attack_power_cof": 92 * 1.1 * 1.15 * 0.9 * 1.15 * 1.8 * 1.05
    },
    3228: {
        "skill_class": MixingDamage,
        "skill_name": "暴雨梨花针",
        "damage_base": [64, 81, 98, 115, 132, 149, 166, 183, 200, 217, 234, 251, 268, 285, 302, 319, 336, 353, 370, 387,
                        404, 421, 438, 455, 472, 489, 506, 523],
        "damage_rand": [e * 0.1 for e in
                        [64, 81, 98, 115, 132, 149, 166, 183, 200, 217, 234, 251, 268, 285, 302, 319, 336, 353, 370,
                         387, 404, 421, 438, 455, 472, 489, 506, 523]],
        "attack_power_cof": 30 * 1.05 * 1.1 * 1.1 * 1.1 * 1.1 * 1.25 * 1.1
    },
    14611: {
        "skill_class": MixingDotDamage,
        "skill_name": "化血(DOT)",
        "damage_base": 90,
        "attack_power_cof": 140 * 1.3 * 1.05 * 2.0 * 1.1,
        "interval": 48,
        "tick": 16
    },
    21266: {
        "skill_class": DotSkill,
        "skill_name": "化血",
        "bind_skill": 14611
    },
    3105: {
        "skill_class": MixingDamage,
        "skill_name": "蚀肌弹",
        "damage_base": [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125,
                        130, 140, 150, 160, 180],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20, 20,
                        20],
        "attack_power_cof": [16 * 1.2 * 1.1 * 1.05 * 1.05 * 1.1 * 1.1 * 1.1 * 1.1] * 9 +
                            [(16 + (i - 9) * 4) * 1.2 * 1.1 * 1.05 * 1.05 * 1.1 * 1.1 * 1.1 * 1.1 for i in
                             range(10, 27)] +
                            [108 * 1.2 * 1.1 * 1.05 * 1.05 * 1.1 * 1.1 * 1.1 * 1.1],
        "interval": 28,
        "weapon_damage_cof": 1024,
    },
    3393: {
        "skill_class": MixingDamage,
        "skill_name": "天女散花",
        "damage_base": [e * 0.95 for e in
                        [40, 44, 47, 51, 54, 58, 61, 65, 68, 72, 75, 79, 82, 86, 89, 93, 96, 100, 103, 107, 110, 114,
                         117, 121, 124, 128, 131]],
        "damage_rand": [e * 0.1 for e in
                        [40, 44, 47, 51, 54, 58, 61, 65, 68, 72, 75, 79, 82, 86, 89, 93, 96, 100, 103, 107, 110, 114,
                         117, 121, 124, 128, 131]],
        "attack_power_cof": [48] * 9 +
                            [48 + (i - 9) * 3 for i in range(10, 27)] +
                            [115]
    },
    3313: {
        "skill_class": MixingDamage,
        "skill_name": "图穷匕见",
        "damage_base": [e * 0.8 for e in [527, 37, 63, 90, 131]],
        "damage_rand": [e * 0.4 for e in [527, 37, 63, 90, 131]],
        "attack_power_cof": 115 * 1.09 * 1.1 * 1.1 * 1.3
    },
    36502: {
        "skill_class": MixingDamage,
        "skill_name": "天绝地灭",
        "damage_base": [e * 0.8 for e in
                        [23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83, 87, 91, 95, 99, 103, 107, 111,
                         115, 119, 123, 127, 131]],
        "damage_rand": [e * 0.4 for e in
                        [23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83, 87, 91, 95, 99, 103, 107, 111,
                         115, 119, 123, 127, 131]],
        "attack_power_cof": [36 * 1.1] * 9 +
                            [36 + (i - 9) * 1 * 1.1 for i in range(10, 28)] +
                            [64 * 1.1]
    },
    30894: {
        "skill_class": MixingDamage,
        "skill_name": "血影留痕",
        "damage_base": [e * 0.8 for e in
                        [23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83, 87, 91, 95, 99, 103, 107, 111,
                         115, 119, 123, 127, 131]],
        "damage_rand": [e * 0.4 for e in
                        [23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83, 87, 91, 95, 99, 103, 107, 111,
                         115, 119, 123, 127, 131]],
        "attack_power_cof": 64 * 1.1 * 1.2
    },
    30727: {
        "skill_class": MixingDamage,
        "skill_name": "天风汲雨",
        "damage_base": [e * 0.8 for e in
                        [23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83, 87, 91, 95, 99, 103, 107, 111,
                         115, 119, 123, 127, 131]],
        "damage_rand": [e * 0.4 for e in
                        [23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83, 87, 91, 95, 99, 103, 107, 111,
                         115, 119, 123, 127, 131]],
        "attack_power_cof": [36 * 1.1 * 1.55 * 2] * 9 +
                            [36 + (i - 9) * 1 * 1.1 * 1.55 * 2 for i in range(10, 28)] +
                            [64 * 1.1 * 1.55 * 2]
    },
    37384: {
        "skill_class": MixingDamage,
        "skill_name": "云合影从",
        "damage_base": 50,
        "damage_rand": 10,
        "attack_power_cof": [(10 + (i + 1) * 200) * 0.5 * 0.85 for i in range(8)]
    },
    25774: {
        "skill_class": MixingDamage,
        "skill_name": "蚀肌弹·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 40
    },
    3480: {
        "skill_class": MixingDamage,
        "skill_name": "暴雨梨花针",
        "damage_base": [e * 0.95 for e in
                        [114, 134, 154, 174, 194, 214, 234, 254, 274, 294, 314, 334, 354, 374, 394, 414, 434, 454, 474,
                         494, 514, 534, 554, 574, 594, 614, 634, 654]],
        "damage_rand": [e * 0.1 for e in
                        [114, 134, 154, 174, 194, 214, 234, 254, 274, 294, 314, 334, 354, 374, 394, 414, 434, 454, 474,
                         494, 514, 534, 554, 574, 594, 614, 634, 654]],
        "attack_power_cof": 36 * 1.05 * 1.1 * 1.1 * 1.1 * 1.5 * 1.1 * 1.2
    },
}

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id)
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)

for skill_id, skill in GENERAL_SKILLS.items():
    SKILLS[skill_id] = skill
