from typing import Dict, Union

from base.skill import Skill, DotSkill, PhysicalDamage, MagicalDamage, MagicalDotDamage
from general.skills import GENERAL_SKILLS

SKILLS: Dict[int, Union[Skill, dict]] = {
    32886: {
        "skill_class": MagicalDamage,
        "skill_name": "破",
        "surplus_cof": [
            1048576 * (1.4168 * 1.4 * 0.88 - 1),
            1048576 * (1.4168 * 0.3 * 2.3 * 0.4 - 1)
        ]
    },
    25512: {
        "skill_class": PhysicalDamage,
        "skill_name": "魂击",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024
    },
    **{
        skill_id: {
            "skill_class": MagicalDamage,
            "skill_name": "三星临",
            "damage_base": [39, 41, 43, 45, 48, 50, 52, 55, 59, 60, 66, 68, 75, 78, 82, 85, 88],
            "damage_rand": [25, 27, 28, 29, 31, 33, 35, 39, 40, 43, 45, 49, 50, 52, 53, 54, 56],
            "attack_power_cof": [(45 + i * 5) for i in range(1, 15)] +
                                [(45 + i * 9) for i in range(15, 17)] +
                                [207]
        } for skill_id in (24558, 24675, 24677)
    },
    24676: {
        "skill_class": MagicalDamage,
        "skill_name": "三星临",
        "damage_base": [39, 41, 43, 45, 48, 50, 52, 55, 59, 60, 66, 68, 75, 78, 82, 85, 88],
        "damage_rand": [25, 27, 28, 29, 31, 33, 35, 39, 40, 43, 45, 49, 50, 52, 53, 54, 56],
        "damage_gain": 1.05,
        "attack_power_cof": [(45 + i * 5) * 1.05 for i in range(1, 15)] +
                            [(45 + i * 9) * 1.05 for i in range(15, 17)] +
                            [207 * 1.05]
    },
    **{
        skill_id: {
            "skill_class": MagicalDamage,
            "skill_name": "兵主逆",
            "damage_base": [125, 130, 135, 140, 145, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350, 370, 390],
            "damage_rand": [10, 15, 17, 19, 21, 23, 25, 28, 52, 57, 65, 67, 71, 75, 79, 153, 174, 188],
            "attack_power_cof": [(40 + i * 6) * 1.1 for i in range(1, 15)] +
                                [(40 + i * 10) * 1.1 for i in range(15, 18)] +
                                [230 * 1.1]
        } for skill_id in (24811, 24812, 24814)
    },
    24813: {
        "skill_class": MagicalDamage,
        "skill_name": "兵主逆",
        "damage_base": [125, 130, 135, 140, 145, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350, 370, 390],
        "damage_rand": [10, 15, 17, 19, 21, 23, 25, 28, 52, 57, 65, 67, 71, 75, 79, 153, 174, 188],
        "damage_gain": 1.05,
        "attack_power_cof": [(40 + i * 6) * 1.05 * 1.1 for i in range(1, 15)] +
                            [(40 + i * 10) * 1.05 * 1.1 for i in range(15, 18)] +
                            [230 * 1.05 * 1.1]
    },
    **{
        skill_id: {
            "skill_class": MagicalDamage,
            "skill_name": "天斗旋",
            "damage_base": [270, 285, 300, 315, 330, 350, 370, 390, 410, 430, 450, 470, 500, 530, 560, 590, 650, 680,
                            730],
            "damage_rand": [30, 35, 45, 55, 70, 85, 100, 115, 135, 155, 175, 205, 235, 265, 295, 325, 400, 450, 500],
            "damage_gain": 0.85,
            "attack_power_cof": [110 + i * 8 for i in range(1, 16)] +
                                [(160 + i * 13) for i in range(16, 19)] +
                                [437]
        } for skill_id in (24821, 24822, 24824)
    },
    24823: {
        "skill_class": MagicalDamage,
        "skill_name": "天斗旋",
        "damage_base": [270, 285, 300, 315, 330, 350, 370, 390, 410, 430, 450, 470, 500, 530, 560, 590, 650, 680, 730],
        "damage_rand": [30, 35, 45, 55, 70, 85, 100, 115, 135, 155, 175, 205, 235, 265, 295, 325, 400, 450, 500],
        "damage_gain": 1.05 * 0.85,
        "attack_power_cof": [(110 + i * 8) * 1.05 for i in range(1, 16)] +
                            [(160 + i * 13) * 1.05 for i in range(16, 19)] +
                            [437 * 1.05]
    },
    24454: {
        "skill_class": MagicalDamage,
        "skill_name": "卦象·火离",
        "damage_base": [50, 52, 55, 59, 60, 66, 68, 75],
        "damage_rand": [28, 29, 31, 33, 35, 39, 40, 43],
        "attack_power_cof": [30] +
                            [120 + (i - 1) * 6 for i in range(2, 8)] +
                            [200]
    },
    24870: {
        "skill_class": MagicalDamage,
        "skill_name": "鬼星开穴",
        "damage_base": [285, 300, 315, 330, 350, 370, 390, 410, 430, 450, 470, 500, 530, 560, 590, 650, 680, 730] +
                       [730 * 1.9],
        "damage_rand": [35, 45, 55, 70, 85, 100, 115, 135, 155, 175, 205, 235, 265, 295, 325, 400, 450, 500] +
                       [500 * 1.9],
        "damage_gain": 1.05 * 2 / 2,
        "attack_power_cof": [(70 + i * 5) * 2 * 0.9 * 0.85 * 1.15 for i in range(1, 15)] +
                            [(115 + i * 11) * 2 * 0.9 * 0.85 * 1.15 for i in range(15, 19)] +
                            [(325 + 45 * (i - 18)) * 2 * 0.9 * 0.85 * 1.15 for i in range(19, 22)]
    },

    37311: {
        "skill_class": MagicalDamage,
        "skill_name": "鬼星开穴",
        "damage_base": [285, 300, 315, 330, 350, 370, 390, 410, 430, 450, 470, 500, 530, 560, 590, 650, 680, 730] +
                       [730 * 1.9],
        "damage_rand": [35, 45, 55, 70, 85, 100, 115, 135, 155, 175, 205, 235, 265, 295, 325, 400, 450, 500] +
                       [500 * 1.9],
        "damage_gain": 1.05 * 2 / 2,
        "attack_power_cof": [(70 + i * 5) * 2 * 0.9 * 0.85 * 1.15 for i in range(1, 15)] +
                            [(115 + i * 11) * 2 * 0.9 * 0.85 * 1.15 for i in range(15, 19)] +
                            [(325 + 45 * (i - 18)) * 2 * 0.9 * 0.85 * 1.15 for i in range(19, 22)]
    },
    33236: {
        "skill_class": MagicalDamage,
        "skill_name": "列宿游",
        "damage_base": 33,
        "damage_rand": 5,
        "damage_gain": 1.05 * 2 / 2,
        "attack_power_cof": [(800 + (800 * (i + 1) * 0.03)) * 1.15 * 0.283 for i in range(16)]
    },
    30847: {
        "skill_class": MagicalDamage,
        "skill_name": "天网",
        "damage_base": 50,
        "attack_power_cof": 100
    },
    34683: {
        "skill_class": MagicalDamage,
        "skill_name": "亘天",
        "damage_base": 33,
        "damage_rand": 5,
        "damage_gain": 1.05 * 2 / 2,
        "attack_power_cof": 270 * 1.1
    },
    25174: {
        "skill_class": MagicalDamage,
        "skill_name": "灵器",
        "damage_base": 33,
        "damage_rand": 5,
        "attack_power_cof": 200 * 0.9 * 1.2
    },
    37599: {
        "skill_class": MagicalDamage,
        "skill_name": "阵星入舆",
        "damage_base": 33,
        "damage_rand": 5,
        "damage_gain": 1.05 * 2 / 2,
        "attack_power_cof": 270 * 1.1
    },
    25837: {
        "skill_class": MagicalDamage,
        "skill_name": "三星临·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 50
    },
    24846: {
        "skill_class": MagicalDotDamage,
        "skill_name": "斗循天转(DOT)",
        "damage_base": 15,
        "attack_power_cof": 230 * 1.9,
        "interval": 48,
        "max_stack": 3,
        "tick": 10
    },
    33588: {
        "skill_class": DotSkill,
        "skill_name": "斗循天转",
        "bind_skill": 24846,
    }
}

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id)
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)

for skill_id, skill in GENERAL_SKILLS.items():
    SKILLS[skill_id] = skill
