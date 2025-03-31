from typing import Dict

from base.skill import Skill, NpcSkill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        35894: dict(channel_interval=24), 36177: {}, 36157: {}, 35771: dict(bind_dots={26856: 1}),
        # 上弦星流术
        35866: {}, 39092: {}, 36579: {},
        # 山海同归契
        35695: dict(pet_buffs={26857: {1: 1}}), 35696: dict(pet_count=3, pet_buffs={26857: {1: 1}}),
        # 奇穴
        36165: dict(consume_dots={26856: 3}), 40717: {}, 36453: {},
        # 装备
        36580: {},
    },
    NpcSkill: {
        36056: {}, 36057: {}, 36111: {}, 36112: {}, 36113: {}, 36114: {},
    }
}
