from typing import Dict, Union

from base.skill import Skill, PhysicalDamage
from general.skills import GENERAL_SKILLS


class 啸日(Skill):
    def record(self, critical, parser):
        super().record(critical, parser)
        if parser.current_buff_stacks.get((-1905, 1)):
            parser.clear_buff(-1905, 1)
        else:
            parser.refresh_buff(-1905, 1)


SKILLS: Dict[int, Union[Skill, dict]] = {
    32821: {
        "skill_class": PhysicalDamage,
        "skill_name": "破",
        "surplus_cof": [
            1048576 * (0.616 - 1),
            1048576 * (0.1 - 1),
            1048576 * (0.8 - 1),
            1048576 * (0.7392 - 1)
        ]
    },
    18381: {
        "skill_class": PhysicalDamage,
        "skill_name": "三柴剑法",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024,
        "skill_damage_addition": 205
    },
    1795: {
        "skill_class": PhysicalDamage,
        "skill_name": "四季剑法",
        "attack_power_cof": 32,
        "weapon_damage_cof": 1024,
        "skill_damage_addition": 205
    },
    1656: {
        "skill_class": 啸日,
        "skill_name": "啸日"
    },
    26673: {
        "skill_class": PhysicalDamage,
        "skill_name": "九溪弥烟",
        "damage_base": [31, 32, 36, 37, 39, 42, 44, 47, 49, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68,
                        69, 71, 72, 73, 74, 75, 77, 78],
        "damage_rand": [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 10, 10, 10, 10,
                        10, 10],
        "attack_power_cof": [16 * 1.1] * 4 +
                            [(16 + (i - 4) * 1) * 1.1 for i in range(5, 32)] +
                            [48 * 1.1]
    },
    13471: {
        "skill_class": PhysicalDamage,
        "skill_name": "黄龙吐翠",
        "damage_base": [48, 66, 75, 90, 96, 111, 120, 125, 128, 141, 154, 167, 180, 193, 206, 219, 232, 245, 258, 271,
                        284, 297, 310, 323, 336, 349],
        "damage_rand": [4, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 19, 20, 21, 22, 24, 25, 26, 28, 29, 30, 32, 33, 34, 35,
                        37],
        "damage_gain": 1 / 3,
        "attack_power_cof": [16] * 10 +
                            [16 + (i - 10) * 5 for i in range(11, 26)] +
                            [112],
        "weapon_damage_cof": 1024
    },
    **{
        skill_id: {
            "skill_class": PhysicalDamage,
            "skill_name": "听雷",
            "damage_base": [109, 111, 119, 125, 131, 139, 147, 149, 151, 153, 155, 159, 165, 171, 177, 183, 193, 203,
                            213,
                            215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280],
            "damage_rand": [3, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9, 10, 10, 11, 11, 12, 13, 13, 14, 14, 15, 16, 16, 17, 17, 18,
                            19,
                            19, 20, 20, 21, 22, 22],
            "damage_gain": 1 / 2,
            "attack_power_cof": [16 * 1.1 * 1.15 * 1.1] * 8 +
                                [(16 + (i - 8) * 5) * 1.1 * 1.15 * 1.1 for i in range(9, 33)] +
                                [144 * 1.1 * 1.15 * 1.1],
            "weapon_damage_cof": 1024
        } for skill_id in (1706, 1707)
    },
    18299: {
        "skill_class": PhysicalDamage,
        "skill_name": "断潮",
        "damage_base": [e * 0.95 for e in [14, 23, 31, 39, 47, 54, 62, 70, 78, 86, 94, 103, 111, 129, 137, 144]],
        "damage_rand": [e * 0.1 for e in [14, 23, 31, 39, 47, 54, 62, 70, 78, 86, 94, 103, 111, 129, 137, 144]],
        "attack_power_cof": [84 * 1.1 * 1.1 * 1.1 * 1.1 * 1.1] * 9 +
                            [(84 + (i - 3) * 5) * 1.1 * 1.1 * 1.1 * 1.1 * 1.1 for i in range(10, 16)] +
                            [160 * 1.1 * 1.1 * 1.1 * 1.1 * 1.1],
        "weapon_damage_cof": 2048
    },
    2896: {
        "skill_class": PhysicalDamage,
        "skill_name": "夕照雷峰",
        "damage_base": [255, 280, 320, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 465, 470, 493, 521, 549,
                        577, 605, 633, 661, 689, 717, 745, 773, 801],
        "damage_rand": [5, 8, 10, 13, 16, 19, 22, 24, 27, 30, 33, 36, 38, 41, 44, 47, 50, 52, 55, 58, 61, 64, 66, 69,
                        72, 75, 78, 80],
        "damage_gain": 0.25,
        "attack_power_cof": [84 * 1.1 * 1.15 * 1.1 * 1.1 * 1.15 * 1.1 * 1.1] * 9 +
                            [(84 + (i - 9) * 5) * 1.1 * 1.15 * 1.1 * 1.1 * 1.15 * 1.1 * 1.1 for i in range(10, 28)] +
                            [180 * 1.1 * 1.15 * 1.1 * 1.1 * 1.15 * 1.1 * 1.1],
        "weapon_damage_cof": 2048
    },
    1594: {
        "skill_class": PhysicalDamage,
        "skill_name": "云飞玉皇",
        "damage_base": [400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 688],
        "damage_rand": [12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72],
        "damage_gain": 0.35,
        "attack_power_cof": 40 * 1.1 * 1.15 * 1.1 * 1.1 * 1.1 * 0.9 * 1.1 * 1.1 * 1.1 * 1.25,
        "weapon_damage_cof": 2048
    },
    1595: {
        "skill_class": PhysicalDamage,
        "skill_name": "云飞玉皇",
        "damage_base": [360, 420, 600, 630, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770],
        "damage_rand": [12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72],
        "damage_gain": 0.35,
        "attack_power_cof": [100 * 1.1 * 1.15 * 1.1 * 1.1 * 1.1 * 0.9 * 1.1 * 1.1 * 1.1 * 1.25] * 9 +
                            [(100 + (i - 10) * 15) * 1.1 * 1.15 * 1.1 * 1.1 * 1.1 * 0.9 * 1.1 * 1.1 * 1.1 * 1.25
                             for i in range(10, 16)] +
                            [200 * 1.1 * 1.15 * 1.1 * 1.1 * 1.1 * 0.9 * 1.1 * 1.1 * 1.1 * 1.25],
        "weapon_damage_cof": 2048
    },
    1598: {
        "skill_class": PhysicalDamage,
        "skill_name": "鹤归孤山",
        "damage_base": [200, 215, 230, 245, 260, 275, 290, 305, 320, 335, 350, 365, 380, 395, 410, 425, 440, 450],
        "damage_rand": [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
        "damage_gain": 1 / 2,
        "attack_power_cof": [80 * 0.7 * 1.1 * 1.1 * 1.1 * 1.1 * 1.15 * 2] * 8 +
                            [(80 + (i - 8) * 8) * 0.7 * 1.1 * 1.1 * 1.1 * 1.1 * 1.15 * 2 for i in range(9, 18)] +
                            [160 * 0.7 * 1.1 * 1.1 * 1.1 * 1.1 * 1.15 * 2],
        "weapon_damage_cof": 2048
    },
    18317: {
        "skill_class": PhysicalDamage,
        "skill_name": "云飞玉皇",
        "damage_base": [760, 840, 1040, 1090, 1140, 1170, 1200, 1230, 1260, 1290, 1320, 1350, 1380, 1410, 1440, 1458],
        "damage_rand": [24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144],
        "damage_gain": 0.35,
        "attack_power_cof": [140 * 1.1 * 1.15 * 1.1 * 1.1 * 1.1 * 0.9 * 1.1 * 1.1 * 1.1 * 1.25] * 9 +
                            [(140 + (i - 10) * 15) * 1.1 * 1.15 * 1.1 * 1.1 * 1.1 * 0.9 * 1.1 * 1.1 * 1.1 * 1.25
                             for i in range(10, 16)] +
                            [240 * 1.1 * 1.15 * 1.1 * 1.1 * 1.1 * 0.9 * 1.1 * 1.1 * 1.1 * 1.25],
        "weapon_damage_cof": 4096
    },
    18991: {
        "skill_class": PhysicalDamage,
        "skill_name": "风来吴山",
        "damage_base": [108, 124, 140, 156, 172, 188, 204, 220, 236, 252],
        "damage_rand": [3, 4, 5, 5, 6, 7, 8, 9, 9, 10],
        "damage_gain": 1 / 2,
        "attack_power_cof": [80 * 0.7 * 1.3 * 1.2 * 1.1 * 1.1 * 1.3] * 4 +
                            [(80 + (i - 5) * 15) * 0.7 * 1.3 * 1.2 * 1.1 * 1.1 * 1.3 for i in range(5, 10)] +
                            [160 * 0.7 * 1.3 * 1.2 * 1.1 * 1.1 * 1.3]
    },
    18685: {
        "skill_class": PhysicalDamage,
        "skill_name": "九溪弥烟",
        "damage_base": [22, 23, 26, 27, 29, 31, 33, 35, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
                        54, 55, 56, 57, 58, 59, 60, 61],
        "damage_rand": [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 10, 10, 10, 10,
                        10, 10],
        "attack_power_cof": [16 * 1.1 * 2 * 1.3 * 0.34 * 1.15 * 1.1 * 1.25] * 4 +
                            [(16 + (i - 4) * 1) * 1.1 * 2 * 1.3 * 0.34 * 1.15 * 1.1 * 1.25 for i in range(5, 32)] +
                            [48 * 1.1 * 2 * 1.3 * 0.34 * 1.15 * 1.1 * 1.25]
    },
    34984: {
        "skill_class": PhysicalDamage,
        "skill_name": "云飞玉皇·岱宗",
        "damage_base": 300,
        "damage_rand": 35,
        "attack_power_cof": 300 * 1.2,
        "weapon_damage_cof": 1024
    },
    30861: {
        "skill_class": PhysicalDamage,
        "skill_name": "鹤归孤山·山倾",
        "damage_base": 1500,
        "attack_power_cof": 450 * 0.8 * 1.1,
    },
    32967: {
        "skill_class": PhysicalDamage,
        "skill_name": "九皋鹤野·落剑",
        "damage_base": 280,
        "damage_rand": 22,
        "attack_power_cof": 250 * 1.1 * 1.1,
    },
    25776: {
        "skill_class": PhysicalDamage,
        "skill_name": "云飞玉皇·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 60
    },
    35051: {
        "skill_class": PhysicalDamage,
        "skill_name": ["烟流暮景", "玉山揽云"],
        "damage_base": 300,
        "damage_rand": 35,
        "attack_power_cof": [150 * 1.2, 200 * 1.2]
    }
}


