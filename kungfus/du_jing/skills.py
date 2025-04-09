from typing import Dict

from base.skill import Skill, PetSkill


class 残香吞噬(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        super().record(actual_critical_strike, actual_damage, parser)
        for dot_id in self.consume_dots:
            parser.current_dot_ticks[dot_id] += 1


SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        2183: dict(channel_interval=16), 32818: {},
        # 千劫万毒手
        40066: {}, 9331: {}, 13472: {}, 6238: dict(bind_dots={2509: 1}), 6236: dict(bind_dots={2295: 1}),
        6237: dict(bind_dots={2296: 1}),
        # 引魂蛊术
        18590: {},
        # 驭虫奇术
        2226: dict(post_buffs={2543: {1: 1}}), 2223: dict(pet_buffs={16543: {1: 1}}),
        # 奇穴
        40198: {}, 6648: {}, 34389: {}, 30578: dict(bind_dots={22730: 1}), 13473: {}, 37959: {},
        18700: dict(bind_dots={12557: 1}), 30579: dict(bind_dots={22731: 1}), 37352: dict(bind_dots={28210: 1}),
        38456: {}, 25039: {}, 21303: {}, 25044: {}, 30918: {},
        # 装备
        25773: {}, 39036: {},
    },
    PetSkill: {
        # 通用
        2477: {}, 2472: {}, 2470: {},
        # 奇穴
        22997: {}, 36292: {}
    },
    残香吞噬: {
        38454: dict(consume_dots=[{dot_id: 1} for dot_id in (2296, 25917, 2295, 2509, 12557, 22731, 22730)])
    }
}
