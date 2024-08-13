from typing import Dict

from base.gain import Gains
from base.recipe import DamageAdditionRecipe

TALENT_GAINS: Dict[int, Gains] = {
    6812: Gains("玄黄", [DamageAdditionRecipe(102, 0, 5638)]),
    6836: Gains("益元"),
    26702: Gains("坚冰"),
    6337: Gains("斜打狗背"),
    6845: Gains("自强", [DamageAdditionRecipe(205, skill_id, skill_id) for skill_id in (5258, 5354)]),
    6820: Gains("无疆"),
    32725: Gains("酩酊"),
    6832: Gains("越渊"),
    28818: Gains("温酒"),
    6818: Gains("雨龙"),
    30774: Gains("龙醒"),
    37339: Gains("易损"),
    6843: Gains("含弘"),
    6814: Gains("复礼"),
    14625: Gains("饮江"),
    14927: Gains("御鸿于天"),
    28989: Gains("城复于隍")
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
