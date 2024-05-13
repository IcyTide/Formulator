from typing import Dict

from base.skill import Skill, DotSkill, DotConsumeSkill, PhysicalDamage, MagicalDamage, MagicalDotDamage, \
    MagicalPetDamage
from general.skills import GENERAL_SKILLS


class 灵蛇引(Skill):
    bind_buffs: list

    def record(self, critical, parser):
        super().record(critical, parser)
        pet_buffs = {(bind_buff, 1): 1 for bind_buff in self.bind_buffs}
        parser.current_next_pet_buff_stacks.append(pet_buffs)


SKILLS: Dict[int, Skill | dict] = {
    32818: {
        "skill_class": MagicalDamage,
        "skill_name": "破",
        "surplus_cof": [
            1048576 * (0.46 - 1),
            1048576 * (0.575 - 1),
            1048576 * (0.92 - 1),
            1048576 * (1.035 - 1),
            1048576 * (0.2 - 1)
        ],
        "skill_shield_gain": [-819] * 4 + [0],
    },
    2183: {
        "skill_class": PhysicalDamage,
        "skill_name": "大荒笛法",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024,
        "skill_damage_addition": 205
    },
    18590: {
        "skill_class": MagicalDotDamage,
        "skill_name": "蛊毒",
        "damage_base": 30 * 0.95,
        "damage_rand": 30 * 0.1,
        "attack_power_cof": 16,
        "interval": 32,
        "tick": 6
    },
    6218: {
        "skill_class": MagicalDotDamage,
        "skill_name": "蝎心(DOT)",
        "damage_base": 80,
        "attack_power_cof": 270 * 1.3 * 1.1 * 1.1 * 1.15,
        "interval": 32,
        "tick": 6
    },
    6621: {
        "skill_class": DotSkill,
        "skill_name": "蝎心",
        "bind_skill": 6218
    },
    25917: {
        "skill_class": MagicalDotDamage,
        "skill_name": "蛇影(DOT)",
        "damage_base": 55,
        "attack_power_cof": 286 * 1.1 * 1.15,
        "interval": 32,
        "max_stack": 2,
        "tick": 6 + 1
    },
    34643: {
        "skill_class": DotSkill,
        "skill_name": "蛇影",
        "bind_skill": 25917
    },
    34879: {
        "skill_class": DotConsumeSkill,
        "skill_name": "蛇影",
        "bind_skill": 25917,
        "tick": 99
    },
    13472: {
        "skill_class": MagicalDamage,
        "skill_name": "百足",
        "damage_base": [e * 0.85 for e in
                        [85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175,
                         180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250]],
        "damage_rand": [e * 0.1 for e in
                        [16, 22, 29, 35, 42, 48, 55, 61, 68, 74, 81, 87, 94, 100, 107, 113, 120, 126, 133, 139, 146,
                         152, 159, 165, 172, 178, 185, 191, 198, 204, 211, 217, 224, 230]],
        "attack_power_cof": 216 * 1.15 * 1.1 * 1.05 * 1.1 * 1.2
    },
    2509: {
        "skill_class": MagicalDotDamage,
        "skill_name": "百足(DOT)",
        "damage_base": 92,
        "attack_power_cof": 232 * 1.1 * 1.05 * 1.1 * 1.15 * 1.2,
        "interval": 48,
        "tick": 6
    },
    6238: {
        "skill_class": DotSkill,
        "skill_name": "百足",
        "bind_skill": 2509
    },
    2295: {
        "skill_class": MagicalDotDamage,
        "skill_name": "蟾啸(DOT)",
        "damage_base": 50,
        "attack_power_cof": 232 * 1.1 * 1.05 * 1.15 * 1.15,
        "interval": 32,
        "tick": 7
    },
    6236: {
        "skill_class": DotSkill,
        "skill_name": "蟾啸",
        "bind_skill": 2295
    },
    34389: {
        "skill_class": MagicalDamage,
        "skill_name": "黯影",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 100,
    },
    29573: {
        "skill_class": MagicalDamage,
        "skill_name": "篾片蛊",
        "damage_base": [225, 260, 295, 330, 365, 400],
        "damage_rand": [19, 20, 21, 22, 23, 24],
        "attack_power_cof": [(117 * (5 + (i + 1)) * 1.15 * 1.1) * 1.1 for i in range(6)]
    },
    25044: {
        "skill_class": MagicalDamage,
        "skill_name": "连缘蛊",
        "damage_base": 43 * 0.95,
        "damage_rand": 43 * 0.1,
        "attack_power_cof": 100 * 0.9 * 1.1 * 1.1,
        "pve_addition": 256,
        "skill_shield_ignore": -819
    },
    30918: {
        "skill_class": MagicalDamage,
        "skill_name": "连缘蛊",
        "damage_base": [e * 0.95 for e in [43, 70, 94, 117, 141, 164, 188, 212, 235, 259, 384]],
        "damage_rand": [e * 0.1 for e in [43, 70, 94, 117, 141, 164, 188, 212, 235, 259, 384]],
        "attack_power_cof": [100 * (i + 1) * 1.1 * 1.1 for i in range(11)],
        "skill_pve_addition": 256,
        "skill_shield_ignore": -819
    },
    2223: {
        "skill_class": 灵蛇引,
        "skill_name": "灵蛇引",
        "bind_buffs": []
    },
    2472: {
        "skill_class": MagicalPetDamage,
        "skill_name": "攻击",
        "damage_base": [e * 0.95 for e in [43, 70, 94, 117, 141, 164, 188, 212, 235, 259, 384]],
        "damage_rand": [e * 0.1 for e in [43, 70, 94, 117, 141, 164, 188, 212, 235, 259, 384]],
        "attack_power_cof": 86 * 1.5,
        "skill_pve_addition": 154,
    },
    22997: {
        "skill_class": MagicalPetDamage,
        "skill_name": "攻击",
        "damage_base": [e * 0.95 for e in [43, 70, 94, 117, 141, 164, 188, 212, 235, 259, 384]],
        "damage_rand": [e * 0.1 for e in [43, 70, 94, 117, 141, 164, 188, 212, 235, 259, 384]],
        "attack_power_cof": 86 * 1.5,
        "skill_pve_addition": 154,
    },
    36292: {
        "skill_class": MagicalPetDamage,
        "skill_name": "幻击",
        "damage_base": 205 * 0.95,
        "damage_rand": 205 * 0.1,
        "attack_power_cof": 115,
    },
    25019: {
        "skill_class": MagicalPetDamage,
        "skill_name": "荒息",
        "damage_base": [e * 0.95 for e in [43, 70, 94, 117, 141, 164, 188, 212, 235, 259, 384]],
        "damage_rand": [e * 0.1 for e in [43, 70, 94, 117, 141, 164, 188, 212, 235, 259, 384]],
        "attack_power_cof": 86 * 1.5 * 2 * 0.9 * 0.9,
    },
    25773: {
        "skill_class": MagicalDamage,
        "skill_name": "蛇影·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 60
    },
    3067: {
        "skill_class": MagicalDamage,
        "skill_name": "赤蛇",
        "damage_base": 240 * 0.85,
        "damage_rand": 217 * 0.1,
        "attack_power_cof": 530
    },
    18882: {
        "skill_class": MagicalDotDamage,
        "skill_name": "赤蛇(DOT)",
        "damage_base": 20,
        "attack_power_cof": 315,
        "interval": 48,
        "max_stack": 3,
        "tick": 10
    },
    26226: {
        "skill_class": DotSkill,
        "skill_name": "赤蛇",
        "bind_skill": 18882
    }
}

for skill_id, detail in SKILLS.items():
    SKILLS[skill_id] = detail.pop('skill_class')(skill_id)
    for attr, value in detail.items():
        setattr(SKILLS[skill_id], attr, value)

for skill_id, skill in GENERAL_SKILLS.items():
    SKILLS[skill_id] = skill
