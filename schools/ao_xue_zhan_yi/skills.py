from typing import Dict, Union

from base.skill import Skill, DotSkill, PhysicalDamage, PhysicalDotDamage
from general.skills import GENERAL_SKILLS


class 战意判定(Skill):
    final_buff = -12608
    bind_buff = -1

    def record(self, critical, parser):
        if buff_level := parser.current_buff_stacks.get((self.bind_buff, 1)):
            parser.refresh_buff(self.final_buff, buff_level)


SKILLS: Dict[int, Union[Skill, dict]] = {
    32820: {
        "skill_class": PhysicalDamage,
        "skill_name": "破",
        "surplus_cof": 1048576 * (0.429 - 1)
    },
    12: {
        "skill_class": PhysicalDamage,
        "skill_name": "梅花枪法",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024
    },
    3442: {
        "skill_class": PhysicalDotDamage,
        "skill_name": "流血(DOT)",
        "skill_level": 30,
        "damage_base": 60,
        "attack_power_cof": 248 * 1.15 * 1.05 * 1.05 * 1.1 * 1.1,
        "interval": 32,
        "max_stack": 2,
        "tick": 7
    },
    18591: {
        "skill_class": DotSkill,
        "skill_name": "流血",
        "bind_skill": 3442,
    },
    409: {
        "skill_class": PhysicalDamage,
        "skill_name": "断魂刺",
        "skill_level": 7,
        "damage_base": 39,
        "damage_rand": 3,
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024,
        "post_buffs": {(-1, 1): 3}
    },
    431: {
        "skill_class": PhysicalDamage,
        "skill_name": "突",
        "skill_level": 6,
        "damage_base": 37,
        "damage_rand": 3,
        "weapon_damage_cof": 1024
    },
    14882: {
        "skill_class": PhysicalDamage,
        "skill_name": "突",
        "damage_base": 10,
        "damage_rand": 3,
        "weapon_damage_cof": 1024
    },
    702: {
        "skill_class": type("Mixing", (PhysicalDamage, DotSkill), {}),
        "skill_name": "灭",
        "skill_level": 19,
        "damage_base": 160 * 1.3,
        "damage_rand": 10,
        "attack_power_cof": 170 * 1.12,
        "weapon_damage_cof": 1024,
        "bind_skill": 3442,
    },
    18207: {
        "skill_class": PhysicalDamage,
        "skill_name": "穿云",
        "skill_level": 28,
        "damage_base": 160,
        "damage_rand": 15,
        "attack_power_cof": 158 * 1.05 * 1.1 * 1.1 * 1.12 * 1.1,
        "weapon_damage_cof": 1024,
        "post_buffs": {(-1, 1): 1}
    },
    18603: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙吟",
        "skill_level": 29,
        "damage_base": 289 * 0.65,
        "damage_rand": 15,
        "attack_power_cof": 184 * 1.1 * 1.1 * 1.12 * 1.1 * 1.1 * 1.2,
        "weapon_damage_cof": 1024,
        "post_buffs": {(-1, 1): 2}
    },
    18773: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙牙",
        "skill_level": 29,
        "damage_base": 445 * 0.5,
        "damage_rand": 15,
        "attack_power_cof": 197 * 1.1 * 1.1 * 1.15 * 1.1 * 1.1 * 1.12 * 0.9 * 1.1 * 1.05,
        "weapon_damage_cof": 1024,
        "post_buffs": {(-1, 1): -3}
    },
    37618: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙吟·大漠",
        "damage_base": 70,
        "damage_rand": 5,
        "attack_power_cof": 350,
        "weapon_damage_cof": 1024,
    },
    24898: {
        "skill_class": PhysicalDamage,
        "skill_name": "灭",
        "attack_power_cof": 42,
        "weapon_damage_cof": 1024
    },
    6526: {
        "skill_class": PhysicalDamage,
        "skill_name": "灭",
        "skill_level": 19,
        "damage_base": 242 * 0.95,
        "damage_rand": 242 * 0.1,
        "damage_gain": 1 / 4,
        "attack_power_cof": 170 * 1.12 * 1,
        "weapon_damage_cof": 1024 / 4
    },
    18740: {
        "skill_class": 战意判定,
        "skill_name": "战意判定"
    },
    15002: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙牙",
        "skill_level": 29,
        "damage_base": 445 * 0.5,
        "damage_rand": 15,
        "damage_gain": 0.1,
        "attack_power_cof": 197 * 1.1 * 1.1 * 1.15 * 0.4 * 1.1 * 1.1 * 1.12 * 0.9 * 1.1 * 1.05,
        "weapon_damage_cof": 1024 * 0.1
    },
    **{
        skill_id: {
            "skill_class": Skill,
            "skill_name": "特效触发",
            "post_buffs": {(-1, 1): 5}
        } for skill_id in (1850, 1861)
    },
    25772: {
        "skill_class": PhysicalDamage,
        "skill_name": "龙牙·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 50
    },
    31031: {
        "skill_class": PhysicalDamage,
        "skill_name": "画角闻龙",
        "damage_base": 523 * 0.95,
        "damage_rand": 523 * 0.1,
        "attack_power_cof": 205,
    },
}

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id)
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)

for skill_id, skill in GENERAL_SKILLS.items():
    SKILLS[skill_id] = skill
