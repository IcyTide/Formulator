from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        25512: dict(channel_interval=16), 32886: {},
        # 九字诀
        24558: {}, **{skill_id: {} for skill_id in range(24675, 24677 + 1)},
        **{skill_id: {} for skill_id in range(24811, 24814 + 1)},
        **{skill_id: {} for skill_id in range(24821, 24824 + 1)},
        # 占术
        24454: {},
        # 奇门
        24870: {}, 25233: {}, 28815: {},
        # 奇穴
        30847: {}, 37311: {}, 34683: {}, 25174: {}, 37599: {},
        # 装备
        25837: {}, 33588: {},
    }
}
