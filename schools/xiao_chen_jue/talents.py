from typing import Dict

from base.recipe import DamageAdditionRecipe
from base.talent import Talent

TALENT_GAINS: Dict[int, Talent] = {
    6812: Talent("玄黄", [DamageAdditionRecipe(102, 0, 5638)]),
    6836: Talent("益元"),
    26702: Talent("坚冰"),
    6337: Talent("斜打狗背"),
    6845: Talent("自强", [DamageAdditionRecipe(205, skill_id, skill_id) for skill_id in (5258, 5354)]),
    6820: Talent("无疆"),
    32725: Talent("酩酊"),
    6832: Talent("越渊"),
    28818: Talent("温酒"),
    6818: Talent("雨龙"),
    30774: Talent("龙醒"),
    37339: Talent("易损"),
    6843: Talent("含弘"),
    6814: Talent("复礼"),
    14625: Talent("饮江"),
    14927: Talent("御鸿于天"),
    28989: Talent("城复于隍")
}

TALENTS = [
    [6812],
    [26702, 6836],
    [6337, 6845],
    [6820],
    [32725],
    [6832],
    [28818],
    [6818, 30774],
    [37339],
    [6814, 6843],
    [14625],
    [14927, 28989]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
