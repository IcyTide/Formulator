from typing import Dict

from base.skill import Skill, DotSkill, PhysicalDamage, MagicalDamage, MagicalDotDamage
from general.skills import GENERAL_SKILLS

SKILLS: Dict[int, Skill | dict] = {
    32813: {
        "skill_class": MagicalDamage,
        "skill_name": "破",
        "surplus_cof": [
            1024 * 1024 * (0.06 - 1),
            1024 * 1024 * (0.30 - 1),
            1024 * 1024 * (0.83 - 1),
            1024 * 1024 * (0.60 - 1)
        ]
    },
    18121: {
        "skill_class": PhysicalDamage,
        "skill_name": "三柴剑法",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024,
        "skill_damage_addition": 205
    },
    303: {
        "skill_class": MagicalDamage,
        "skill_name": "三才化生",
        "damage_base": 780 * 0.1,
        "damage_rand": 78 * 0.1,
        "attack_power_cof": 16
    },
    **{
        skill_id: {
            "skill_class": MagicalDamage,
            "skill_name": "五方行尽",
            "damage_base": [(51 * i / 100) for i in range(1, 11)],
            "attack_power_cof": [(8 * i * 1.4) for i in range(1, 11)],
        } for skill_id in (327, 328, 329, 330, 331, 461, 462, 463, 464, 465)
    },
    896: {
        "skill_class": MagicalDamage,
        "skill_name": "四象轮回",
        "damage_base": 1260 + 827 - 1907,
        "damage_rand": 20,
        "attack_power_cof": 170 * 1.1 * 1.1 * 0.95 * 0.9 * 1.05 * 1.05 * 1.1 * 2.07
    },
    **{
        skill_id: {
            "skill_class": MagicalDamage,
            "skill_name": "两仪化形",
            "damage_base": [(16526 + 10742 * i / 100) for i in range(1, 11)],
            "damage_rand": [273 * i / 100 for i in range(1, 11)],
            "attack_power_cof": [(22.5 * i * 0.85 * 1.1 * 1.1 * 1.05 * 0.9 * 1.05 * 1.05 * 1.1 * 1.1 * 1.32) for i in
                                 range(1, 11)],
        } for skill_id in (3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448)
    },
    **{
        skill_id: {
            "skill_class": MagicalDamage,
            "skill_name": "两仪化形",
            "damage_base": 1298 * 2.1,
            "damage_rand": 1298 * 2.1,
            "attack_power_cof": [(14 * i * 0.8) for i in range(1, 11)],
        } for skill_id in (6091, 6092, 6093, 6094, 6095, 6096, 6097, 6098, 6099, 6100)
    },
    **{
        skill_id: {
            "skill_class": MagicalDamage,
            "skill_name": "飞剑",
            "damage_base": 50,
            "attack_power_cof": 40 * 0.75 * 1.15 * 1.1 * 1.45,
        } for skill_id in (18649, 18650, 18651, 18652, 18653)
    },
    18670: {
        "skill_class": MagicalDamage,
        "skill_name": "六合独尊",
        "damage_base": 1038 / 16,
        "damage_rand": 104 / 2,
        "attack_power_cof": 82 * 2
    },
    22014: {
        "skill_class": MagicalDamage,
        "skill_name": "万世不竭",
        "damage_base": 1150,
        "damage_rand": 78,
        "attack_power_cof": 300 * 1.1 * 1.15 * 1.1 * 1.12
    },
    36439: {
        "skill_class": MagicalDamage,
        "skill_name": "颠越苍穹击",
        "damage_base": 1038,
        "damage_rand": 104,
        "attack_power_cof": 155 * 0.9
    },
    25770: {
        "skill_class": MagicalDamage,
        "skill_name": "四象轮回·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 65
    },
    6424: {
        "skill_class": MagicalDotDamage,
        "skill_name": "气竭(DOT)",
        "damage_base": 10,
        "attack_power_cof": 229 * 1.7,
        "interval": 48,
        "max_stack": 3,
        "tick": 10
    },
    33592: {
        "skill_class": DotSkill,
        "skill_name": "气竭",
        "bind_skill": 6424
    },
}

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id)
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)

for skill_id, skill in GENERAL_SKILLS.items():
    SKILLS[skill_id] = skill
