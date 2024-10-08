from typing import Dict

from base.skill import Skill


class 风逝加成(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if buff_stack := parser.current_target_buff_stacks[29451].get(1):
            parser.refresh_target_buff(-29451, 1, buff_stack)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.clear_target_buff(-29451)
            parser.clear_target_buff(29451)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            18121: dict(channel_interval=21), 589: {}, 21726: {}, 21979: {}, 25771: {}, 32814: {}, 34693: {}, 34694: {},
            36272: {}, 24973: {}, 24977: {}, 38534: {}, 32780: {}, 18528: {}, 18529: {}, 14975: {},
            2681: dict(post_buffs={2757: {1: 1}}),
            **{skill_id: {} for skill_id in range(386, 394 + 1)},
            **{skill_id: {} for skill_id in range(6076, 6085 + 1)},
            32408: dict(consume_dots={748: 1}),
            6761: dict(consume_dots={748: 0}),
            600: dict(bind_dots={748: 1}),
            37453: dict(bind_dots={889: 1}),
            30944: dict(bind_dots={23170: 1})
        },
        风逝加成: {
            4954: {}
        }
    },
    1: {
        Skill: {
            100010: {}, 100011: {}, 101658: {}, 100374: {}, 100019: {}, 100012: {}, 100017: {}, 100003: {}, 100008: {},
            101633: {},
            101581: dict(bind_dots={70624: 1}),
            100021: dict(consume_dots={70624: 0}),
            101634: dict(consume_dots={70624: 0}),
        }
    }
}
