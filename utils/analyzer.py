from collections import defaultdict
from copy import copy
from dataclasses import dataclass
from functools import cached_property
from typing import Dict, Union, List

from base.attribute import Attribute
from base.constant import FRAME_PER_SECOND
from base.dot import Dot
from base.skill import Skill, NpcSkill, PetSkill
from schools import School


@dataclass
class Detail:
    damage: int = 0
    critical_damage: int = 0
    critical_strike: float = 0.
    expected_damage: float = 0.

    timeline: List[tuple] = None
    gradients: Dict[str, float] = None

    def __post_init__(self):
        self.timeline = []
        self.gradients = defaultdict(float)

    @cached_property
    def count(self):
        return len(self.timeline)

    @cached_property
    def actual_critical_count(self):
        return len([t for t in self.timeline if t[1]])

    @cached_property
    def actual_critical_strike(self):
        return self.actual_critical_count / self.count

    @cached_property
    def total_actual_damage(self):
        return sum([t[-1] for t in self.timeline if t[-1]])

    @cached_property
    def actual_damage(self):
        return self.total_actual_damage / self.count


def filter_status(status, school: School):
    buffs = []
    for buff_id, buff_level, buff_stack in status:
        buff = school.buffs[buff_id]
        if not buff.activate:
            continue
        buff.buff_level, buff.buff_stack = buff_level, buff_stack
        buffs.append(copy(buff))

    return sorted(buffs, key=lambda x: abs(x.buff_id))


def add_buffs(current_buffs, snapshot_buffs, target_buffs, attribute: Attribute, damage: Union[Dot, Skill]):
    if isinstance(damage, Dot):
        display_current_buffs = [buff for buff in current_buffs if buff.add_dot(attribute, damage.bind_skill, False)]
        display_snapshot_buffs = [buff for buff in snapshot_buffs if buff.add_dot(attribute, damage.bind_skill, True)]
        display_target_buffs = [buff for buff in target_buffs if buff.add_all(attribute, damage.bind_skill)]
    elif isinstance(damage, NpcSkill):
        display_current_buffs = [buff for buff in current_buffs if buff.add_all(attribute, damage)]
        display_snapshot_buffs = [buff for buff in snapshot_buffs if buff.add_all(attribute, damage)]
        display_target_buffs = [buff for buff in target_buffs if buff.add_all(attribute, damage)]
    elif isinstance(damage, PetSkill):
        display_current_buffs = [buff for buff in current_buffs if buff.add_all(attribute, damage)]
        display_snapshot_buffs = [buff for buff in snapshot_buffs if buff.add_pet(attribute, damage)]
        display_target_buffs = [buff for buff in target_buffs if buff.add_all(attribute, damage)]
    else:
        display_current_buffs = [buff for buff in current_buffs if buff.add_all(attribute, damage)]
        display_snapshot_buffs = []
        display_target_buffs = [buff for buff in target_buffs if buff.add_all(attribute, damage)]

    return display_current_buffs, display_snapshot_buffs, display_target_buffs


def sub_buffs(current_buffs, snapshot_buffs, target_buffs, attribute: Attribute, damage: Union[Dot, Skill]):
    if isinstance(damage, Dot):
        for buff in current_buffs:
            buff.sub_dot(attribute, damage.bind_skill, False)
        for buff in snapshot_buffs:
            buff.sub_dot(attribute, damage.bind_skill, True)
        for buff in target_buffs:
            buff.sub_all(attribute, damage.bind_skill)
    elif isinstance(damage, NpcSkill):
        for buff in current_buffs:
            buff.sub_all(attribute, damage)
        for buff in snapshot_buffs:
            buff.sub_all(attribute, damage)
        for buff in target_buffs:
            buff.sub_all(attribute, damage)
    elif isinstance(damage, PetSkill):
        for buff in current_buffs:
            buff.sub_all(attribute, damage)
        for buff in snapshot_buffs:
            buff.sub_pet(attribute, damage)
        for buff in target_buffs:
            buff.sub_all(attribute, damage)
    else:
        for buff in current_buffs:
            buff.sub_all(attribute, damage)
        for buff in target_buffs:
            buff.sub_all(attribute, damage)


