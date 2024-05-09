from typing import Dict

from base.skill import Skill, DotSkill, PhysicalDamage, PhysicalDotDamage
from general.skills import GENERAL_SKILLS

SKILLS: Dict[int, Skill | dict] = {
    32815: {
        "skill_class": PhysicalDamage,
        "skill_name": "破",
        "surplus_cof": [
            1048576 * (0.7 - 1),
            1048576 * (0.875 - 1),
            1048576 * (1.4 - 1),
            1048576 * (1.54 - 1),
            1048576 * (1 - 1)
        ]
    },
    19712: {
        "skill_class": PhysicalDamage,
        "skill_name": "飘遥伞击",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024,
        "skill_damage_addition": 205
    },
    20016: {
        "skill_class": PhysicalDamage,
        "skill_name": "翼绝云天",
        "damage_base": [33, 45, 58, 70, 83, 95, 107, 120, 132, 144, 157, 169, 182, 194, 206, 219, 231, 244, 256, 268,
                        281, 293, 306, 318, 330, 343, 355, 367, 380, 392, 405, 417],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15,
                        15, 15, 15, 15, 15, 15],
        "attack_power_cof": [20 * 0.9 * 2 * 0.85] * 6 +
                            [(3 * i + 1.5) * 0.9 * 2 * 0.85 for i in range(7, 32)] +
                            [100 * 0.9 * 2 * 0.85],
    },
    31250: {
        "skill_class": PhysicalDamage,
        "skill_name": "振翅图南",
        "damage_base": [37, 67, 97, 127, 157, 187, 217, 248, 278, 308, 338, 368, 398, 428, 458],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10],
        "attack_power_cof": [30 * 0.9 * 0.885 * 1.1] * 2 +
                            [7 * i * 0.9 * 0.885 * 1.1 for i in range(3, 15)] +
                            [110 * 0.9 * 0.885 * 1.1],
    },
    20054: {
        "skill_class": PhysicalDamage,
        "skill_name": "跃潮斩波",
        "damage_base": [130, 237, 344, 450, 557, 664, 771, 878, 984, 1091, 1198, 1305, 1411, 1518, 1625],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10],
        "attack_power_cof": [78 * 1.07 * 0.9 * 0.9] * 4 +
                            [26 * i * 1.07 * 0.9 * 0.9 for i in range(5, 14)] +
                            [390 * 1.07 * 0.9 * 0.9]
    },
    20322: {
        "skill_class": PhysicalDamage,
        "skill_name": "溟海御波",
        "damage_base": [130, 237, 344, 450, 557, 664, 771, 878, 984, 1091, 1198, 1305, 1411, 1518, 1625],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15],
        "attack_power_cof": [78 * 0.9 * 1.065 * 0.9 * 0.8 * 1.1 * 1.15] * 3 +
                            [26 * i * 0.9 * 1.065 * 0.9 * 0.8 * 1.1 * 1.15 for i in range(4, 14)] +
                            [390 * 0.9 * 1.065 * 0.9 * 0.8 * 1.1 * 1.15],
    },
    20684: {
        "skill_class": PhysicalDamage,
        "skill_name": "海运南冥",
        "damage_base": [125, 228, 330, 433, 536, 638, 741, 844, 946, 1049, 1151, 1254, 1357, 1459, 1562],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15],
        "attack_power_cof": [50 * 1.8 * 0.8 * 1.1 * 0.9 * 0.85 * 1.1 * 1.15] * 3 +
                            [16.6 * i * 1.8 * 0.8 * 1.1 * 0.9 * 0.85 * 1.1 * 1.15 for i in range(4, 14)] +
                            [250 * 1.8 * 0.8 * 1.1 * 0.9 * 0.85 * 1.1 * 1.15],
    },
    20685: {
        "skill_class": PhysicalDamage,
        "skill_name": "海运南冥",
        "damage_base": [167, 304, 441, 578, 714, 851, 988, 1125, 1262, 1399, 1536, 1672, 1809, 1946, 2083],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15],
        "attack_power_cof": [50 * 2 * 0.8 * 1.1 * 0.9 * 0.85 * 1.1 * 1.15] * 3 +
                            [16.6 * i * 2 * 0.8 * 1.1 * 0.9 * 0.85 * 1.1 * 1.15 for i in range(4, 14)] +
                            [250 * 2 * 0.8 * 1.1 * 0.9 * 0.85 * 1.1 * 1.15],
    },
    20323: {
        "skill_class": PhysicalDamage,
        "skill_name": "逐波灵游",
        "damage_base": [67, 122, 176, 231, 286, 341, 395, 450, 505, 559, 614, 669, 724, 778, 833],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15],
        "attack_power_cof": [40 * 0.9 * 1.06 * 0.9 * 1.15] * 3 +
                            [13.3 * i * 0.9 * 1.06 * 0.9 * 1.15 for i in range(4, 14)] +
                            [200 * 0.9 * 1.06 * 0.9 * 1.15],
    },
    36282: {
        "skill_class": PhysicalDamage,
        "skill_name": "定波砥澜",
        "damage_base": [90, 86, 130, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350],
        "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15, 15, 15, 20],
        "attack_power_cof": [100 * 1.1] +
                            [200 * 1.1] +
                            [300 * 1.1],
        "weapon_damage_cof": 1024
    },
    19819: {
        "skill_class": PhysicalDamage,
        "skill_name": "木落雁归",
        "damage_base": [87, 134, 182, 229, 277, 324, 372, 419, 466, 514, 561, 609, 656, 704, 751, 798, 846, 893, 941,
                        988, 1036, 1083],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15],
        "attack_power_cof": [52 * 1.1 * 1.15] * 3 +
                            [(11.5 * i + 5) * 1.1 * 1.15 for i in range(4, 22)] +
                            [260 * 1.1 * 1.15],
        "weapon_damage_cof": 2048
    },
    19766: {
        "skill_class": PhysicalDamage,
        "skill_name": "击水三千",
        "damage_base": [40, 55, 71, 86, 101, 117, 132, 147, 163, 178, 193, 209, 224, 239, 255, 270, 285, 301, 316, 331,
                        347, 362, 377, 393, 408, 423, 439, 454, 469, 485, 500],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15,
                        15, 15, 15, 15, 15],
        "attack_power_cof": [24 * 1.2 * 1.1] * 5 +
                            [(3.6 * i + 5) * 1.2 * 1.1 for i in range(6, 31)] +
                            [120 * 1.2 * 1.1],
        "weapon_damage_cof": 1024
    },
    19767: {
        "skill_class": PhysicalDamage,
        "skill_name": "击水三千",
        "damage_base": [40, 55, 71, 86, 101, 117, 132, 147, 163, 178, 193, 209, 224, 239, 255, 270, 285, 301, 316, 331,
                        347, 362, 377, 393, 408, 423, 439, 454, 469, 485, 500],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15,
                        15, 15, 15, 15, 15],
        "attack_power_cof": [27 * 1.2 * 1.1] * 5 +
                            [(4 * i + 6) * 1.2 * 1.1 for i in range(6, 31)] +
                            [135 * 1.2 * 1.1],
        "weapon_damage_cof": 1024
    },
    19768: {
        "skill_class": PhysicalDamage,
        "skill_name": "击水三千",
        "damage_base": [40, 55, 71, 86, 101, 117, 132, 147, 163, 178, 193, 209, 224, 239, 255, 270, 285, 301, 316, 331,
                        347, 362, 377, 393, 408, 423, 439, 454, 469, 485, 500],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15,
                        15, 15, 15, 15, 15],
        "attack_power_cof": [30 * 1.2 * 1.1] * 5 +
                            [(4.5 * i + 7) * 1.2 * 1.1 for i in range(6, 31)] +
                            [150 * 1.2 * 1.1],
        "weapon_damage_cof": 1024
    },
    20052: {
        "skill_class": PhysicalDamage,
        "skill_name": "浮游天地",
        "damage_base": [67, 152, 237, 322, 407, 493, 578, 663, 748, 833],
        "damage_rand": 10,
        "attack_power_cof": [40 * 0.7] * 2 +
                            [20 * i * 0.7 for i in range(3, 9)] +
                            [200 * 0.7],
        "weapon_damage_cof": 2048
    },
    25273: {
        "skill_class": PhysicalDamage,
        "skill_name": "青冥",
        "damage_base": [133, 644, 1156, 1667, 133, 644, 1156, 1667],
        "damage_rand": 10,
        "attack_power_cof": (130 + 16) * 1.15 * 0.7
    },
    18386: {
        "skill_class": PhysicalDotDamage,
        "skill_name": "青冥(DOT)",
        "damage_base": 50,
        "attack_power_cof": 550,
        "interval": 32,
        "max_stack": 6,
        "tick": 6
    },
    25640: {
        "skill_class": DotSkill,
        "skill_name": "青冥",
        "bind_skill": 18386
    },
    25783: {
        "skill_class": PhysicalDamage,
        "skill_name": "木落雁归·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 50
    },
    19557: {
        "skill_class": PhysicalDotDamage,
        "skill_name": "御波驾澜(DOT)",
        "damage_base": 25,
        "attack_power_cof": 680,
        "interval": 48,
        "max_stack": 3,
        "tick": 6

    },
    26935: {
        "skill_class": DotSkill,
        "skill_name": "御波驾澜",
        "bind_skill": 19557
    }
}

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id)
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)

for skill_id, skill in GENERAL_SKILLS.items():
    SKILLS[skill_id] = skill
