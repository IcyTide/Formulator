from typing import Dict

from base.gain import Gain

TALENTS: Dict[int, Gain] = {
    6812: Gain("玄黄", recipes=[(1714, 1)]),
    6836: Gain("益元"),
    26702: Gain("坚冰"),
    6337: Gain("斜打狗背"),
    6845: Gain("自强", recipes=[(4764, 1), (4765, 1)]),
    6820: Gain("无疆"),
    32725: Gain("酩酊"),
    6832: Gain("越渊"),
    28818: Gain("温酒"),
    6818: Gain("雨龙"),
    30774: Gain("龙醒"),
    37339: Gain("易损"),
    6843: Gain("含弘"),
    6814: Gain("复礼"),
    14625: Gain("饮江"),
    14927: Gain("御鸿于天"),
    28989: Gain("城复于隍")
}

TALENT_CHOICES = [
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
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
