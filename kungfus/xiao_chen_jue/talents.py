from typing import Dict, List

from base.gain import Gain

TALENTS: List[Dict[int, Gain]] = [
    {
        6812: Gain("玄黄", recipes=[(1714, 1)])
    },
    {
        26702: Gain("坚冰", skill_ids=[26703]),
        6813: Gain("御龙")
    },
    {
        6845: Gain("自强", recipes=[(5879, 1)])
    },
    {
        6820: Gain("无疆", buff_ids=[6377])
    },
    {
        32725: Gain("酩酊")
    },
    {
        6832: Gain("越渊", buff_ids=[5994])
    },
    {
        6810: Gain("落水打狗")
    },
    {
        6818: Gain("雨龙", dot_ids=[6401], skill_ids=[6867]),
        6824: Gain("驯致", skill_ids=list(range(19430, 19439 + 1)), recipes=[(4340, 1)]),
        14633: Gain("亢野", skill_ids=list(range(18909, 18974 + 1)))
    },
    {
        38878: Gain("追远", skill_ids=[38891])
    },
    {
        6814: Gain("复礼", buff_ids=[12356]),
        6843: Gain("含弘", buff_ids=[12356])
    },
    {
        25197: Gain("祭湘君", skill_ids=[25201, 25202])
    },
    {
        40331: Gain("潜龙勿用", skill_ids=[40335])
    }
]
