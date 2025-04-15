from typing import Dict

from base.skill import Skill


class 跬步判定(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[12779].get(1):
            parser.refresh_buff(-12550, 1)
            parser.refresh_buff(-12551, 1)
        elif parser.current_buff_stacks[12780].get(1):
            parser.refresh_buff(-12550, 2)
            parser.refresh_buff(-12551, 2)
        elif parser.current_buff_stacks[12781].get(1):
            parser.refresh_buff(-12550, 3)
            parser.refresh_buff(-12551, 3)
        elif parser.current_buff_stacks[12782].get(1):
            parser.refresh_buff(-12550, 4)
            parser.refresh_buff(-12551, 4)
        elif parser.current_buff_stacks[12783].get(1):
            parser.refresh_buff(-12550, 5)
            parser.refresh_buff(-12551, 5)


SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        18121: dict(channel_interval=21), 32813: {},
        # 北冥剑气
        303: {}, 305: {}, 28381: {}, 896: {},
        **{skill_id: {} for skill_id in list(range(327, 331 + 1)) + list(range(461, 465 + 1))},
        **{skill_id: {} for skill_id in range(3439, 3448 + 1)},
        **{skill_id: {} for skill_id in range(18649, 18653 + 1)}, 22014: {},
        # 坐忘经
        2681: dict(post_buffs={2757: {1: 1}}),
        # 奇穴
        **{skill_id: {} for skill_id in range(6091, 6100 + 1)},
        40158: {}, 36438: {}, 18670: {},
        # 装备
        25770: {}
    },
    跬步判定: {18698: {}}
}
