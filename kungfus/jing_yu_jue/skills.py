from typing import Dict

from base.skill import Skill


class 逐一击破判定(Skill):
    final_buff = 10169

    def record(self, actual_critical_strike, actual_damage, parser):
        if not parser.current_buff_stacks[10167].get(1):
            parser.refresh_buff(self.final_buff, 1)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            3121: dict(channel_interval=16), 3095: {}, 3187: {}, 3222: {}, 3291: {}, 6920: {}, 22789: {}, 25775: {},
            32884: {}, 37616: {}, 33870: {}, 37504: {}, 36543: {},
            **{skill_id: {} for skill_id in (21841, 21840, 3227, 8470, 8469, 8468, 8467)},
            3386: dict(post_buffs={3276: {1: 1}, 17103: {1: 1}}),
            30629: dict(post_buffs={3276: {1: 1}, 17103: {1: 1}}, key_skill=True),
            3094: dict(key_skill=True),
            3098: dict(key_skill=True),
            3125: dict(bind_dots={2237: 1}),
            29148: dict(bind_dots={2237: 1}),
            18815: dict(bind_dots={12663: 1}),
            29154: dict(bind_dots={12663: 1})
        },
        逐一击破判定: {
            26551: {}
        }
    }
}
