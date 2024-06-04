from typing import Dict

from base.skill import Skill, Damage, DotDamage


class 吞噬(Skill):
    bind_buff_levels: dict
    bind_buff = -32489

    def record(self, critical, parser):
        if buff_level := self.bind_buff_levels.get(self.skill_level):
            parser.refresh_buff(self.bind_buff, buff_level)
            super().record(critical, parser)
            parser.clear_buff(self.bind_buff, buff_level)
        else:
            super().record(critical, parser)


class 折花吞噬(吞噬):
    bind_dots = {
        **{i + 9: skill_id for i, skill_id in enumerate([714, 666, 711, 24158])}
    }
    bind_buff_levels = {
        **{i + 9: 1 for i in range(4)}
    }

    def record(self, critical, parser):
        self.bind_dot = self.bind_dots[self.skill_level]
        super().record(critical, parser)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        16: dict(damage_addition=205),
        182: {}, 186: {}, 6693: {}, 14941: {}, 25768: {}, 32467: {}, 32501: {}, 33222: {}, 37270: {}, 37525: {}
    },
    DotDamage: {
        711: dict(extra_tick=1),
        714: dict(extra_tick=1),
        666: dict(extra_tick=1),
        24158: {}
    },
    Skill: {
        **{skill_id: dict(bind_dot=711) for skill_id in (18730, 13848, 6136)},
        **{skill_id: dict(bind_dot=714) for skill_id in (285, 13847, 6135)},
        **{skill_id: dict(bind_dot=666) for skill_id in (180, 13849, 6134)},
        **{skill_id: dict(bind_dot=24158) for skill_id in (32409, 32481)},
    },
    吞噬: {
        6129: dict(bind_dot=711, bind_buff_levels={5: 2, 6: 1}),
        6126: dict(bind_dot=714, bind_buff_levels={5: 2, 6: 1}),
        6128: dict(bind_dot=666, bind_buff_levels={5: 2, 6: 1}),
        32410: dict(bind_dot=24158, bind_buff_levels={2: 2, 3: 1})
    },
    折花吞噬: {601: {}}
}
SKILLS = {}
for skill_class, skills in SCHOOL_SKILLS.items():
    for skill_id, attrs in skills.items():
        skill = skill_class(skill_id)
        for attr, value in attrs.items():
            setattr(skill, attr, value)
        SKILLS[skill_id] = skill
