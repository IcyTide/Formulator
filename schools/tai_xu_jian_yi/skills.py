from typing import Dict

from base.constant import DOT_DAMAGE_SCALE
from base.skill import Skill, DotSkill, DotConsumeSkill, PhysicalDamage, PhysicalDotDamage
from general.skills import GENERAL_SKILLS

SKILLS: Dict[int, Skill | dict] = {
    36177: {
        "skill_class": PhysicalDamage,
        "skill_name": "破",
        "surplus_cof": [
            1048576 * (0.3 - 1),
            1048576 * (0.3 - 1)
        ]
    },
    35894: {
        "skill_class": PhysicalDamage,
        "skill_name": "风矢",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024,
        "skill_damage_addition": 205 + 250
    },
    35866: {
        "skill_class": PhysicalDamage,
        "skill_name": "劲风簇",
        "damage_base": [35, 70, 105, 140, 157, 175, 193, 210, 228, 245, 263, 280, 298, 315, 333],
        "damage_rand": 5,
        "attack_power_cof": [25 * 0.9 * 0.9 * 0.95] * 3 +
                            [(25 + (i - 4) * 10) * 0.9 * 0.9 * 0.95 for i in range(4, 15)] +
                            [175 * 0.9 * 0.9 * 0.95],
        "weapon_damage_cof": 1024
    },
    35987: {
        "skill_class": PhysicalDamage,
        "skill_name": "饮羽簇",
        "damage_base": [77, 154, 321, 308, 347, 385, 424, 462, 501, 539, 578, 616, 655, 693, 732],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10],
        "attack_power_cof": [66 * 0.9 * 0.9 * 0.95 * 0.9 * 0.95] * 3 +
                            [(66 + (i - 4) * 38) * 0.9 * 0.9 * 0.95 * 0.9 * 0.95 for i in range(4, 15)] +
                            [552 * 0.9 * 0.9 * 0.95 * 0.9 * 0.95],
        "weapon_damage_cof": 2048
    },
    36056: {
        "skill_class": PhysicalDamage,
        "skill_name": "践踏",
        "damage_base": [16, 44, 72, 100, 128, 156, 184, 212, 240, 268, 296],
        "damage_rand": 20,
        "attack_power_cof": [70 * 1.05] * 2 +
                            [(70 + (i - 3) * 58) * 1.05 for i in range(3, 11)] +
                            [607 * 1.05],
        "skill_damage_addition": 62
    },
    36057: {
        "skill_class": PhysicalDamage,
        "skill_name": "重击",
        "damage_base": [16, 44, 72, 100, 128, 156, 184, 212, 240, 268, 296],
        "damage_rand": 20,
        "attack_power_cof": [33 * 1.05] * 2 +
                            [(33 + (i - 3) * 26) * 1.05 for i in range(3, 11)] +
                            [276 * 1.05],
        "skill_damage_addition": 62
    },
    36111: {
        "skill_class": PhysicalDamage,
        "skill_name": "攻击",
        "damage_base": [16, 44, 72, 100, 128, 156, 184, 212, 240, 268, 296],
        "damage_rand": 20,
        "attack_power_cof": [33 * 1.05] * 2 +
                            [(33 + (i - 3) * 26) * 1.05 for i in range(3, 11)] +
                            [276 * 1.05],
        "skill_damage_addition": 62
    },
    36112: {
        "skill_class": PhysicalDamage,
        "skill_name": "攻击",
        "damage_base": [48, 132, 216, 300, 384, 468, 552, 636, 720, 804, 296],
        "damage_rand": 20,
        "attack_power_cof": [99 * 1.05] * 2 +
                            [(99 + (i - 3) * 26) * 1.05 for i in range(3, 11)] +
                            [828 * 1.05],
        "skill_damage_addition": 62
    },
    36113: {
        "skill_class": PhysicalDamage,
        "skill_name": "攻击",
        "damage_base": [16, 44, 72, 100, 128, 156, 184, 212, 240, 268, 296],
        "damage_rand": 20,
        "attack_power_cof": [70 * 1.05] * 2 +
                            [(70 + (i - 3) * 26) * 1.05 for i in range(3, 11)] +
                            [607 * 1.05],
        "skill_damage_addition": 62
    },
    36114: {
        "skill_class": PhysicalDamage,
        "skill_name": "攻击",
        "damage_base": [16, 44, 72, 100, 128, 156, 184, 212, 240, 268, 296],
        "damage_rand": 20,
        "attack_power_cof": [23 * 1.05] * 2 +
                            [(23 + (i - 3) * 26) * 1.05 for i in range(3, 11)] +
                            [165 * 1.05],
        "skill_damage_addition": 62
    },
    36157: {
        "skill_class": PhysicalDamage,
        "skill_name": "标鹄",
        "damage_base": 30,
        "damage_rand": 20,
        "attack_power_cof": 512 * 1.15 * 0.9 * 0.95
    },
    26856: {
        "skill_class": PhysicalDotDamage,
        "skill_name": "贯穿(DOT)",
        "damage_base": 32,
        "attack_power_cof": 215 * 0.7 * 1.15 * 0.9 * 0.9 * 0.9,
        "interval": DOT_DAMAGE_SCALE * 4
    },
    36165: {
        "skill_class": DotConsumeSkill,
        "skill_name": "贯穿",
        "bind_skill": 26856,
        "tick": 3
    },
    35771: {
        "skill_class": DotSkill,
        "skill_name": "贯穿",
        "bind_skill": 26856,
        "max_stack": 6,
        "tick": 4
    },
    36453: {
        "skill_class": PhysicalDamage,
        "skill_name": "朝仪万汇",
        "damage_base": 37,
        "damage_rand": 5,
        "attack_power_cof": 215
    },
    36579: {
        "skill_class": PhysicalDamage,
        "skill_name": "劲风簇·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 60
    },
    36580: {
        "skill_class": PhysicalDamage,
        "skill_name": "月弦激星",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 390
    }
}

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id, detail.pop('skill_name'))
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)

for skill_id, skill in GENERAL_SKILLS.items():
    SKILLS[skill_id] = skill
