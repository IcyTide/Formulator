from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        1795: dict(channel_interval=32), 18383: dict(channel_interval=21), 32821: {},
        # 秀水剑法
        1706: {}, 13470: {}, 13471: {}, 26673: {},
        # 灵峰剑式
        1707: {}, 2896: {}, 1594: {}, 1595: {}, 1598: {}, 18317: {}, 18299: {}, 18991: {},
        # 君子风
        1658: dict(post_buffs={-1: {1: 1}}), 1659: dict(post_buffs={-1: {1: -1}}),
        # 奇穴
        30861: {}, 32967: {}, 29129: {},
        # 装备
        25776: {}, 35051: {}
    }
}
