from typing import Dict

from base.skill import Skill, DotSkill, DotConsumeSkill, PhysicalDamage, MagicalDamage, MagicalDotDamage
from general.skills import GENERAL_SKILLS

SKILLS: Dict[int, Skill | dict] = {
    32841: {
        "skill_class": MagicalDamage,
        "skill_name": "破",
        "surplus_cof": [
            1048576 * (0.525 * 1.2 - 1),
            1048576 * (1.008 * 1.2 - 1),
            1048576 * (0.21 * 1.2 - 1),
            1048576 * (0.35 * 1.2 - 1),
            1048576 * (0.7 * 1.2 - 1),
            1048576 * (1.05 * 1.2 - 1)
        ]
    },
    27451: {
        "skill_class": PhysicalDamage,
        "skill_name": "裁叶饮刃",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024,
        "skill_damage_addition": 205
    },
    28081: {
        "skill_class": MagicalDamage,
        "skill_name": "无方中和",
        "damage_base": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        "damage_rand": 10,
        "attack_power_cof": [20 * 0.9 * 0.92 * 1.1 * 1.1] * 3 +
                            [(20 * (i - 4) + 20) * 0.9 * 0.92 * 1.1 * 1.1 for i in range(4, 9)] +
                            [160 * 0.9 * 0.92 * 1.1 * 1.1] * 2,
    },
    20052: {
        "skill_class": MagicalDotDamage,
        "skill_name": "逆乱(DOT)",
        "damage_base": 95,
        "attack_power_cof": 90 * 1.5 * 0.8 * 1.05 * 1.1,
        "interval": 32
    },
    27560: {
        "skill_class": DotSkill,
        "skill_name": "逆乱",
        "bind_skill": 20052,
        "max_stack": 8,
        "tick": 7
    },
    27552: {
        "skill_class": MagicalDamage,
        "skill_name": "商陆缀寒",
        "damage_base": [38, 49, 60, 71, 82, 93, 104, 115, 126, 137, 148, 159, 170, 181, 192, 203, 214, 225, 236, 247,
                        258, 269, 280, 291, 302, 313, 324, 335, 346, 357, 368, 379],
        "damage_rand": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20,
                        20, 20, 20, 20, 20, 20, 20, 20],
        "attack_power_cof": [43 * 1.15] * 6 +
                            [(4 * i + 43) * 1.15 for i in range(7, 32)] +
                            [200 * 1.15],
    },
    27555: {
        "skill_class": MagicalDamage,
        "skill_name": "钩吻断肠",
        "damage_base": [24, 34, 44, 54, 64, 74, 84, 94, 104, 114],
        "damage_rand": 10,
        "attack_power_cof": [16] * 3 +
                            [(12 * (i - 4) + 16) for i in range(4, 9)] +
                            [120],
    },
    27557: {
        "skill_class": MagicalDamage,
        "skill_name": "川乌射罔",
        "damage_base": [33, 45, 58, 70, 83, 95, 107, 120, 132, 144, 157, 169, 182, 194, 206, 219, 231, 244, 256, 268,
                        281, 293, 306, 318, 330, 343, 355, 367, 380, 392, 405, 417],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15,
                        15, 15, 15, 15, 15, 15],
        "attack_power_cof": [25] * 2 +
                            [(12 * (i - 3) + 25) for i in range(3, 9)] +
                            [208],
    },
    27579: {
        "skill_class": MagicalDamage,
        "skill_name": "沾衣未妨",
        "damage_base": 125,
        "damage_rand": 10,
        "attack_power_cof": 150 * 0.8,
    },
    27584: {
        "skill_class": MagicalDamage,
        "skill_name": "且待时休",
        "damage_base": [33, 45, 58, 70, 83, 95, 107, 120, 132, 144, 157, 169, 182, 194, 206, 219, 231, 244, 256, 268,
                        281, 293, 306, 318, 330, 343, 355, 367, 380, 392, 405, 417],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15,
                        15, 15, 15, 15, 15, 15],
        "attack_power_cof": [30 * 1.8 * 1.2 * 1.15] * 6 +
                            [(3 * (i - 7) + 40) * 1.8 * 1.2 * 1.15 for i in range(7, 14)] +
                            [72 * 1.8 * 1.2 * 1.15],
    },
    28346: {
        "skill_class": MagicalDamage,
        "skill_name": "银光照雪",
        "damage_base": [50, 62, 74, 86, 98, 110, 134, 170, 230, 242, 290, 302, 338, 350, 410],
        "damage_rand": [10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 20, 20, 20, 20, 20],
        "attack_power_cof": [20] * 5 +
                            [(10 * (i - 6) + 24) for i in range(6, 15)] +
                            [120],
    },
    34699: {
        "skill_class": MagicalDamage,
        "skill_name": "银光照雪·结草",
        "damage_base": [50, 62, 74, 86, 98, 110, 134, 170, 230, 242, 290, 302, 338, 350, 410],
        "damage_rand": [10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 20, 20, 20, 20, 20],
        "attack_power_cof": [20] * 5 +
                            [(10 * (i - 6) + 24) for i in range(6, 15)] +
                            [120],
    },
    27539: {
        "skill_class": MagicalDamage,
        "skill_name": "惊鸿掠水",
        "damage_base": [30, 39, 48, 57, 66, 75, 84, 93, 102, 111, 120, 129, 138, 147, 156],
        "damage_rand": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15],
        "attack_power_cof": [40] * 6 +
                            [(4 * (i - 7) + 40) for i in range(7, 14)] +
                            [100],
    },
    29505: {
        "skill_class": type("Mixing", (MagicalDamage, DotConsumeSkill), {}),
        "skill_name": "含锋破月",
        "damage_base": [35, 53, 71, 89, 107, 125, 143, 161, 179, 197, 215, 233, 251, 269, 287, 305, 323, 341, 359, 377,
                        395, 413, 431, 449, 467, 485, 503, 521, 539, 557, 575],
        "damage_rand": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20,
                        20, 20, 20, 20, 20, 20, 20],
        "attack_power_cof": [50 * 1.15 * 0.85] * 5 +
                            [(9 * (i - 6) + 50) * 1.15 * 0.85 for i in range(6, 31)] +
                            [280 * 1.15 * 0.85],
        "bind_skill": 20052,
        "tick": 2
    },
    34700: {
        "skill_class": type("Mixing", (MagicalDamage, DotConsumeSkill), {}),
        "skill_name": "含锋破月·结草",
        "damage_base": [35, 53, 71, 89, 107, 125, 143, 161, 179, 197, 215, 233, 251, 269, 287, 305, 323, 341, 359, 377,
                        395, 413, 431, 449, 467, 485, 503, 521, 539, 557, 575],
        "damage_rand": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20,
                        20, 20, 20, 20, 20, 20, 20],
        "attack_power_cof": [50 * 1.15 * 0.85] * 5 +
                            [(9 * (i - 6) + 50) * 1.15 * 0.85 for i in range(6, 31)] +
                            [280 * 1.15 * 0.85],
        "bind_skill": 20052,
        "tick": 2
    },
    29506: {
        "skill_class": type("Mixing", (MagicalDamage, DotConsumeSkill), {}),
        "skill_name": "飞叶满襟",
        "damage_base": [55, 74, 93, 112, 131, 150, 169, 188, 207, 226, 245, 264, 283, 302, 321, 340, 359, 378, 397, 416,
                        435, 454, 473, 492, 511, 530, 549, 568, 587, 606, 625],
        "damage_rand": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20,
                        20, 20, 20, 20, 20, 20, 20],
        "attack_power_cof": [55 * 1.15 * 0.85] * 5 +
                            [(9 * (i - 6) + 55) * 1.15 * 0.85 for i in range(6, 31)] +
                            [340 * 1.15 * 0.85],
        "bind_skill": 20052,
        "tick": 2
    },
    34702: {
        "skill_class": type("Mixing", (MagicalDamage, DotConsumeSkill), {}),
        "skill_name": "飞叶满襟·结草",
        "damage_base": [55, 74, 93, 112, 131, 150, 169, 188, 207, 226, 245, 264, 283, 302, 321, 340, 359, 378, 397, 416,
                        435, 454, 473, 492, 511, 530, 549, 568, 587, 606, 625],
        "damage_rand": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20,
                        20, 20, 20, 20, 20, 20, 20],
        "attack_power_cof": [55 * 1.15 * 0.85] * 5 +
                            [(9 * (i - 6) + 55) * 1.15 * 0.85 for i in range(6, 31)] +
                            [340 * 1.15 * 0.85],
        "bind_skill": 20052,
        "tick": 2
    },
    27657: {
        "skill_class": MagicalDamage,
        "skill_name": "苍棘缚地",
        "damage_base": [20, 33, 46, 59, 72, 85, 98, 111, 124, 137],
        "damage_rand": 10,
        "attack_power_cof": [70 * 0.9] * 3 +
                            [(3 * (i - 4) + 70) * 0.9 for i in range(4, 9)] +
                            [300 * 0.9],
    },
    29674: {
        "skill_class": MagicalDamage,
        "skill_name": "疾根",
        "damage_base": 120,
        "damage_rand": 10,
        "attack_power_cof": 170 * 0.5 * 0.7 * 1.1
    },
    28385: {
        "skill_class": MagicalDamage,
        "skill_name": "紫叶沉疴",
        "damage_base": 417,
        "damage_rand": 15,
        "attack_power_cof": 190
    },
    28434: {
        "skill_class": MagicalDamage,
        "skill_name": "紫伏",
        "damage_base": [33, 45, 58, 70, 83, 95, 107, 120, 132, 144, 157, 169, 182, 194, 206, 219, 231, 244, 256, 268,
                        281, 293, 306, 318, 330, 343, 355, 367, 380, 392, 405, 417],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15,
                        15, 15, 15, 15, 15, 15],
        "attack_power_cof": 125 * 1.5
    },
    35367: {
        "skill_class": MagicalDamage,
        "skill_name": "应理与药",
        "damage_base": 100,
        "damage_rand": 10,
        "attack_power_cof": 580 * 1.15 * 1.5
    },
    29698: {
        "skill_class": MagicalDamage,
        "skill_name": "商陆缀寒·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 65
    },
    36580: {
        "skill_class": MagicalDamage,
        "skill_name": "银羽南徊",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 390
    }
}

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id)
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)

for skill_id, skill in GENERAL_SKILLS.items():
    SKILLS[skill_id] = skill
