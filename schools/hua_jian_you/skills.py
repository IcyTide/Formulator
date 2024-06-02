from typing import Dict

from base.skill import Damage, DotDamage, DotSkill, DotConsumeSkill


class 吞噬(DotConsumeSkill):
    bind_buff_levels: dict
    bind_buff = -32489

    def record(self, critical, parser):
        if not (last_dot := parser.current_last_dot.pop(self.bind_skill, None)):
            return
        if self.skill_level not in self.bind_buff_levels:
            return

        skill_tuple, status_tuple = last_dot
        if buff_level := self.bind_buff_levels[self.skill_level]:
            current_status, snapshot_status, target_status = status_tuple
            new_target_status = (*target_status, (self.bind_buff, buff_level, 1))
            new_status_tuple = (current_status, snapshot_status, new_target_status)
        else:
            new_status_tuple = status_tuple
        skill_id, skill_level, skill_stack = skill_tuple
        parser.current_dot_ticks[skill_id] += 1
        tick = parser.current_dot_ticks.pop(skill_id)
        parser.current_records[(skill_id, skill_level, skill_stack * tick)][new_status_tuple].append(
            parser.current_records[skill_tuple][status_tuple].pop()
        )


class 折花吞噬(吞噬):
    bind_skills = {
        **{i + 9: skill_id for i, skill_id in enumerate([714, 666, 711, 24158])}
    }
    bind_buff_levels = {
        **{i + 9: 1 for i in range(4)}
    }

    def record(self, critical, parser):
        if self.skill_level not in self.bind_skills:
            return
        self.bind_skill = self.bind_skills[self.skill_level]
        super().record(critical, parser)


SCHOOL_SKILLS: Dict[type, Dict[int, dict]] = {
    Damage: {
        11: {}, 182: {}, 186: {}, 6693: {}, 14941: {}, 25768: {}, 32467: {}, 32501: {}, 33222: {}, 37270: {}, 37525: {}
    },
    DotDamage: {
        711: {},
        714: {},
        666: {},
        24158: {}
    },
    DotSkill: {
        **{skill_id: {"bind_skill": 711} for skill_id in (18730, 13848, 6136)},
        **{skill_id: {"bind_skill": 714} for skill_id in (285, 13847, 6135)},
        **{skill_id: {"bind_skill": 666} for skill_id in (180, 13849, 6134)},
        **{skill_id: {"bind_skill": 24158} for skill_id in (32409, 32481)},
    },
    吞噬: {
        6129: {"bind_skill": 711, "bind_buff_levels": {5: 2, 6: 1}},
        6126: {"bind_skill": 714, "bind_buff_levels": {5: 2, 6: 1}},
        6128: {"bind_skill": 666, "bind_buff_levels": {5: 2, 6: 1}},
        32410: {"bind_skill": 24158, "bind_buff_levels": {2: 2, 3: 1}}
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
