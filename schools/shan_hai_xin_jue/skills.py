from typing import Dict

from base.skill import PhysicalDamage, PhysicalDotDamage, Skill
from general.skills import GENERAL_SKILLS

SKILLS: Dict[int, Skill | dict] = {
    32823: {
        "skill_class": PhysicalDamage,
        "skill_name": "破",
        "surplus_cof": 0
    },
    35894: {
        "skill_class": PhysicalDamage,
        "skill_name": "风矢",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024
    },
    35866: {
        "skill_class": PhysicalDamage,
        "skill_name": "劲风簇",
        "attack_power_cof": 0,
        "weapon_damage_cof": 0
    },
    35987: {
        "skill_class": PhysicalDamage,
        "skill_name": "饮羽簇",
        "attack_power_cof": 0,
        "weapon_damage_cof": 0
    },
    36056: {
        "skill_class": PhysicalDamage,
        "skill_name": "践踏",
        "attack_power_cof": 0
    },
    36057: {
        "skill_class": PhysicalDamage,
        "skill_name": "重击",
        "attack_power_cof": 0
    },
    36111: {
        "skill_class": PhysicalDamage,
        "skill_name": "攻击",
        "attack_power_cof": 0
    },
    36112: {
        "skill_class": PhysicalDamage,
        "skill_name": "攻击",
        "attack_power_cof": 0
    },
    36113: {
        "skill_class": PhysicalDamage,
        "skill_name": "攻击",
        "attack_power_cof": 0
    },
    36114: {
        "skill_class": PhysicalDamage,
        "skill_name": "攻击",
        "attack_power_cof": 0
    },
    36157: {
        "skill_class": PhysicalDamage,
        "skill_name": "标鹄",
        "attack_power_cof": 0
    },
    26856: {
        "skill_class": PhysicalDamage,
        "skill_name": "贯穿(DOT)",
        "attack_power_cof": 0
    },
    35771: {
        "skill_class": Skill,
        "skill_name": "贯穿",
        "bind_skill": 26856,
        "max_stack": 6,
        "tick": 4
    },
    36453: {
        "skill_class": PhysicalDamage,
        "skill_name": "朝仪万汇",
        "attack_power_cof": 0
    }
}

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id, detail.pop('skill_name'))
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)

for skill_id, skill in GENERAL_SKILLS.items():
    SKILLS[skill_id] = skill
