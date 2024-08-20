from typing import Dict

from base.gain import Gain
from base.skill import Skill


class 血魄(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[13040].post_buffs[-1][1] += 25

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[13040].post_buffs[-1][1] -= 25


TALENTS: Dict[int, Gain] = {
    13317: Gain("刀魂"),
    13090: Gain("绝返"),
    13087: Gain("分野", recipes=[(1823, 1)]),
    21281: 血魄("血魄"),
    22897: Gain("锋鸣"),
    37239: Gain("麾远"),
    34912: Gain("业火麟光"),
    13126: Gain("恋战"),
    25203: Gain("扶阵"),
    36058: Gain("援戈"),
    36205: Gain("惊涌"),
    14838: Gain("蔑视", buff_ids=[-9889]),
    30769: Gain("阵云结晦"),
    32619: Gain("祭血关山")
}

TALENT_CHOICES = [
    [13317],
    [13090],
    [13087],
    [21281],
    [22897],
    [37239],
    [34912],
    [13126, 25203],
    [36058],
    [36205],
    [14838],
    [30769, 32619]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
