from typing import Dict

from base.constant import DOT_DAMAGE_SCALE, FRAME_PER_SECOND
from base.skill import Skill, DotSkill, PhysicalDamage, PhysicalDotDamage
from general.skills import GENERAL_SKILLS


class 横刀断浪流血(Skill):
    def record(self, current_frame, player_id, skill_level, skill_stack, critical, parser):
        bind_skill = self.bind_skill
        bind_buff = self.bind_buff
        parser.ticks[player_id][bind_skill] = self.tick
        parser.stacks[player_id][bind_skill] = self.max_stack
        parser.status[player_id][(bind_buff, 1)] = self.max_stack
        parser.snapshot[player_id][bind_skill] = parser.status[player_id].copy()


SKILLS: Dict[int, Skill | dict] = {
    33146: {
        "skill_class": PhysicalDamage,
        "skill_name": "破",
        "surplus_cof": 1048576 * (0.48 - 1)
    },
    **{
        skill_id: {
            "skill_class": PhysicalDamage,
            "skill_name": "云刀",
            "attack_power_cof": 16,
            "weapon_damage_cof": 1024
        } for skill_id in (32974, 32975)
    },
    32510: {
        "skill_class": PhysicalDamage,
        "skill_name": "避实击虚",
        "damage_base": [35, 42, 45, 50, 55, 60],
        "damage_rand": 5,
        "attack_power_cof": [80 * 0.9, 100 * 0.9 * 0.9, 120 * 0.9 * 0.9, 160 * 0.8 * 0.9, 160 * 0.9, 200 * 0.9]
    },
    32246: {
        "skill_class": PhysicalDamage,
        "skill_name": "留客雨",
        "damage_base": [35, 42, 45, 50, 52, 55, 56, 58, 60, 62, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 109, 115,
                        120, 130, 140, 150, 160],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15,
                        15],
        "damage_gain": 1.1,
        "attack_power_cof": [90] * 11 +
                            [(100 + (i - 12) * 5) for i in range(12, 27)] +
                            [200],
        "weapon_damage_cof": 1024
    },
    32766: {
        "skill_class": PhysicalDamage,
        "skill_name": "触石雨",
        "damage_base": [180, 200],
        "damage_rand": [15, 30],
        "attack_power_cof": [200, 200 * 1.6]
    },
    32149: {
        "skill_class": PhysicalDamage,
        "skill_name": "行云势·一",
        "damage_base": [35, 42, 45, 50, 52, 55, 56, 58, 60, 62, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 109, 115,
                        120, 130, 140, 150, 160, 170, 180],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15,
                        15, 15, 15],
        "attack_power_cof": [40 * 1.5] * 12 +
                            [(40 + (i - 12) * 5) * 1.5 for i in range(13, 30)] +
                            [135 * 1.5],
        "weapon_damage_cof": 1024
    },
    32150: {
        "skill_class": PhysicalDamage,
        "skill_name": "行云势·二",
        "damage_base": [35, 42, 45, 50, 52, 55, 56, 58, 60, 62, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 109, 115,
                        120, 130, 140, 150, 160, 170, 180],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15,
                        15, 15, 15],
        "damage_gain": 1.2,
        "attack_power_cof": [50 * 1.5] * 12 +
                            [(50 + (i - 12) * 5) * 1.5 for i in range(13, 30)] +
                            [159 * 1.5],
        "weapon_damage_cof": 2048
    },
    32151: {
        "skill_class": PhysicalDamage,
        "skill_name": "行云势·三",
        "damage_base": [35, 42, 45, 50, 52, 55, 56, 58, 60, 62, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 109, 115,
                        120, 130, 140, 150, 160, 170, 180],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15,
                        15, 15, 15],
        "damage_gain": 1.5,
        "attack_power_cof": [70 * 1.5 * 1.5] * 12 +
                            [(70 + (i - 12) * 5) * 1.5 * 1.5 for i in range(13, 30)] +
                            [190 * 1.5 * 1.5],
        "weapon_damage_cof": 2048
    },
    32154: {
        "skill_class": PhysicalDamage,
        "skill_name": "决云势",
        "damage_base": [107, 120, 132, 144, 157, 55, 56, 58, 60, 62, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 109,
                        115, 120, 130, 140, 150, 160],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15,
                        15],
        "damage_gain": 1.25,
        "attack_power_cof": [50 + i * 15 for i in range(1, 3)] +
                            [80 + i * 20 for i in range(3, 5)] +
                            [188],
        "weapon_damage_cof": 1024
    },
    32167: {
        "skill_class": PhysicalDamage,
        "skill_name": "断云势",
        "damage_base": [62, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 109, 115],
        "damage_rand": [5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15],
        "damage_gain": 1.5,
        "attack_power_cof": [(120 + i * 10) * 0.9 for i in range(1, 6)] +
                            [(150 + i * 15) * 0.9 for i in range(6, 14)] +
                            [380 * 0.9],
        "weapon_damage_cof": 2048
    },
    32348: {
        "skill_class": PhysicalDamage,
        "skill_name": "断云势",
        "damage_base": [62, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 109, 115],
        "damage_rand": [5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15],
        "damage_gain": 1.5 * 0.4,
        "attack_power_cof": [(120 + i * 10) * 0.9 for i in range(1, 6)] +
                            [(150 + i * 15) * 0.9 for i in range(6, 14)] +
                            [380 * 0.9],
        "attack_power_cof_gain": 0.4,
        "weapon_damage_cof": 2048
    },
    32602: {
        "skill_class": PhysicalDamage,
        "skill_name": "沧浪三叠·一",
        "damage_base": [76, 85, 94, 107, 118, 125, 135, 145, 155, 165, 175, 185, 190, 200, 205, 210, 215, 220, 225, 230,
                        235, 240, 245, 250, 255],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20, 20],
        "damage_gain": 0.8,
        "attack_power_cof": [130] * 11 +
                            [(160 + (i - 12) * 5) for i in range(12, 25)] +
                            [230],
        "weapon_damage_cof": 2048
    },
    32603: {
        "skill_class": PhysicalDamage,
        "skill_name": "沧浪三叠·二",
        "damage_base": [76, 85, 94, 107, 118, 125, 135, 145, 155, 165, 175, 185, 190, 200, 205, 210, 215, 220, 225, 230,
                        235, 240, 245, 250, 255],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20, 20],
        "damage_gain": 1.05,
        "attack_power_cof": [155] * 11 +
                            [(185 + (i - 12) * 5) for i in range(12, 25)] +
                            [255],
        "weapon_damage_cof": 2560
    },
    32604: {
        "skill_class": PhysicalDamage,
        "skill_name": "沧浪三叠·三",
        "damage_base": [76, 85, 94, 107, 118, 125, 135, 145, 155, 165, 175, 185, 190, 200, 205, 210, 215, 220, 225, 230,
                        235, 240, 245, 250, 255],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20, 20],
        "damage_gain": 1.15,
        "attack_power_cof": [180] * 11 +
                            [(210 + (i - 12) * 5) for i in range(12, 25)] +
                            [290],
        "weapon_damage_cof": 3072
    },
    **{
        skill_id: {
            "skill_class": 横刀断浪流血,
            "skill_name": "流血",
            "bind_skill": 24443,
            "bind_buff": -32513,
            "max_stack": i + 1,
            "tick": 3
        } for i, skill_id in enumerate([32874, 32873, 32872, 32871, 32870, 32869])
    },
    24443: {
        "skill_class": PhysicalDotDamage,
        "skill_name": "流血(DOT)",
        "damage_base": 114,
        "attack_power_cof": 100,
        "interval": FRAME_PER_SECOND * DOT_DAMAGE_SCALE / 3
    },
    32234: {
        "skill_class": PhysicalDamage,
        "skill_name": "横云断浪",
        "damage_base": [547, 588, 629, 670, 711, 752, 793, 834, 875, 916, 957, 998, 1039, 1080, 1121, 1162, 1203],
        "damage_rand": [e * 0.1 for e in
                        [547, 588, 629, 670, 711, 752, 793, 834, 875, 916, 957, 998, 1039, 1080, 1121, 1162, 1203]],
        "damage_gain": 0.6,
        "attack_power_cof": [300 * 0.8] * 5 +
                            [(320 + (i - 6) * 10) * 0.8 for i in range(6, 17)] +
                            [450 * 0.8],
        "weapon_damage_cof": 3072
    },
    **{
        skill_id: {
            "skill_class": PhysicalDamage,
            "skill_name": "孤锋破浪",
            "damage_base": [90, 98, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290],
            "damage_rand": [5, 5, 5, 5, 5, 10, 10, 10, 10, 15, 15, 15],
            "damage_gain": 5,
            "attack_power_cof": [400 * 0.9 * 0.85 * 0.9 * 1.1] * 4 +
                                [(400 + (i - 5) * 30) * 0.9 * 0.85 * 0.9 * 1.1 for i in range(5, 12)] +
                                [650 * 0.9 * 0.85 * 0.9 * 1.1],
            "weapon_damage_cof": 3072
        } for skill_id in (32235, 32236, 32237, 32238, 32239, 32891, 32892)
    },
    32357: {
        "skill_class": PhysicalDamage,
        "skill_name": "驰风八步",
        "damage_base": [10, 13, 16, 19, 22, 25],
        "damage_rand": 5,
        "attack_power_cof": 45,
    },
    36118: {
        "skill_class": PhysicalDamage,
        "skill_name": "潋风·携刃",
        "damage_base": 78,
        "damage_rand": 10,
        "attack_power_cof": 150 * 1.1 * 1.25,
    },
    33239: {
        "skill_class": PhysicalDamage,
        "skill_name": "行云势·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 60
    },
    27820: {
        "skill_class": PhysicalDotDamage,
        "skill_name": "斩浪破锋(DOT)",
        "damage_base": 25,
        "attack_power_cof": 500,
        "interval": 48

    },
    36851: {
        "skill_class": DotSkill,
        "skill_name": "斩浪破锋",
        "bind_skill": 27820,
        "max_stack": 3,
        "tick": 6
    }
}

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id, detail.pop('skill_name'))
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)

for skill_id, skill in GENERAL_SKILLS.items():
    SKILLS[skill_id] = skill
