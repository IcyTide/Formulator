from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        27451: dict(channel_interval=16), 32841: {}, 28081: {},
        # 行忌制方
        27552: {}, 27555: {}, 27560: dict(bind_dots={20052: 1}), 27557: {}, 27579: {}, 27584: {},
        # 凌波飞叶令
        28346: {}, 27539: {}, **{skill_id: dict(consume_dots=[{20052: 2}] * 31 + [{}]) for skill_id in (29505, 29506)},
        # 神农百草诀
        27657: {}, 28385: {}, 29535: {},
        # 奇穴
        40212: {}, 40208: {}, 28434: {},
        # 装备
        29698: {}, 29695: {}
    }
}
