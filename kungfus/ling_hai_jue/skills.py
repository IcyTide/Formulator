from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        19712: dict(channel_interval=24), 32815: {},
        # 风起云扬诀
        19766: {}, 19767: {}, 20014: {}, 19819: {},
        # 长空破云式
        20016: {}, 31250: {},
        # 九霄踏云步
        20052: {}, 20054: {},
        # 碧海缥缈掌
        20322: {}, 20323: {}, 20684: {}, 20685: {},
        # 奇穴
        30506: {}, 38675: dict(bind_dots={29350: 1}), 30503: {}, 32595: {},
        # 装备
        25783: {}, 26935: dict(bind_dots={19557: 1})
    }
}
