from typing import Dict

from base.gain import Gain
from base.skill import Skill


class 腾焰飞芒(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (13468, 4202, 3963):
            skills[skill_id].skill_critical_strike += 1000
            skills[skill_id].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (13468, 4202, 3963):
            skills[skill_id].skill_critical_strike -= 1000
            skills[skill_id].skill_critical_power -= 102


class 净身明礼(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (13468, 3963):
            skills[skill_id].skill_damage_addition += 256

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (13468, 3963):
            skills[skill_id].skill_damage_addition -= 256


TALENT_GAINS: Dict[int, Gain] = {
    5972: 腾焰飞芒("腾焰飞芒"),
    18279: 净身明礼("净身明礼"),
    22888: Gain("诛邪镇魔"),
    6717: Gain("无明业火"),
    34383: Gain("明光恒照"),
    34395: Gain("日月同辉"),
    34372: Gain("靡业报劫"),
    17567: Gain("用晦而明"),
    25166: Gain("净体不畏"),
    34378: Gain("降灵尊"),
    34347: Gain("悬象著明"),
    37337: Gain("崇光斩恶"),
}

TALENTS = [
    [5972],
    [18279],
    [22888],
    [6717],
    [34383],
    [34395],
    [34372],
    [17567],
    [25166],
    [34378],
    [34347],
    [37337]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
