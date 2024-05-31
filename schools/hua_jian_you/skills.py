from typing import Dict, Union

from base.skill import Skill, DotSkill, PhysicalDamage, MagicalDamage, MagicalDotDamage
from general.skills import GENERAL_SKILLS


class DotConsumeSkill(Skill):
    bind_buff_levels: dict

    def record(self, critical, parser):
        if not (last_dot := parser.current_last_dot.pop(self.bind_skill, None)):
            return
        if self.skill_level not in self.bind_buff_levels:
            return

        skill_tuple, status_tuple = last_dot
        if buff_level := self.bind_buff_levels[self.skill_level]:
            current_status, snapshot_status, target_status = status_tuple
            new_target_status = (*target_status, (-32489, buff_level, 1))
            new_status_tuple = (current_status, snapshot_status, new_target_status)
        else:
            new_status_tuple = status_tuple
        skill_id, skill_level, skill_stack = skill_tuple
        parser.current_dot_ticks[skill_id] += 1
        tick = parser.current_dot_ticks.pop(skill_id)
        parser.current_records[(skill_id, skill_level, skill_stack * tick)][new_status_tuple].append(
            parser.current_records[skill_tuple][status_tuple].pop()
        )


class GeneraConsumeSkill(DotConsumeSkill):
    bind_skills = {
        **{i + 9: skill_id for i, skill_id in enumerate([714, 666, 711, 24158])}
    }
    bind_buff_levels = {
        **{i + 9: 1 for i in range(4)}
    }

    def record(self, critical, parser):
        if self.skill_level not in self.bind_skills:
            return
        self.bind_skill = self.bind_skills[self.skill_level]
        super().record(critical, parser)


