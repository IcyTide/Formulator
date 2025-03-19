from typing import Dict

from base.skill import Skill, NpcSkill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        35894: dict(channel_interval=24), 35866: {}, 39092: {}, 36157: {}, 36177: {}, 36453: {}, 36579: {},
        36580: {},
        36165: dict(consume_dots={26856: 3}),
        35695: dict(pet_buffs={26857: {1: 1}}),
        35696: dict(pet_count=3, pet_buffs={26857: {1: 1}}),
        35771: dict(bind_dots={26856: 1})
    },
    NpcSkill: {
        36056: {}, 36057: {}, 36111: {}, 36112: {}, 36113: {}, 36114: {},
    }
}
