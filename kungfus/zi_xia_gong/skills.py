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


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            18121: dict(channel_interval=21), 32813: {}, 303: {}, 305: {}, 896: {}, 2299: {}, 2329: {}, 18670: {},
            22014: {}, 36439: {}, 25770: {}, 24944: {}, 21716: {}, 21860: {}, 28379: {}, 30825: {}, 34633: {},
            34634: {}, 32414: {}, 36102: {}, 28590: {}, 32416: {},
            2681: dict(post_buffs={2757: {1: 1}}),
            **{skill_id: {} for skill_id in range(327, 331 + 1)},
            **{skill_id: {} for skill_id in range(461, 465 + 1)},
            **{skill_id: {} for skill_id in range(3439, 3448 + 1)},
            **{skill_id: {} for skill_id in range(6091, 6100 + 1)},
            **{skill_id: {} for skill_id in range(18649, 18653 + 1)},
            **{skill_id: {} for skill_id in range(466, 475 + 1)},
            33592: dict(bind_dot=6424)
        },
        跬步判定: {18698: {}}
    }
}
