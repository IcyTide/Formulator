from typing import Dict, Union

from base.skill import Skill, DotSkill, PhysicalDamage, PhysicalDotDamage, MagicalDamage
from general.skills import GENERAL_SKILLS


class 盾压(PhysicalDamage):
    def record(self, critical, parser):
        if parser.current_buff_stacks.get((8474, 13)):
            self.post_buffs[(-1, 1)] = 15 * 2
        else:
            self.post_buffs[(-1, 1)] = 15

        super().record(critical, parser)


class 绝刀(PhysicalDamage):
    final_buff = -9052
    bind_buff = -1

    def record(self, critical, parser):
        current_rage = parser.current_buff_stacks.get((-1, 1), 0)
        cost_rage = min(current_rage, 50)
        buff_level = cost_rage // 10 - 1
        if buff_level > 0:
            parser.refresh_buff(self.final_buff, buff_level)
        if parser.current_buff_stacks.get((8451, 1)):
            self.post_buffs[(-1, 1)] = 0
        elif parser.current_buff_stacks.get((8474, 13)):
            self.post_buffs[(-1, 1)] = 0
        else:
            self.post_buffs[(-1, 1)] = -cost_rage
        super().record(critical, parser)


SKILLS: Dict[int, Union[Skill, dict]] = {
    32745: {
        "skill_class": PhysicalDamage,
        "skill_name": "破",
        "surplus_cof": [
            1048576 * (0.4 - 1),
            1048576 * (0.55 * 0.33 - 1),
            1048576 * (0.7 - 1),
            1048576 * (0.8 * 0.33 - 1),
            1048576 * (0.9 - 1),
        ]
    },
    13039: {
        "skill_class": PhysicalDamage,
        "skill_name": "卷雪刀",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024
    },
    **{
        skill_id: {
            "skill_class": PhysicalDamage,
            "skill_name": "盾击",
            "damage_base": [150, 180, 210, 240, 270, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 520],
            "damage_rand": [e * 0.1 for e in
                            [50, 80, 100, 120, 140, 160, 180, 200, 240, 280, 320, 360, 400, 440, 480, 520]],
            "damage_gain": 1 / 5,
            "attack_power_cof": [16 * 1.05 * 1.05 * 1.1 * 1.1] * 4 +
                                [(16 + (i - 4) * 5) * 1.05 * 1.05 * 1.1 * 1.1 for i in range(5, 16)] +
                                [100 * 1.05 * 1.05 * 1.1 * 1.1],
            "weapon_damage_cof": 1024,
            "skill_shield_gain": -512,
            "post_buffs": {(-1, 1): 10}
        } for skill_id in (13106, 13160, 13161)
    },
    19409: {
        "skill_class": 盾压,
        "skill_name": "盾压",
        "damage_base": [30, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300, 315, 330, 345,
                        360, 375, 390, 405],
        "damage_rand": [e * 0.1 for e in
                        [20, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300, 315,
                         330, 345, 360, 375]],
        "damage_gain": 1 / 2,
        "attack_power_cof": [40 * 1.05 * 1.05 * 1.05 * 1.1] * 4 +
                            [(40 + (i - 4) * 7) * 1.05 * 1.05 * 1.05 * 1.1 for i in range(5, 24)] +
                            [190 * 1.05 * 1.05 * 1.05 * 1.1],
        "weapon_damage_cof": 1024
    },
    13099: {
        "skill_class": PhysicalDamage,
        "skill_name": "盾猛",
        "damage_base": [35, 75, 85, 95, 105, 115, 125, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300, 315,
                        330, 345, 360, 375, 390],
        "damage_rand": [e * 0.1 for e in
                        [35, 45, 55, 65, 75, 85, 95, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285,
                         300, 315, 330, 345, 360]],
        "damage_gain": 1 / 3,
        "attack_power_cof": [40 * 1.05 * 1.05 * 1.05] * 4 +
                            [(40 + (i - 4) * 4) * 1.05 * 1.05 * 1.05 for i in range(5, 25)] +
                            [150 * 1.05 * 1.05 * 1.05],
        "weapon_damage_cof": 1024,
        "post_buffs": {(-1, 1): 15}
    },
    13040: {
        "skill_class": Skill,
        "skill_name": "血怒",
        "post_buffs": {(-1, 1): 10 + 15}
    },
    13463: {
        "skill_class": PhysicalDamage,
        "skill_name": "盾飞",
        "damage_base": [30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 300],
        "damage_rand": [e * 0.1 for e in
                        [20, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 300]],
        "damage_gain": 1 / 10,
        "attack_power_cof": [16] * 4 +
                            [16 + (i - 4) * 1 for i in range(5, 18)] +
                            [35],
        "weapon_damage_cof": 1024,
        "post_target_buffs": {(-8248, 1): 1}
    },
    13044: {
        "skill_class": PhysicalDamage,
        "skill_name": "盾刀",
        "damage_base": [31, 40, 45, 48, 55, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96,
                        98, 102, 106, 110, 114, 118, 122, 126, 130],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15,
                        15, 15, 15, 15, 15, 15, 15],
        "attack_power_cof": [16 * 1.05 * 1.05 * 1.1] * 4 +
                            [(16 + (i - 4) * 3) * 1.05 * 1.05 * 1.1 for i in range(5, 33)] +
                            [100 * 1.05 * 1.05 * 1.1],
        "weapon_damage_cof": 1024,
        "post_buffs": {(-1, 1): 5}
    },
    8249: {
        "skill_class": PhysicalDotDamage,
        "skill_name": "流血(DOT)",
        "damage_base": 47,
        "attack_power_cof": [16 * 1.5 * 2 * 1.05 * 1.1] * 9 +
                            [(16 + (i - 9) * 4) * 1.5 * 2 * 1.05 * 1.1 for i in range(10, 22)] +
                            [70 * 1.5 * 2 * 1.05 * 1.1],
        "interval": 32,
        "tick": 13
    },
    29188: {
        "skill_class": DotSkill,
        "skill_name": "流血",
        "bind_skill": 8249,
        "post_target_buffs": {(-8248, 1): -1}
    },
    13075: {
        "skill_class": 绝刀,
        "skill_name": "绝刀",
        "damage_base": [240, 270, 300, 330, 350, 370, 390, 410, 430, 450, 470, 490, 510, 540, 570, 600, 630, 660, 690,
                        720],
        "damage_rand": [e * 0.1 for e in
                        [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440,
                         500]],
        "damage_gain": 1 / 4,
        "attack_power_cof": [60 * 0.9 * 0.75 * 0.9 * 1.1 * 1.05 * 1.05 * 1.05 * 1.22 * 1.05 * 1.05 * 1.1 * 1.06] * 4 +
                            [(60 + (i - 4) * 12) * 0.9 * 0.75 * 0.9 * 1.1 * 1.05 * 1.05 * 1.05 * 1.22 * 1.05 * 1.05 *
                             1.1 * 1.06 for i in range(5, 20)] +
                            [250 * 0.75 * 0.9 * 1.1 * 1.05 * 1.05 * 1.05 * 1.22 * 1.05 * 1.05 * 1.1 * 1.06],
        "weapon_damage_cof": 1024
    },
    13092: {
        "skill_class": PhysicalDamage,
        "skill_name": "斩刀",
        "damage_base": [230, 260, 290, 320, 350, 380, 410, 440, 470, 510, 550, 580, 610, 640, 670, 700, 710, 720, 730,
                        740, 750, 760],
        "damage_rand": [e * 0.1 for e in
                        [20, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300, 315,
                         330, 345]],
        "damage_gain": 0.3,
        "attack_power_cof": [50 * 0.9 * 0.85 * 1.05 * 1.1 * 1.15 * 1.15 * 1.05 * 1.1 * 1.1 * 1.06 * 1.2] * 4 +
                            [(50 + (i - 4) * 10) * 0.9 * 0.85 * 1.05 * 1.1 * 1.15 * 1.15 * 1.05 * 1.1 * 1.1 * 1.06 * 1.2
                             for i in range(5, 22)] +
                            [250 * 0.9 * 0.85 * 1.05 * 1.1 * 1.15 * 1.15 * 1.05 * 1.1 * 1.1 * 1.06 * 1.2],
        "weapon_damage_cof": 1024,
        "post_buffs": {(-1, 1): -15}
    },
    28479: {
        "skill_class": PhysicalDamage,
        "skill_name": "劫刀",
        "damage_base": [e / 5 for e in
                        [120, 150, 180, 210, 230, 250, 270, 290, 310, 330, 350, 370, 390, 400, 410, 420, 430, 440, 450,
                         460, 470, 480, 490, 500, 510, 520, 530, 550]],
        "damage_rand": [e * 0.1 for e in
                        [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 120, 130, 140, 150, 160, 170, 180, 190, 200,
                         210, 220, 230, 240, 250, 260, 270, 280, 290]],
        "attack_power_cof": [20 * 1.1 * 1.05 * 1.1 * 1.05 * 1.1 * 1.05 * 1.06] * 9 +
                            [(20 + (i - 9) * 7) * 1.1 * 1.05 * 1.1 * 1.05 * 1.1 * 1.05 * 1.06
                             for i in range(10, 28)] +
                            [160 * 1.1 * 1.05 * 1.1 * 1.05 * 1.1 * 1.05 * 1.06],
        "weapon_damage_cof": 1024,
        "post_buffs": {(-1, 1): -5}
    },
    36065: {
        "skill_class": PhysicalDamage,
        "skill_name": ["击破·援戈", "斩破·惊涌", "绝破·惊涌", "闪破·惊涌", "劫破·惊涌"],
        "surplus_cof": [
            1048576 * (0.697 * 0.5 * 1.2 - 1),
            1048576 * (0.697 * 0.14 * 1.2 * 1.2 - 1),
            1048576 * (0.697 * 0.14 * 1.2 * 1.2 - 1),
            1048576 * (0.697 * 0.14 * 1.2 - 1),
            1048576 * (0.697 * 0.14 * 1.2 - 1),
        ]
    },
    36482: {
        "skill_class": PhysicalDamage,
        "skill_name": "援戈·血影",
        "damage_base": 400 / 5,
        "damage_rand": 150 * 0.1,
        "attack_power_cof": 300 * 2.3 * 0.83 * 1.2,
        "weapon_damage_cof": 1024
    },
    37253: {
        "skill_class": PhysicalDamage,
        "skill_name": "麾远",
        "damage_base": 400 / 5,
        "damage_rand": 150 * 0.1,
        "attack_power_cof": 170 * 2,
    },
    34673: {
        "skill_class": PhysicalDamage,
        "skill_name": "业火焚城",
        "attack_power_cof": 40,
        "weapon_damage_cof": 1024
    },
    34674: {
        "skill_class": PhysicalDamage,
        "skill_name": "麟光甲寒",
        "damage_base": 400 / 5,
        "damage_rand": 150 * 0.1,
        "attack_power_cof": 220 * 1.3 * 1.2,
        "weapon_damage_cof": 1024
    },
    34714: {
        "skill_class": PhysicalDamage,
        "skill_name": "业火焚城·云盾",
        "damage_base": 400 / 5,
        "damage_rand": 150 * 0.1,
        "attack_power_cof": 160 * 1.3,
        "weapon_damage_cof": 1024
    },
    37448: {
        "skill_class": PhysicalDamage,
        "skill_name": "破·麟光",
        "surplus_cof": 1048576 * (0.697 * 0.14 * 1.2 - 1)
    },
    30925: {
        "skill_class": PhysicalDamage,
        "skill_name": "阵云结晦",
        "damage_base": 240,
        "damage_rand": 80 * 0.1,
        "damage_gain": 1.2 / 4,
        "attack_power_cof": 80 * 2 * 1.5,
        "weapon_damage_cof": 1024,
        "skill_pve_addition": 614
    },
    30926: {
        "skill_class": PhysicalDamage,
        "skill_name": "月照连营",
        "damage_base": 320,
        "damage_rand": 120 * 0.1,
        "damage_gain": 1.2 / 4,
        "attack_power_cof": 100 * 2 * 1.5,
        "weapon_damage_cof": 1024,
        "skill_pve_addition": 614
    },
    30857: {
        "skill_class": PhysicalDamage,
        "skill_name": "雁门迢递",
        "damage_base": [400, 460, 520, 580, 640, 700, 760],
        "damage_rand": [e * 0.1 for e in [300, 320, 340, 360, 380, 400, 420]],
        "damage_gain": 1.2 / 4,
        "attack_power_cof": 120 * 2 * 1.5,
        "weapon_damage_cof": 1024,
        "skill_pve_addition": 614
    },
    30858: {
        "skill_class": PhysicalDamage,
        "skill_name": "绝国",
        "damage_base": 24,
        "damage_rand": 15 * 0.1,
        "damage_gain": 1.2 / 4,
        "attack_power_cof": [20 * (i + 1) * 1.2 * 1.3 for i in range(15)] +
                            [40 * i * 1.2 * 1.3 for i in range(16, 80)] +
                            [40 * 80 * 1.2 * 1.3],
        "weapon_damage_cof": 1024,
    },
    30859: {
        "skill_class": PhysicalDamage,
        "skill_name": "阵云绝",
        "damage_base": 47,
        "damage_rand": 28 * 0.1,
        "damage_gain": 1.2 / 4,
        "attack_power_cof": 80 * 1.2,
        "weapon_damage_cof": 1024,
        "skill_pve_addition": 614
    },

    16727: {
        "skill_class": Skill,
        "skill_name": "魂吸",
        "post_buffs": {(-1, 1): 3}
    },
    23284: {
        "skill_class": PhysicalDamage,
        "skill_name": "争神焱舞",
        "damage_base": [86625, 88698, 119225],
        "interval": 30,
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024
    },
    23285: {
        "skill_class": PhysicalDamage,
        "skill_name": "苍蛟扫狼",
        "damage_base": [57750, 59132, 79483],
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024
    },
    23286: {
        "skill_class": PhysicalDamage,
        "skill_name": "争神焱舞",
        "damage_base": [144375, 147831, 198708],
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024
    },
    23287: {
        "skill_class": MagicalDamage,
        "skill_name": "炎帝反击",
        "damage_base": [121904, 286452, 410323],
        "attack_power_cof": 16
    },
    23294: {
        "skill_class": MagicalDamage,
        "skill_name": "苍炎",
        "damage_base": [122, 380, 380],
        "attack_power_cof": 16
    },
    25780: {
        "skill_class": PhysicalDamage,
        "skill_name": "盾击·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 50
    }
}


