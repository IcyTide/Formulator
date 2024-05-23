from typing import Dict, Union

from base.skill import Skill, DotSkill, PhysicalDamage, PhysicalDotDamage
from general.skills import GENERAL_SKILLS

SKILLS: Dict[int, Union[Skill, dict]] = {
    32823: {
        "skill_class": PhysicalDamage,
        "skill_name": "破",
        "surplus_cof": [
            1048576 * (0.875 - 1),
            1048576 * (0.1375 - 1),
            1048576 * (0.275 - 1),
            1048576 * (0.4032 - 1)
        ]
    },
    **{
        skill_id: {
            "skill_class": PhysicalDamage,
            "skill_name": "霜风刀法",
            "attack_power_cof": 16,
            "weapon_damage_cof": 1024
        } for skill_id in (16419, 16820, 16822)
    },
    **{
        skill_id: {
            "skill_class": PhysicalDamage,
            "skill_name": "雷走风切",
            "damage_base": 175,
            "damage_rand": 15,
            "attack_power_cof": 224 * 0.8 * 0.7,
        } for skill_id in (16599, 16631)
    },
    11447: {
        "skill_class": PhysicalDotDamage,
        "skill_name": "闹须弥(DOT)",
        "damage_base": [25, 28, 31, 34, 37, 40, 43, 46, 49, 52],
        "attack_power_cof": [50] +
                            [50 + (i - 1) * 25 for i in range(2, 10)] +
                            [280],
        "interval": 48,
        "tick": 8
    },
    17060: {
        "skill_class": DotSkill,
        "skill_name": "闹须弥",
        "bind_skill": 11447,
    },
    16933: {
        "skill_class": PhysicalDamage,
        "skill_name": "惊燕式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [16 * 1.3 * 1.2] +
                            [(16 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [64 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16934: {
        "skill_class": PhysicalDamage,
        "skill_name": "惊燕式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [20 * 1.3 * 1.2] +
                            [(20 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [80 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16935: {
        "skill_class": PhysicalDamage,
        "skill_name": "逐鹰式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [16 * 1.3 * 1.2] +
                            [(16 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [64 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16936: {
        "skill_class": PhysicalDamage,
        "skill_name": "逐鹰式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [16 * 1.3 * 1.2] +
                            [(16 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [96 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16937: {
        "skill_class": PhysicalDamage,
        "skill_name": "控鹤式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [16 * 1.3 * 1.2] +
                            [(16 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [80 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16938: {
        "skill_class": PhysicalDamage,
        "skill_name": "控鹤式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [20 * 1.3 * 1.2] +
                            [(20 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [104 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16939: {
        "skill_class": PhysicalDamage,
        "skill_name": "起凤式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [16 * 1.3 * 1.2] +
                            [(16 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [96 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16940: {
        "skill_class": PhysicalDamage,
        "skill_name": "起凤式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [20 * 1.3 * 1.2] +
                            [(20 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [120 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16941: {
        "skill_class": PhysicalDamage,
        "skill_name": "腾蛟式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [16 * 1.3 * 1.2] +
                            [(16 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [112 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16942: {
        "skill_class": PhysicalDamage,
        "skill_name": "腾蛟式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [20 * 1.3 * 1.2] +
                            [(20 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [128 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16943: {
        "skill_class": PhysicalDamage,
        "skill_name": "擒龙式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [16 * 1.3 * 1.2] +
                            [(16 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [112 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16944: {
        "skill_class": PhysicalDamage,
        "skill_name": "擒龙式",
        "damage_base": [30, 35, 40, 45, 50, 55, 60, 65, 70, 80],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10],
        "attack_power_cof": [20 * 1.3 * 1.2] +
                            [(20 + (i - 1) * 8) * 1.3 * 1.2 for i in range(2, 10)] +
                            [144 * 1.3 * 1.2],
        "weapon_damage_cof": 1024
    },
    16787: {
        "skill_class": PhysicalDamage,
        "skill_name": "坚壁清野",
        "damage_base": [150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350, 370, 390, 410, 430],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 20, 20, 20],
        "attack_power_cof": [60 * 1.2 * 0.7 * 1.1] +
                            [(60 + (i - 1) * 16) * 1.2 * 0.7 * 1.1 for i in range(2, 15)] +
                            [288 * 1.2 * 0.7 * 1.1],
    },
    16794: {
        "skill_class": PhysicalDamage,
        "skill_name": "坚壁清野",
        "damage_base": [55, 70, 85, 100, 115, 130, 145, 160, 175, 190, 205, 220, 235, 240, 250],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 20, 20, 20],
        "attack_power_cof": [32 * 1.1] +
                            [32 + (i - 1) * 9 * 1.1 for i in range(2, 15)] +
                            [160 * 1.1],
    },
    16610: {
        "skill_class": PhysicalDamage,
        "skill_name": "刀啸风吟",
        "damage_base": [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 205, 220, 235, 240, 250],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 20, 20, 20],
        "attack_power_cof": [50 * 1.2 * 1.05 * 1.1 * 1.1 * 1.05 * 1.1] +
                            [(50 + (i - 1) * 14) * 1.2 * 1.05 * 1.1 * 1.1 * 1.05 * 1.1 for i in range(2, 15)] +
                            [256 * 1.2 * 1.05 * 1.1 * 1.1 * 1.05 * 1.1],
    },
    16760: {
        "skill_class": PhysicalDamage,
        "skill_name": "项王击鼎",
        "damage_base": [35, 45, 55, 70, 85, 100, 115, 130, 145, 175, 190, 205, 220, 235, 250],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15],
        "attack_power_cof": [40 * 1.2 * 0.9 * 1.1 * 1.1] +
                            [(40 + (i - 1) * 11) * 1.2 * 0.9 * 1.1 * 1.1 for i in range(2, 15)] +
                            [200 * 1.2 * 0.9 * 1.1 * 1.1],
        "weapon_damage_cof": 1024
    },
    16382: {
        "skill_class": PhysicalDamage,
        "skill_name": "项王击鼎",
        "damage_base": [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15],
        "attack_power_cof": [16 * 0.9 * 1.1] +
                            [(16 + (i - 1) * 7) * 0.9 * 1.1 for i in range(2, 15)] +
                            [128 * 0.9 * 1.1],
        "weapon_damage_cof": 1024
    },
    20991: {
        "skill_class": PhysicalDamage,
        "skill_name": "破釜沉舟",
        "damage_base": [90, 86, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 15, 15, 20],
        "attack_power_cof": [80 * 0.9 * 0.95 * 1.1 * 1.15 * 1.1] +
                            [(80 + (i - 1) * 22) * 0.9 * 0.95 * 1.1 * 1.15 * 1.1 for i in range(2, 15)] +
                            [400 * 0.9 * 0.95 * 1.1 * 1.15 * 1.1],
        "weapon_damage_cof": 2048
    },
    **{
        skill_id: {
            "skill_class": PhysicalDamage,
            "skill_name": "上将军印",
            "damage_base": [100, 140, 160, 180, 200, 220, 240, 260, 280, 300],
            "damage_rand": [10, 10, 10, 10, 10, 15, 15, 15, 15, 15],
            "damage_gain": 1 + 0.15 * i,
            "attack_power_cof": [60 * 0.9 * 1.1 * 1.05] +
                                [(60 + (i - 1) * 10) * 0.9 * 1.1 * 1.05 for i in range(2, 10)] +
                                [160 * 0.9 * 1.1 * 1.05],
            "attack_power_cof_gain": 1 + 0.15 * i,
            "weapon_damage_cof": 1024,
            "weapon_damage_cof_gain": 1 + max(0.15 * i, 0.6)
        } for i, skill_id in enumerate([16803, 16802, 16801, 16800, 17043, 19423, 19424])
    },
    36486: {
        "skill_class": PhysicalDamage,
        "skill_name": "楚歌",
        "damage_base": [55, 70],
        "damage_rand": 5,
        "attack_power_cof": [240 * 0.8 * 1.5, 1200 * 0.8 * 1.5],
    },
    30645: {
        "skill_class": PhysicalDamage,
        "skill_name": "降麒",
        "damage_base": [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15],
        "attack_power_cof": 60 * 2,
        "weapon_damage_cof": 1024
    },
    34585: {
        "skill_class": PhysicalDamage,
        "skill_name": "绝期",
        "damage_base": [55, 70, 85, 100, 115, 130, 145, 160, 175, 190, 205, 220, 235, 240, 250],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 20, 20, 20],
        "attack_power_cof": 120,
    },
    32859: {
        "skill_class": PhysicalDamage,
        "skill_name": "上将军印·见尘",
        "damage_base": [int(e * 1.45 * 0.5) for e in [100, 140, 160, 180, 200, 220, 240, 260, 280, 300]],
        "damage_rand": [int(e * 1.45 * 0.5) for e in [10, 10, 10, 10, 10, 15, 15, 15, 15, 15]],
        "attack_power_cof": [60 * 1.45 * 1.1 * 0.7] +
                            [(60 + (i - 1) * 10) * 1.45 * 1.1 * 0.7 for i in range(2, 10)] +
                            [160 * 1.45 * 0.9 * 1.1 * 0.7],
    },
    37458: {
        "skill_class": PhysicalDamage,
        "skill_name": "掠关",
        "damage_base": [80, 88, 96, 106, 112, 118, 124, 132, 138, 142, 150, 158, 166, 172, 180],
        "damage_rand": [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 48, 50],
        "attack_power_cof": 230 * 1.3
    },
    25782: {
        "skill_class": PhysicalDamage,
        "skill_name": "上将军印·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 25
    },
    19555: {
        "skill_class": PhysicalDotDamage,
        "skill_name": "背水沉舟(DOT)",
        "damage_base": 25,
        "attack_power_cof": 380,
        "interval": 48,
        "max_stack": 3,
        "tick": 6
    },
    26934: {
        "skill_class": DotSkill,
        "skill_name": "背水沉舟",
        "bind_skill": 19555,
    }
}

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id)
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)

for skill_id, skill in GENERAL_SKILLS.items():
    SKILLS[skill_id] = skill
