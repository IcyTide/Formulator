from typing import Dict

from base.talent import Talent
from base.recipe import DamageAdditionRecipe


TALENT_GAINS: Dict[int, Talent] = {
    6812: Talent("玄黄", [DamageAdditionRecipe(102, 0, 5638)]),
    26702: Talent("坚冰"),
    6337: Talent("斜打狗背"),
    6820: Talent("无疆"),
    32725: Talent("酩酊"),
    6832: Talent("越渊"),
    28818: Talent("温酒"),
    6818: Talent("雨龙"),
    37339: Talent("易损"),
    6814: Talent("复礼"),
    14625: Talent("饮江"),
    14927: Talent("御鸿于天")
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
