from typing import Dict

from base.gain import Gain
from base.skill import Skill


class 雾锁(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[896].skill_damage_addition += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[896].skill_damage_addition -= 102


class 白虹(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[896].skill_critical_strike += 1000
        skills[896].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[896].skill_critical_strike -= 1000
        skills[896].skill_critical_power -= 102


class 霜锋(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448):
            skills[skill_id].skill_damage_addition += 102
        skills[18670].skill_damage_addition += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448):
            skills[skill_id].skill_damage_addition -= 102
        skills[18670].skill_damage_addition -= 102


class 跬步(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[896].skill_damage_addition += 204
        for skill_id in (3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448):
            skills[skill_id].skill_damage_addition += 204

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[896].skill_damage_addition -= 204
        for skill_id in (3439, 3440, 3441, 3442, 3443, 3444, 3445, 3446, 3447, 3448):
            skills[skill_id].skill_damage_addition -= 204


class 重光(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for i, skill_id in enumerate([18649, 18650, 18651, 18652, 18653]):
            skills[skill_id].skill_damage_addition += int(i * 0.15 * 1024)

    def sub_skills(self, skills: Dict[int, Skill]):
        for i, skill_id in enumerate([18649, 18650, 18651, 18652, 18653]):
            skills[skill_id].skill_damage_addition -= int(i * 0.15 * 1024)


TALENT_GAINS: Dict[int, Gain] = {
    5840: 雾锁("雾锁"),
    5827: 白虹("白虹"),
    5823: Gain("心固"),
    5828: 霜锋("霜锋"),
    357: Gain("化三清"),
    5846: Gain("无形"),
    23614: Gain("归元"),
    5819: Gain("同尘"),
    18695: 跬步("跬步"),
    32411: Gain("正气"),
    14834: Gain("抱阳"),
    18679: Gain("浮生"),
    24945: Gain("破势"),
    18669: 重光("重光"),
    14613: Gain("固本"),
}

TALENTS = [
    [5840, 5827],
    [5823, 5828],
    [357, 5846],
    [23614],
    [5819],
    [18695],
    [32411],
    [14834],
    [18679],
    [24945],
    [18669],
    [14613]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
