from typing import Dict

from base.attribute import Attribute
from base.gain import Gain
from base.skill import Skill


class 玄黄(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (6369, 6370, 6371, 6372, 6373, 6374):
            skills[skill_id].skill_damage_addition += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (6369, 6370, 6371, 6372, 6373, 6374):
            skills[skill_id].skill_damage_addition -= 102


TALENT_GAINS: Dict[int, Gain] = {
    6812: 玄黄("玄黄"),
    26702: Gain("坚冰"),
    6337: Gain("斜打狗背"),
    6820: Gain("无疆"),
    32725: Gain("酩酊"),
    6832: Gain("越渊"),
    28818: Gain("温酒"),
    6818: Gain("雨龙"),
    37339: Gain("易损"),
    6814: Gain("复礼"),
    14625: Gain("饮江"),
    14927: Gain("御鸿于天")
}

TALENTS = [
    [6812],
    [26702],
    [6337],
    [6820],
    [32725],
    [6832],
    [28818],
    [6818],
    [37339],
    [6814],
    [14625],
    [14927]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
