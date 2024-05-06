from typing import Dict

from base.skill import Skill, DotSkill, DotConsumeSkill, PhysicalDamage, MagicalDamage, MagicalDotDamage
from general.skills import GENERAL_SKILLS

SKILLS: Dict[int, Skill | dict] = {
    32889: {
        "skill_class": MagicalDamage,
        "skill_name": "破",
        "surplus_cof": 1048576 * (1.2 * 0.33 * 0.33 - 1)
    },
    32957: {
        "skill_class": MagicalDamage,
        "skill_name": "破·虚空",
        "surplus_cof": 1048576 * (0.55 * 0.7 * 1.33 - 1)
    },
    15: {
        "skill_class": PhysicalDamage,
        "skill_name": "连环双刀",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024,
        "skill_damage_addition": 205
    },
    2920: {
        "skill_class": MagicalDotDamage,
        "skill_name": "急曲(DOT)",
        "damage_base": 100,
        "attack_power_cof": 114 * 1.1 * 0.9 * 1.1,
        "interval": 48
    },
    18716: {
        "skill_class": DotSkill,
        "skill_name": "急曲",
        "bind_skill": 2920,
        "max_stack": 3,
        "tick": 6
    },
    6559: {
        "skill_class": type("Mixing", (MagicalDamage, DotConsumeSkill), {}),
        "skill_name": "江海凝光",
        "damage_base": [65, 68, 71, 75, 78, 81, 83, 86] +
                       [e * 0.95 for e in
                        [95, 101, 106, 111, 116, 121, 127, 132, 137, 142, 147, 153, 158, 163, 168, 173, 179, 184, 189,
                         194, 199, 205, 210, 215]],
        "damage_rand": [e * 0.1 for e in
                        [54, 59, 64, 69, 75, 80, 85, 90, 95, 101, 106, 111, 116, 121, 127, 132, 137, 142, 147, 153, 158,
                         163, 168, 173, 179, 184, 189, 194, 199, 205, 210, 215]],
        "damage_gain": 1 / 2.5,
        "attack_power_cof": [36 * 1.3 * 1.1] * 9 +
                            [(36 + (i - 9) * 1) * 1.3 * 1.1 for i in range(10, 32)] +
                            [164 * 1.3 * 1.1],
        "bind_skill": 2920,
        "tick": 99,
        "last_dot": False,
    },
    30524: {
        "skill_class": MagicalDamage,
        "skill_name": "剑气长江",
        "damage_base": [e * 0.2 for e in [21, 76, 80, 81, 84]] +
                       [e * 2 * 0.98 * 0.2 for e in
                        [255, 264, 272, 281, 289, 298, 306, 325, 323, 332, 340, 349, 357, 366, 374, 383, 391, 400, 408,
                         417, 425, 434, 442]],
        "damage_rand": [e * 2 * 0.04 * 0.5 for e in
                        [33, 41, 50, 58, 67, 75, 84, 92, 101, 109, 118, 126, 135, 143, 152, 160, 169, 177, 186, 194,
                         203, 211, 220, 228, 237, 245, 254, 262]],
        "attack_power_cof": [64 * 1.1 * 1.2 * 1.1 * 1.1 * 1.1 * 1.1 * 1.1] * 9 +
                            [(64 + (i - 9) * 4) * 1.1 * 1.2 * 1.1 * 1.1 * 1.1 * 1.1 * 1.1 for i in range(10, 28)] +
                            [152 * 1.1 * 1.2 * 1.1 * 1.1 * 1.1 * 1.1 * 1.1],
    },
    2716: {
        "skill_class": MagicalDamage,
        "skill_name": "剑破虚空",
        "damage_base": [e * 0.98 / 2 + 10 for e in
                        [125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 174, 182, 190, 198, 206, 214, 222, 230]],
        "damage_rand": [e * 0.04 / 2 + 10 for e in
                        [94, 102, 110, 118, 126, 134, 142, 150, 158, 166, 174, 182, 190, 198, 206, 214, 222, 230]],
        "attack_power_cof": [80 * 1.1 * 1.1 * 1.1] * 9 +
                            [(80 + (i - 9) * 15) * 1.1 * 1.1 * 1.1 for i in range(10, 18)] +
                            [220 * 1.1 * 1.1 * 1.1],
    },
    6234: {
        "skill_class": MagicalDamage,
        "skill_name": "玳弦急曲",
        "damage_base": [20, 79, 90, 96, 103, 109, 116, 122, 129, 135, 142, 148, 155, 161, 168, 174, 181, 187, 194, 200,
                        207, 213, 220, 226, 233, 239, 246, 252],
        "damage_rand": [e * 0.1 for e in
                        [27, 33, 40, 46, 53, 59, 66, 72, 79, 85, 92, 98, 105, 111, 118, 124, 131, 137, 144, 150, 157,
                         163, 170, 176, 183, 189, 196, 202]],
        "attack_power_cof": [36 * 0.9 * 0.9 * 1.25 * 1.05] * 9 +
                            [(36 + (i - 9) * 3) * 0.9 * 0.9 * 1.25 * 1.05 for i in range(10, 28)] +
                            [85 * 0.9 * 1.25 * 1.05],
    },
    6554: {
        "skill_class": MagicalDamage,
        "skill_name": "玳弦急曲",
        "damage_base": [20, 79, 90, 96, 103, 109, 116, 122, 129, 135, 142, 148, 155, 161, 168, 174, 181, 187, 194, 200,
                        207, 213, 220, 226, 233, 239, 246, 252],
        "damage_rand": [e * 0.1 for e in
                        [27, 33, 40, 46, 53, 59, 66, 72, 79, 85, 92, 98, 105, 111, 118, 124, 131, 137, 144, 150, 157,
                         163, 170, 176, 183, 189, 196, 202]],
        "damage_gain": 0.15,
        "attack_power_cof": 85 * 0.45 * 0.9 * 1.25 * 1.05,
    },
    23936: {
        "skill_class": MagicalDamage,
        "skill_name": "广陵月",
        "damage_base": 20,
        "damage_rand": 17,
        "attack_power_cof": 16 * 1.1,
    },
    34642: {
        "skill_class": MagicalDamage,
        "skill_name": "流玉",
        "damage_base": 384 * 0.95,
        "damage_rand": 384 * 0.1,
        "attack_power_cof": 250 * 1.1,
        "skill_shield_gain": -819,
    },
    34704: {
        "skill_class": MagicalDamage,
        "skill_name": "破·流玉",
        "surplus_cof": 1048576 * (1.2 * 1.1 * 1.25 - 1)
    },
    37317: {
        "skill_class": MagicalDamage,
        "skill_name": "留芳仙姿·剑破",
        "damage_base": [70, 75, 80, 85, 90, 95, 100, 105, 110, 115],
        "damage_rand": 5,
        "attack_power_cof": 175,
    },
    37318: {
        "skill_class": MagicalDamage,
        "skill_name": "留芳仙姿·玳弦",
        "damage_base": [70, 75, 80, 85, 90, 95, 100, 105, 110, 115],
        "damage_rand": 5,
        "attack_power_cof": 30,
    },
    37319: {
        "skill_class": MagicalDamage,
        "skill_name": "留芳仙姿·剑气",
        "damage_base": [70, 75, 80, 85, 90, 95, 100, 105, 110, 115],
        "damage_rand": 5,
        "attack_power_cof": 70,
    },
    37320: {
        "skill_class": MagicalDamage,
        "skill_name": "留芳仙姿·剑影",
        "damage_base": [70, 75, 80, 85, 90, 95, 100, 105, 110, 115],
        "damage_rand": 5,
        "attack_power_cof": 260,
    },
    33140: {
        "skill_class": MagicalDamage,
        "skill_name": "盈袖",
        "damage_base": [70, 75, 80, 85, 90, 95],
        "damage_rand": 5,
        "attack_power_cof": [(400 * (i + 1) + 250) * 0.25 * 0.5 for i in range(6)]
    },
    30532: {
        "skill_class": MagicalDamage,
        "skill_name": "钗燕",
        "damage_base": [133, 644, 1156, 1667],
        "damage_rand": 5,
        "attack_power_cof": 100 * 1.3,
    },
    34611: {
        "skill_class": MagicalDamage,
        "skill_name": "钗燕·明",
        "damage_base": [70, 75, 80, 85, 90, 95],
        "damage_rand": 5,
        "attack_power_cof": 300 * 1.6 * 1.8 * 0.7 * 0.95,
    },
    24999: {
        "skill_class": MagicalDamage,
        "skill_name": "化冰",
        "damage_base": [20, 79, 90, 96, 103, 109, 116, 122, 129, 135, 142, 148, 155, 161, 168, 174, 181, 187, 194, 200,
                        207, 213, 220, 226, 233, 239, 246, 252],
        "damage_rand": [e * 0.1 for e in
                        [27, 33, 40, 46, 53, 59, 66, 72, 79, 85, 92, 98, 105, 111, 118, 124, 131, 137, 144, 150, 157,
                         163, 170, 176, 183, 189, 196, 202]],
        "attack_power_cof": 300 * 1.05 * 1.2,
    },
    34612: {
        "skill_class": MagicalDamage,
        "skill_name": "凝华",
        "damage_base": [70, 75, 80, 85, 90, 95, 100, 105, 110, 115],
        "damage_rand": 5,
        "attack_power_cof": [30 * (i + 1) * 0.7 for i in range(10)],
    },
    35058: {
        "skill_class": MagicalDamage,
        "skill_name": "凝华·明",
        "damage_base": [70, 75, 80, 85, 90, 95, 100, 105, 110, 115],
        "damage_rand": 5,
        "attack_power_cof": [370 * (i + 1) * 0.5 * 1.7 * 0.7 * 1.2 / 3 for i in range(10)],
    },
    25769: {
        "skill_class": MagicalDamage,
        "skill_name": "剑破虚空·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 65
    },
    18512: {
        "skill_class": MagicalDotDamage,
        "skill_name": "气吞长江(DOT)",
        "damage_base": 25,
        "attack_power_cof": 400 * 1.4,
        "interval": 48
    },
    25757: {
        "skill_class": DotSkill,
        "skill_name": "气吞长江",
        "bind_skill": 18512,
        "max_stack": 3,
        "tick": 10
    }
}

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id)
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)

for skill_id, skill in GENERAL_SKILLS.items():
    SKILLS[skill_id] = skill
