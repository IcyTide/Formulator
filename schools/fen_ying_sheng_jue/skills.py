from typing import Dict, Union

from base.skill import Skill, DotSkill, PhysicalDamage, MagicalDamage, MagicalDotDamage
from general.skills import GENERAL_SKILLS

SKILLS: Dict[int, Union[Skill, dict]] = {
    32887: {
        "skill_class": MagicalDamage,
        "skill_name": "破",
        "surplus_cof": [
            1048576 * (0.35 - 1),
            -1048576 * (1 - 0.42 * 0.75 * 0.72 * 1.5),
            1048576 * (0.7 - 1),
            -1048576 * (1 - 0.42 * 0.75 * 0.72 * 1.5)
        ]
    },
    4326: {
        "skill_class": PhysicalDamage,
        "skill_name": "大漠刀法",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024,
        "skill_damage_addition": 205
    },
    19055: {
        "skill_class": PhysicalDamage,
        "skill_name": ["赤日轮", "烈日斩", "生死劫·日", "生死劫·月", "净世破魔击·日", "净世破魔击·月", "幽月轮",
                       "银月斩", "驱夜断愁",
                       "悬象著明·日", "悬象著明·月"],
        "weapon_damage_cof": [1024] * 4 + [2048] + [1024] * 3 + [2048] + [1024],
    },
    4202: {
        "skill_class": MagicalDotDamage,
        "skill_name": "银月斩(DOT)",
        "damage_base": 55,
        "attack_power_cof": [40 * 1.1 * 1.1 * 1.1 * 1.05 * 1.05 * 1.3] * 9 +
                            [(40 + (i - 9) * 4) * 1.1 * 1.1 * 1.1 * 1.05 * 1.05 * 1.3 for i in range(10, 32)] +
                            [128 * 1.1 * 1.1 * 1.1 * 1.05 * 1.05 * 1.3],
        "interval": 32,
        "tick": 9
    },
    13359: {
        "skill_class": DotSkill,
        "skill_name": "银月斩",
        "bind_skill": 4202
    },
    13468: {
        "skill_class": MagicalDamage,
        "skill_name": "银月斩",
        "damage_base": [e * 0.95 for e in
                        [160, 180, 200, 220, 240, 260, 280, 300, 310, 320, 330, 340, 350, 360, 370, 380, 395, 413]],
        "damage_rand": [e * 0.1 for e in
                        [73, 93, 113, 133, 153, 173, 193, 213, 233, 253, 273, 293, 313, 333, 353, 373, 393, 413]],
        "damage_gain": 1 / 4,
        "attack_power_cof": [40 * 1.1 * 1.1 * 1.1 * 1.05 * 1.05 * 1.3] * 9 +
                            [(40 + (i - 9) * 4) * 1.1 * 1.1 * 1.1 * 1.05 * 1.05 * 1.3 for i in range(10, 32)] +
                            [128 * 1.1 * 1.1 * 1.1 * 1.05 * 1.05 * 1.3]
    },
    3963: {
        "skill_class": MagicalDamage,
        "skill_name": "烈日斩",
        "damage_base": [e * 0.95 for e in
                        [125, 145, 165, 185, 205, 225, 245, 265, 285, 305, 325, 345, 365, 375, 385, 395, 405, 415, 425,
                         430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 490]],
        "damage_rand": [e * 0.1 for e in
                        [67, 80, 94, 107, 121, 134, 148, 161, 175, 188, 202, 215, 229, 242, 256, 269, 283, 296, 310,
                         323, 337, 350, 364, 377, 391, 404, 418, 431, 445, 458, 472, 485]],
        "damage_gain": 1 / 3,
        "attack_power_cof": [64 * 1.1 * 1.1 * 1.05 * 1.05 * 1.3] * 9 +
                            [(64 + (i - 9) * 3) * 1.1 * 1.1 * 1.05 * 1.05 * 1.3 for i in range(10, 32)] +
                            [141 * 1.1 * 1.1 * 1.05 * 1.05 * 1.3],
    },
    4035: {
        "skill_class": MagicalDamage,
        "skill_name": "生死劫·日",
        "damage_base": 70,
        "damage_rand": 10,
        "attack_power_cof": 64 * 1.05
    },
    4036: {
        "skill_class": MagicalDamage,
        "skill_name": "生死劫·月",
        "damage_base": 70,
        "damage_rand": 10,
        "attack_power_cof": 64 * 1.05
    },
    4476: {
        "skill_class": MagicalDamage,
        "skill_name": "净世破魔击·月",
        "damage_base": [e * 2 * 0.98 for e in
                        [85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175,
                         180, 185, 190, 197, 204, 212, 219, 226, 233, 240, 248, 255, 262]],
        "damage_rand": [e * 2 * 0.04 for e in
                        [39, 46, 53, 60, 68, 75, 82, 89, 96, 104, 111, 118, 125, 132, 140, 147, 154, 161, 168, 176, 183,
                         190, 197, 204, 212, 219, 226, 233, 240, 248, 255, 262]],
        "damage_gain": 1 / 7,
        "attack_power_cof": [26 * 1.15 * 1.1 * 1.1 * 1.1 * 1.05 * 1.1] * 9 +
                            [(26 + (i - 9) * 1) * 1.15 * 1.1 * 1.1 * 1.1 * 1.05 * 1.1 for i in range(10, 32)] +
                            [60 * 1.15 * 1.1 * 1.1 * 1.1 * 1.05 * 1.1],
        "attack_power_cof_gain": 1 * 1.1 * 1.15 * 1.2
    },
    **{
        skill_id: {
            "skill_class": MagicalDamage,
            "skill_name": "净世破魔击·日",
            "damage_base": [e * 0.95 for e in
                            [160, 190, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370,
                             380,
                             390, 400, 410, 420, 430, 440, 450, 460, 470, 478, 492, 506, 520]],
            "damage_rand": [e * 0.1 for e in
                            [86, 100, 114, 128, 142, 156, 170, 184, 198, 212, 226, 240, 254, 268, 282, 296, 310, 324,
                             338,
                             352, 366, 380, 394, 408, 422, 436, 450, 464, 478, 492, 506, 520]],
            "damage_gain": damage_gain,
            "attack_power_cof": [ap[0] * 1.15 * 1.1 * 1.1 * 1.1 * 1.05 * 1.1] * 9 +
                                [(ap[1] + (i - 9) * 2.4) * 1.15 * 1.1 * 1.1 * 1.1 * 1.05 * 1.1 for i in range(10, 32)] +
                                [ap[2] * 1.15 * 1.1 * 1.1 * 1.1 * 1.05 * 1.1],
            "attack_power_cof_gain": 1 * 1.1 * 1.15 * 1.2
        } for skill_id, ap, damage_gain in [
            (4483, (66, 96, 180), 0.4),
            (4484, (90, 90, 149), 0.4),
            (4485, (77, 77, 139), 0.4),
            (4486, (64, 64, 128), 0.3),
            (4487, (51, 51, 117), 0.3),
            (4488, (38, 38, 106), 0.3),
            (4489, (26, 26, 96), 0.2),
            (4490, (16, 16, 83), 0.2)
        ]
    },
    4480: {
        "skill_class": MagicalDamage,
        "skill_name": "驱夜断愁",
        "damage_base": [e * 0.98 for e in
                        [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 425, 430, 435, 440, 445, 450,
                         455, 460, 465, 470, 475, 480, 485, 490, 495, 500]],
        "damage_rand": [e * 0.1 for e in
                        [137, 149, 161, 173, 185, 197, 209, 221, 233, 245, 257, 269, 281, 293, 305, 317, 329, 341, 353,
                         365, 377, 389, 401, 413, 425, 437, 449, 461, 473]],
        "damage_gain": 1 / 5,
        "attack_power_cof": [100 * 1.1*1.05*1.05] * 9 +
                            [(100 + (i - 9) * 5)*1.1*1.05*1.05 for i in range(10, 29)] +
                            [200*1.1*1.05*1.05],
    },
    4482: {
        "skill_class": MagicalDamage,
        "skill_name": "驱夜断愁",
        "damage_base": [e * 0.98 for e in
                        [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 425, 430, 435, 440, 445, 450,
                         455, 460, 465, 470, 475, 480, 485, 490, 495, 500]],
        "damage_rand": [e * 0.1 for e in
                        [137, 149, 161, 173, 185, 197, 209, 221, 233, 245, 257, 269, 281, 293, 305, 317, 329, 341, 353,
                         365, 377, 389, 401, 413, 425, 437, 449, 461, 473]],
        "damage_gain": 1.3 / 5,
        "attack_power_cof": [150 * 1.1 * 1.05 * 1.05 * 1.05] * 9 +
                            [(150 + (i - 9) * 5) * 1.1 * 1.05 * 1.05 * 1.05 for i in range(10, 29)] +
                            [260 * 1.1 * 1.05 * 1.05 * 1.05],
    },

    18280: {
        "skill_class": MagicalDamage,
        "skill_name": "烈日斩",
        "damage_base": [e * 0.95 for e in
                        [125, 145, 165, 185, 205, 225, 245, 265, 285, 305, 325, 345, 365, 375, 385, 395, 405, 415, 425,
                         430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 490]],
        "damage_rand": [e * 0.1 for e in
                        [67, 80, 94, 107, 121, 134, 148, 161, 175, 188, 202, 215, 229, 242, 256, 269, 283, 296, 310,
                         323, 337, 350, 364, 377, 391, 404, 418, 431, 445, 458, 472, 485]],
        "damage_gain": 1 / 3,
        "attack_power_cof": [64 * 1.1 * 1.1 * 1.05] * 9 +
                            [(64 + (i - 9) * 3) * 1.1 * 1.1 * 1.05 for i in range(10, 32)] +
                            [141 * 1.1 * 1.1 * 1.05],
    },
    18281: {
        "skill_class": MagicalDamage,
        "skill_name": "银月斩",
        "damage_base": [e * 0.95 for e in
                        [160, 180, 200, 220, 240, 260, 280, 300, 310, 320, 330, 340, 350, 360, 370, 380, 395, 413]],
        "damage_rand": [e * 0.1 for e in
                        [73, 93, 113, 133, 153, 173, 193, 213, 233, 253, 273, 293, 313, 333, 353, 373, 393, 413]],
        "damage_gain": 1 / 4,
        "attack_power_cof": [40 * 1.1 * 1.1 * 1.1] * 9 +
                            [(40 + (i - 9) * 4) * 1.1 * 1.1 * 1.1 for i in range(10, 32)] +
                            [128 * 1.1 * 1.1 * 1.1]
    },
    26708: {
        "skill_class": MagicalDamage,
        "skill_name": "净体不畏·日",
        "damage_base": 100,
        "damage_rand": 20,
        "attack_power_cof": [
            50 * 1.1 * 1.2 * 1.8,
            50 * 1.1 * 1.2 * 1.8 * 0.5 * 1.5,
            50 * 1.1 * 1.2 * 1.8 * 1.5,
            50 * 1.1 * 1.2 * 1.8 * 1.5 * 0.1,
            50 * 1.1 * 1.2 * 1.8 * 1.5 * 0.1
        ]
    },
    26709: {
        "skill_class": MagicalDamage,
        "skill_name": "净体不畏·月",
        "damage_base": 100,
        "damage_rand": 20,
        "attack_power_cof": [
            50 * 1.1 * 1.2 * 1.8,
            50 * 1.1 * 1.2 * 1.8 * 0.5 * 1.5,
            50 * 1.1 * 1.2 * 1.8 * 1.5,
            50 * 1.1 * 1.2 * 1.8 * 1.5 * 0.1,
            50 * 1.1 * 1.2 * 1.8 * 1.5 * 0.1
        ]
    },
    26916: {
        "skill_class": MagicalDamage,
        "skill_name": "诛邪镇魔",
        "damage_base": 209,
        "damage_rand": 240,
        "damage_gain": 2,
        "attack_power_cof": 225 * 1.05 * 1.1 * 1.1 * 1.15 * 1.1,
        "attack_power_cof_gain": 2,
    },
    25725: {
        "skill_class": MagicalDotDamage,
        "skill_name": "靡业报劫·日(DOT)",
        "damage_base": 30,
        "attack_power_cof": [377, 754, 1131, 1508],
        "interval": 32,
        "ticK": 7
    },
    **{
        skill_id: {
            "skill_class": DotSkill,
            "skill_name": "靡业报劫·日",
            "bind_skill": 25725
        } for skill_id in (34373, 35038)
    },
    25726: {
        "skill_class": MagicalDotDamage,
        "skill_name": "靡业报劫·月(DOT)",
        "damage_base": 30,
        "attack_power_cof": [377, 754, 1131, 1508],
        "interval": 32,
        "ticK": 7
    },
    **{
        skill_id: {
            "skill_class": DotSkill,
            "skill_name": "靡业报劫·月",
            "bind_skill": 25726
        } for skill_id in (34374, 35039)
    },
    35056: {
        "skill_class": MagicalDamage,
        "skill_name": "靡业报劫",
        "damage_base": 70,
        "damage_rand": 10,
        "attack_power_cof": 160
    },
    35057: {
        "skill_class": MagicalDamage,
        "skill_name": "靡业报劫·终",
        "damage_base": 70,
        "damage_rand": 10,
        "attack_power_cof": 160 * 2
    },
    34985: {
        "skill_class": MagicalDamage,
        "skill_name": "降灵尊",
        "damage_base": 70,
        "damage_rand": 10,
        "attack_power_cof": 50 * 1.1 * 1.2 * 1.8 * 1.5 * 1.42 * 1.5 * 0.8
    },
    34348: {
        "skill_class": MagicalDamage,
        "skill_name": "悬象著明·日",
        "damage_base": 70,
        "damage_rand": 10,
        "attack_power_cof": 64 * 1.05
    },
    34349: {
        "skill_class": MagicalDamage,
        "skill_name": "悬象著明·月",
        "damage_base": 70,
        "damage_rand": 10,
        "attack_power_cof": 64 * 1.05
    },
    34362: {
        "skill_class": MagicalDamage,
        "skill_name": "生死劫·月悬象",
        "damage_base": 70,
        "damage_rand": 10,
        "attack_power_cof": 64 * 1.05
    },
    34363: {
        "skill_class": MagicalDamage,
        "skill_name": "生死劫·日悬象",
        "damage_base": 70,
        "damage_rand": 10,
        "attack_power_cof": 64 * 1.05
    },
    34359: {
        "skill_class": MagicalDamage,
        "skill_name": "净世破魔击·月悬象",
        "damage_base": [e * 2 * 0.98 for e in
                        [85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175,
                         180, 185, 190, 197, 204, 212, 219, 226, 233, 240, 248, 255, 262]],
        "damage_rand": [e * 2 * 0.04 for e in
                        [39, 46, 53, 60, 68, 75, 82, 89, 96, 104, 111, 118, 125, 132, 140, 147, 154, 161, 168, 176, 183,
                         190, 197, 204, 212, 219, 226, 233, 240, 248, 255, 262]],
        "damage_gain": 1 / 7,
        "attack_power_cof": 60 * 1.15 * 1.1 * 1.1 * 1.1 * 1.05 * 1.1 * 0.7,
    },
    34361: {
        "skill_class": MagicalDamage,
        "skill_name": "净世破魔击·日悬象",
        "damage_base": [e * 0.95 for e in
                        [160, 190, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380,
                         390, 400, 410, 420, 430, 440, 450, 460, 470, 478, 492, 506, 520]],
        "damage_rand": [e * 0.1 for e in
                        [86, 100, 114, 128, 142, 156, 170, 184, 198, 212, 226, 240, 254, 268, 282, 296, 310, 324, 338,
                         352, 366, 380, 394, 408, 422, 436, 450, 464, 478, 492, 506, 520]],
        "damage_gain": 0.2,
        "attack_power_cof": 180 * 1.15 * 1.1 * 1.1 * 1.1 * 1.05 * 1.1 * 0.7
    },
    37336: {
        "skill_class": MagicalDamage,
        "skill_name": "崇光斩恶",
        "damage_base": 209,
        "damage_rand": 240,
        "attack_power_cof": [e * 1.06 for e in [720, 885, 1217]] + [e * 1.06 * 2.65 for e in [720, 885, 1217]]
    },
    25766: {
        "skill_class": MagicalDamage,
        "skill_name": "守缺式·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 50
    }
}


