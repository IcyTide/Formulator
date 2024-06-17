from typing import Dict

from base.skill import Skill, Dot


class 吞噬(Skill):
    bind_buff_levels: dict
    bind_buff = -1

    def record(self, critical, parser):
        if buff_level := self.bind_buff_levels.get(self.skill_level):
            parser.refresh_buff(self.bind_buff, buff_level)
            super().record(critical, parser)
            parser.clear_buff(self.bind_buff, buff_level)
        else:
            super().record(critical, parser)


class 折花吞噬(吞噬):
    consume_dots = {
        **{i + 9: skill_id for i, skill_id in enumerate([714, 666, 711, 24158])}
    }
    bind_buff_levels = {
        **{i + 9: 1 for i in range(4)}
    }

    def record(self, critical, parser):
        self.consume_dot = self.consume_dots[self.skill_level]
        super().record(critical, parser)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        16: dict(damage_addition=205),
        182: {}, 186: {}, 6693: {}, 14941: {}, 25768: {}, 32467: {}, 32501: {}, 33222: {}, 37270: {}, 37525: {},
        **{skill_id: dict(bind_dot=711) for skill_id in (18730, 13848, 6136)},
        **{skill_id: dict(bind_dot=714) for skill_id in (285, 13847, 6135)},
        **{skill_id: dict(bind_dot=666) for skill_id in (180, 13849, 6134)},
        **{skill_id: dict(bind_dot=24158) for skill_id in (32481, 32409)},
    },
    Dot: {
        711: dict(tick_extra=1),
        714: dict(tick_extra=1),
        666: dict(tick_extra=1),
        24158: {}
    },
    吞噬: {
        6129: dict(consume_dot=711, bind_buff_levels={5: 2, 6: 1}),
        6126: dict(consume_dot=714, bind_buff_levels={5: 2, 6: 1}),
        6128: dict(consume_dot=666, bind_buff_levels={5: 2, 6: 1}),
        32410: dict(consume_dot=24158, bind_buff_levels={2: 2, 3: 1})
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