def concat_buffs(current_buffs, snapshot_buffs, target_buffs):
    buffs = []
    if current_buffs:
        buffs.append(",".join(buff.display_name for buff in current_buffs))
    if snapshot_buffs:
        buffs.append(",".join(buff.display_name for buff in snapshot_buffs))
    if target_buffs:
        buffs.append(",".join(buff.display_name for buff in target_buffs))

    if buffs:
        buffs = ";".join(buffs)
    else:
        buffs = "~"
    return buffs


def analyze_details(record, start_frame, end_frame, attribute: Attribute, school: School):
    total = Detail()
    details = {}
    summary = {}
    start_frame = int(start_frame * FRAME_PER_SECOND)
    end_frame = int(end_frame * FRAME_PER_SECOND)

    for damage, status in record.items():
        damage_tuple, dot_skill_tuple = damage
        if dot_skill_tuple:
            dot_id, dot_level, dot_stack = damage_tuple
            damage, damage.buff_level, damage.buff_stack = school.dots[dot_id], dot_level, dot_stack
            dot_skill_id, dot_skill_level = dot_skill_tuple
            dot_skill, dot_skill.skill_level = school.skills[dot_skill_id], dot_skill_level
            damage.bind_skill = dot_skill
            damage_name = damage.buff_name
        else:
            skill_id, skill_level = damage_tuple
            damage, damage.skill_level, = school.skills[skill_id], skill_level
            damage_name = damage.skill_name
        if not damage.activate:
            continue
        damage_detail = details[damage.display_name] = {}
        if not (damage_summary := summary.get(damage_name)):
            damage_summary = summary[damage_name] = Detail()
        damage_total = damage_detail[""] = Detail()
        for (current_status, snapshot_status, target_status), timeline in status.items():
            if not (timeline := [t for t in timeline if start_frame <= t[0] < end_frame]):
                continue

            current_buffs = filter_status(current_status, school)
            snapshot_buffs = filter_status(snapshot_status, school)
            target_buffs = filter_status(target_status, school)

            display_buffs = add_buffs(current_buffs, snapshot_buffs, target_buffs, attribute, damage)
            buffs = concat_buffs(*display_buffs)
            if buffs in damage_detail:
                detail = damage_detail[buffs]
            else:
                detail = damage_detail[buffs] = Detail(*damage(attribute))
                detail.gradients = analyze_gradients(damage, attribute)
            sub_buffs(current_buffs, snapshot_buffs, target_buffs, attribute, damage)

            detail.timeline += timeline
            damage_total.timeline += timeline

            damage_total.damage += detail.damage * len(timeline)
            damage_total.critical_damage += detail.critical_damage * len(timeline)
            damage_total.critical_strike += detail.critical_strike * len(timeline)
            damage_total.expected_damage += detail.expected_damage * len(timeline)
            for attr, residual_damage in detail.gradients.items():
                damage_total.gradients[attr] += residual_damage * len(timeline)

        if damage_total.timeline:
            total.expected_damage += damage_total.expected_damage
            damage_summary.critical_strike += damage_total.critical_strike
            damage_summary.expected_damage += damage_total.expected_damage
            damage_summary.timeline += damage_total.timeline
            damage_total.damage /= len(damage_total.timeline)
            damage_total.critical_damage /= len(damage_total.timeline)
            damage_total.expected_damage /= len(damage_total.timeline)
            damage_total.critical_strike /= len(damage_total.timeline)
            for attr, residual_damage in damage_total.gradients.items():
                total.gradients[attr] += residual_damage
                damage_total.gradients[attr] /= len(damage_total.timeline)
        else:
            details.pop(damage.display_name)

    summary = {damage: detail for damage, detail in summary.items() if detail.count}
    return total, summary, details


def analyze_gradients(damage, attribute):
    results = {}
    for attr, value in attribute.grad_attrs.items():
        origin_value = getattr(attribute, attr)
        setattr(attribute, attr, origin_value + value)
        _, _, _, results[attr] = damage(attribute)
        setattr(attribute, attr, origin_value)
    return results