SKILLS: Dict[int, Union[Skill, dict]] = {
    32467: {
        "skill_class": MagicalDamage,
        "skill_name": "破",
        "surplus_cof": [
            -1048576 * (1 - (0.2813 * 0.83 * 0.927 * 1.15 * (1 + 0.2 * i)))
            for i in range(7)
        ]
    },
    11: {
        "skill_class": PhysicalDamage,
        "skill_name": "六合棍",
        "attack_power_cof": 16,
        "weapon_damage_cof": 1024,
        "skill_damage_addition": 205
    },
    711: {
        "skill_class": MagicalDotDamage,
        "skill_name": "兰摧玉折(DOT)",
        "damage_base": 30,
        "attack_power_cof": [(28 + 48 * 0.9 * 1.25 * 1.15 * 1.05 * 1.1 * 1.05 * 1.15 * 1.1) * 1.05 * 1.05 * 1.05] * 9 +
                            [(28 + (48 + (i - 9) * 9) * 0.9 * 1.25 * 1.15 * 1.05 * 1.1 * 1.05 * 1.15 * 1.1) * 1.05 *
                             1.05 * 1.05 for i in range(10, 19)] +
                            [(28 + 155 * 0.9 * 1.25 * 1.15 * 1.05 * 1.1 * 1.05 * 1.15 * 1.1) * 1.05 * 1.05 * 1.05],
        "interval": 48,
        "tick": 6 + 1
    },
    **{
        skill_id: {
            "skill_class": DotSkill,
            "skill_name": "兰摧玉折",
            "bind_skill": 711
        } for skill_id in (13848, 6136)  # 18730
    },
    6129: {
        "skill_class": DotConsumeSkill,
        "skill_name": "兰摧玉折",
        "bind_skill": 711,
        "bind_buff_levels": {5: 2, 6: 1}
    },
    714: {
        "skill_class": MagicalDotDamage,
        "skill_name": "钟林毓秀(DOT)",
        "damage_base": 38,
        "attack_power_cof": [48 * 0.9 * 1.25 * 1.15 * 1.05 * 1.15 * 1.1 * 1.05 * 1.05 * 1.05] * 9 +
                            [(48 + (i - 9) * 8) * 0.9 * 1.25 * 1.15 * 1.05 * 1.15 * 1.1 * 1.05 * 1.05 * 1.05 for i in
                             range(10, 24)] +
                            [175 * 0.9 * 1.25 * 1.15 * 1.05 * 1.15 * 1.1 * 1.05 * 1.05 * 1.05],
        "interval": 48,
        "tick": 6 + 1
    },
    **{
        skill_id: {
            "skill_class": DotSkill,
            "skill_name": "钟林毓秀",
            "bind_skill": 714
        } for skill_id in (285, 13847, 6135)
    },
    6126: {
        "skill_class": DotConsumeSkill,
        "skill_name": "钟林毓秀",
        "bind_skill": 714,
        "bind_buff_levels": {5: 2, 6: 1}
    },
    14941: {
        "skill_class": MagicalDamage,
        "skill_name": "阳明指",
        "damage_base": [38, 44, 49, 54, 59, 63, 69, 71, 73, 75, 77, 79, 81, 83, 85, 86, 90, 94, 98, 102, 105, 110, 115,
                        120, 125, 135, 145, 155],
        "damage_rand": [5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                        27, 28],
        "attack_power_cof": [48 * 1.365 * 1.2 * 1.05 * 1.1 * 1.15] * 9 +
                            [(48 + (i - 9) * 4) * 1.365 * 1.2 * 1.05 * 1.1 * 1.15 for i in range(10, 28)] +
                            [130 * 1.365 * 1.2 * 1.05 * 1.1 * 1.15],
    },
    666: {
        "skill_class": MagicalDotDamage,
        "skill_name": "商阳指(DOT)",
        "damage_base": 50,
        "attack_power_cof": [64 * 0.9 * 1.25 * 1.15 * 1.05 * 1.15 * 1.05 * 1.05 * 1.1] * 9 +
                            [(64 + (i - 9) * 4) * 0.9 * 1.25 * 1.15 * 1.05 * 1.15 * 1.05 * 1.05 * 1.1 for i in
                             range(10, 29)] +
                            [161 * 0.9 * 1.25 * 1.15 * 1.05 * 1.15 * 1.05 * 1.05 * 1.1],
        "interval": 48,
        "tick": 6 + 1
    },
    **{
        skill_id: {
            "skill_class": DotSkill,
            "skill_name": "商阳指",
            "bind_skill": 666
        } for skill_id in (180, 6134)
    },
    6128: {
        "skill_class": DotConsumeSkill,
        "skill_name": "商阳指",
        "bind_skill": 666,
        "bind_buff_levels": {5: 2, 6: 1}
    },
    6693: {
        "skill_class": MagicalDamage,
        "skill_name": "商阳指",
        "attack_power_cof": [64 * 1.15] * 9 +
                            [(64 + (i - 9) * 4) * 1.15 for i in range(10, 29)] +
                            [161 * 1.15],
    },
    182: {
        "skill_class": MagicalDamage,
        "skill_name": "玉石俱焚",
        "damage_base": [20, 22, 24, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68,
                        69, 72, 75, 78, 81],
        "damage_rand": [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10],
        "attack_power_cof": 64 * 1.15
    },
    186: {
        "skill_class": MagicalDamage,
        "skill_name": "芙蓉并蒂",
        "damage_base": [28, 43, 61, 76],
        "damage_rand": 5,
        "attack_power_cof": 64 * 1.15
    },
    33222: {
        "skill_class": MagicalDamage,
        "skill_name": "快雪时晴",
        "damage_base": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55,
                        57, 59, 61, 63, 65],
        "damage_rand": [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10],
        "attack_power_cof": [44 * 0.9 * 1.05 * 1.1 * 1.15 * 1.23] * 9 +
                            [(44 + (i - 9) * 2) * 0.9 * 1.05 * 1.1 * 1.15 * 1.23 for i in range(10, 29)] +
                            [84 * 0.9 * 1.05 * 1.1 * 1.15 * 1.23],
        "skill_damage_addition": 512,
    },
    24158: {
        "skill_class": MagicalDotDamage,
        "skill_name": "快雪时晴(DOT)",
        "damage_base": 38,
        "attack_power_cof": (28 + 155 * 0.9 * 1.25 * 1.15 * 1.05 * 1.1 * 1.05 * 1.15 * 1.1) * 1.05 * 1.2 * 0.12,
        "interval": 64,
        "tick": 7,
        "max_stack": 6
    },
    **{
        skill_id: {
            "skill_class": DotSkill,
            "skill_name": "快雪时晴",
            "bind_skill": 24158
        } for skill_id in (32409, 32481)
    },
    32410: {
        "skill_class": DotConsumeSkill,
        "skill_name": "快雪时晴",
        "bind_skill": 24158,
        "bind_buff_levels": {2: 2, 3: 1}
    },
    601: {
        "skill_class": GeneraConsumeSkill,
        "skill_name": "折花吞噬",
    },
    32501: {
        "skill_class": MagicalDamage,
        "skill_name": "折花",
        "damage_base": 155,
        "damage_rand": 28,
        "attack_power_cof": [304] * 3 + [334]
    },
    37525: {
        "skill_class": MagicalDamage,
        "skill_name": "钟灵",
        "damage_base": 121,
        "damage_rand": 10,
        "attack_power_cof": 328
    },
    37270: {
        "skill_class": MagicalDamage,
        "skill_name": ["墨海", "临源"],
        "damage_base": 33,
        "damage_rand": 2,
        "damage_gain": 1.05 * 2 / 2,
        "attack_power_cof": [1800 * 1.1] +
                            [1800 * 2.5 * 1.1],
    },
    25768: {
        "skill_class": MagicalDamage,
        "skill_name": "兰摧玉折·神兵",
        "damage_base": 20,
        "damage_rand": 2,
        "attack_power_cof": 100
    }
}


