from typing import Dict, Union

from base.constant import GLOBAL_DAMAGE_FACTOR
from base.skill import Skill, DotSkill, PhysicalDamage, MagicalDamage, MagicalDotDamage, MagicalNpcDamage
from general.skills import GENERAL_SKILLS

SKILLS: Dict[int, Union[Skill, dict]] = {
    32738: {
        "skill_class": MagicalDamage,
        "skill_name": ["破", "破", "破", "破·流照", "破·争鸣"],
        "surplus_cof": [
            1048576 * (0.25 * 0.5 * 1.3 * 1.2 * 0.5 * 1.11 * 0.9 - 1),
            1048576 * (0.3 * 0.5 * 1.3 * 1.2 * 0.5 * 1.11 * 0.9 - 1),
            1048576 * (0.36 * 0.5 * 1.3 * 1.2 * 0.5 * 1.11 * 0.9 - 1),
            1048576 * (0.125 * 0.5 * 1.3 * 1.2 * 0.5 * 1.11 * 1.17 - 1),
            1048576 * (0.36 * 0.7 * 1.15 - 1)
        ]
    },
    14063: {
        "skill_class": PhysicalDamage,
        "skill_name": "五音六律",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024,
    },
    14494: {
        "skill_class": MagicalDamage,
        "skill_name": "阳春白雪",
        "damage_base": [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104,
                        107, 110],
        "damage_rand": [5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                        10],
        "damage_gain": 0.7,
        "attack_power_cof": 64 * 1.4,
    },
    15076: {
        "skill_class": MagicalNpcDamage,
        "skill_name": "宫",
        "damage_base": [34, 45, 55, 65, 75, 85, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 125, 130, 135, 140,
                        145, 150, 155, 160],
        "damage_rand": [5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 30, 30, 30, 30, 40, 40, 40],
        "attack_power_cof": [80 * 0.2 * 0.85 * 1.1] * 9 +
                            [(80 + (i - 9) * 6) * 0.2 * 0.85 * 1.1 for i in range(10, 25)] +
                            [200 * 0.2 * 0.85 * 1.1],
        "interval": 24
    },
    9357: {
        "skill_class": MagicalDotDamage,
        "skill_name": "商(DOT)",
        "damage_base": 58,
        "attack_power_cof": [48 * 1.1 * 1.05 * 1.05 * 1.05 * 1.12 * 1.05 * 1.1 * 1.05] * 9 +
                            [(48 + (i - 9) * 7) * 1.1 * 1.05 * 1.05 * 1.05 * 1.12 * 1.05 * 1.1 * 1.05 for i in
                             range(10, 25)] +
                            [160 * 1.1 * 1.05 * 1.05 * 1.05 * 1.12 * 1.05 * 1.1 * 1.05],
        "interval": 48,
        "tick": 6
    },
    **{
        skill_id: {
            "skill_class": DotSkill,
            "skill_name": "商",
            "bind_skill": 9357
        } for skill_id in (14287, 17788)
    },
    14311: {
        "skill_class": MagicalDamage,
        "skill_name": "商",
        "damage_base": [e * 0.7 for e in
                        [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104,
                         107, 110]],
        "damage_rand": [5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                        10],
        "attack_power_cof": [64 * 1.2 * 1.05 * 1.2 * 1.12 * 1.05] +
                            [64 * 1.2 * 1.05 * 1.2 * 1.12 * 1.5 * 1.05] +
                            [64 * 1.2 * 1.05 * 1.2 * 1.12 * 2 * 1.05],
    },
    9361: {
        "skill_class": MagicalDotDamage,
        "skill_name": "角(DOT)",
        "damage_base": 58,
        "attack_power_cof": [48 * 1.05 * 1.05 * 1.12 * 1.05 * 1.1 * 1.05] * 9 +
                            [(48 + (i - 9) * 8) * 1.05 * 1.05 * 1.12 * 1.05 * 1.1 * 1.05 for i in
                             range(10, 25)] +
                            [180 * 1.05 * 1.05 * 1.12 * 1.05 * 1.1 * 1.05],
        "interval": 48,
        "tick": 6
    },
    **{
        skill_id: {
            "skill_class": DotSkill,
            "skill_name": "角",
            "bind_skill": 9361
        } for skill_id in (14291, 17792)
    },
    14312: {
        "skill_class": MagicalDamage,
        "skill_name": "角",
        "damage_base": [e * 0.7 for e in
                        [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104,
                         107, 110]],
        "damage_rand": [5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                        10],
        "attack_power_cof": [64 * 1.2 * 1.05 * 1.2 * 1.12 * 1.05] +
                            [64 * 1.2 * 1.05 * 1.2 * 1.12 * 1.5 * 1.05] +
                            [64 * 1.2 * 1.05 * 1.2 * 1.12 * 2 * 1.05],
    },
    **{
        skill_id: {
            "skill_class": MagicalDamage,
            "skill_name": "徵",
            "damage_base": [70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160,
                            165,
                            170, 175, 180, 185, 190],
            "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20],
            "attack_power_cof": [40 * 1.2 * 1.09 * 1.65] * 9 +
                                [(40 + (i - 9) * 3) * 1.2 * 1.09 * 1.65 for i in range(10, 25)] +
                                [95 * 1.2 * 1.09 * 1.65],
        } for skill_id in (14227, 18859)
    },
    14100: {
        "skill_class": MagicalDamage,
        "skill_name": "羽",
        "damage_base": [32, 36, 46, 50, 54, 58, 62, 66, 70, 72, 74, 76, 78, 80, 82, 84, 86, 89, 92, 95, 98, 101, 104,
                        107, 110],
        "damage_rand": [5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                        10],
        "damage_gain": 1.3,
        "attack_power_cof": [60 * 1.1 * 1.3 * 1.15 * 1.1 * 1.1 * 1.05 * 1.1] * 9 +
                            [(60 + (i - 9) * 3) * 1.1 * 1.3 * 1.15 * 1.1 * 1.1 * 1.05 * 1.1 for i in range(10, 25)] +
                            [115 * 1.1 * 1.3 * 1.15 * 1.1 * 1.1 * 1.05 * 1.1],
    },
    18860: {
        "skill_class": MagicalDamage,
        "skill_name": "变宫",
        "damage_base": [34, 45, 55, 65, 75, 85, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 125, 130, 135, 140,
                        145, 150, 155, 160],
        "damage_rand": [5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 30, 30, 30, 30, 40, 40, 40],
        "attack_power_cof": [80 * 1.2 * 1.1 * 1.05] * 9 +
                            [80 + (i - 9) * 6 * 1.2 * 1.1 * 1.05 for i in range(10, 25)] +
                            [200 * 1.2 * 1.1 * 1.05],
    },
    32624: {
        "skill_class": MagicalDamage,
        "skill_name": "弦风",
        "damage_base": 40,
        "damage_rand": 2,
        "attack_power_cof": 40 * 1.2 * 1.25,
    },
    30799: {
        "skill_class": MagicalDamage,
        "skill_name": "流照",
        "damage_base": 107,
        "damage_rand": 27,
        "attack_power_cof": 117 * 0.35 * 1.5,
        "skill_shield_gain": -922
    },
    34676: {
        "skill_class": MagicalDamage,
        "skill_name": "知音兴尽",
        "damage_base": 40,
        "damage_rand": 6,
        "attack_power_cof": [(3750 + 125 * (i + 1)) * 0.2 * 10 * 1.2 * 1.15 for i in range(21)] +
                            [2810 * 0.2 * 1.2 * 1.15] * 2 +
                            [3250 * 0.2 * 1.2 * 1.15],
        "global_damage_factor": GLOBAL_DAMAGE_FACTOR(1048576 * (0.25 * 0.5 * 1.3 * 1.2 * 0.5 * 1.11 * 0.9 - 1))
    },
    25781: {
        "skill_class": MagicalDamage,
        "skill_name": "羽·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 50
    },
    31008: {
        "skill_class": MagicalDamage,
        "skill_name": "宫·神兵",
        "damage_base": 100,
        "damage_rand": 10,
        "attack_power_cof": 200 * 1.2 * 1.1 * 1.05
    },
    31138: {
        "skill_class": MagicalDamage,
        "skill_name": "变宫·神兵",
        "damage_base": 100,
        "damage_rand": 10,
        "attack_power_cof": 200 * 1.2 * 1.1 * 1.05
    },
    23187: {
        "skill_class": MagicalDotDamage,
        "skill_name": "神兵·宫(DOT)",
        "damage_base": 58,
        "attack_power_cof": 360 * 1.1 * 1.05 * 1.05 * 1.05 * 1.35,
        "interval": 48,
        "max_stack": 3,
        "tick": 10
    },
    31005: {
        "skill_class": DotSkill,
        "skill_name": "神兵·宫",
        "bind_skill": 23187
    }
}

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id)
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)

for skill_id, skill in GENERAL_SKILLS.items():
    SKILLS[skill_id] = skill
