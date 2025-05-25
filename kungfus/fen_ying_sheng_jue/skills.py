from typing import Dict

from base.skill import Skill


SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        # 通用
        4326: dict(channel_interval=16), 32816: {}, 19055: {},
        # 日月净世
        14701: {}, 4476: {}, 40088: {}, 40089: {}, 6257: {}, 6258: {},
        13359: dict(bind_dots={4202: 1}), 4024: {}, 4025: {}, 4026: {}, 4028: {}, 4029: {}, 4030: {},
        # 御暗烬灭令
        4480: {},
        # 奇穴
        18280: {}, 18281: {}, 26916: dict(global_damage_factor=[0.0, -952664.0 / 2, -952664.0 / 2, -952664.0]),
        26708: {}, 26709: {}, 18631: dict(post_buffs={-12575: {1: 1}}), 34985: {},
        **{skill_id: {} for skill_id in range(34348, 34363 + 1) if skill_id not in [34350, 34351, 34352, 34358]},
        34373: dict(bind_dots={25725: 1}), 34374: dict(bind_dots={25726: 1}), 37336: {},
        # 装备
        25777: {}, 35065: {},
    }
}
