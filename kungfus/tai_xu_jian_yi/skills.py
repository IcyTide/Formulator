from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        18121: dict(channel_interval=21), 32814: {},
        # 天道剑势
        17689: {}, 17690: {}, 21979: {}, 38534: {}, 37453: dict(bind_dots={889: 1}), 4954: {}, 14975: {},
        **{skill_id: {} for skill_id in range(386, 394 + 1)},
        600: dict(bind_dots={748: 1}),
        # 坐忘经
        2681: dict(post_buffs={2757: {1: 1}}),
        # 奇穴
        **{skill_id: {} for skill_id in range(6076, 6085 + 1)}, 26699: {}, 31012: {}, 40752: {},
        6761: dict(consume_dots={748: 0}), 21726: {}, 34693: {}, 34694: {},
        # 装备
        25771: {},
    }
}
