from collections import defaultdict
from copy import copy
from dataclasses import dataclass
from typing import Dict, Union

from base.attribute import Attribute
from base.constant import FRAME_PER_SECOND
from base.skill import Skill, NpcSkill, PetSkill
from base.dot import Dot
from schools import School


@dataclass
class Detail:
    damage: int = 0
    critical_damage: int = 0
    critical_strike: float = 0.
    expected_damage: float = 0.

    gradients: Dict[str, float] = None

    critical_count: int = 0
    count: int = 0

    def __post_init__(self):
        self.gradients = defaultdict(float)

    @property
    def actual_critical_strike(self):
        if self.count:
            return self.critical_count / self.count
        return 0


def filter_status(status, school: School):
    buffs = []
    for buff_id, buff_level, buff_stack in status:
        buff = school.buffs[buff_id]
        if not buff.activate:
            continue
        buff.buff_level, buff.buff_stack = buff_level, buff_stack
        buffs.append(copy(buff))

    return sorted(buffs, key=lambda x: x.buff_id)


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


def analyze_details(record, duration: int, attribute: Attribute, school: School):
    total = Detail()
    details = {}
    summary = {}
    duration *= FRAME_PER_SECOND

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
            damage, damage.skill_level,  = school.skills[skill_id], skill_level
            damage_name = damage.skill_name
        if not damage.activate:
            continue
        damage_detail = details[damage.display_name] = {}
        if not (damage_summary := summary.get(damage_name)):
            damage_summary = summary[damage_name] = Detail()
        damage_total = damage_detail[""] = Detail()
        for (current_status, snapshot_status, target_status), timeline in status.items():
            if not (timeline := [t for t in timeline if t[0] < duration]):
                continue
            critical_timeline = [t for t in timeline if t[1]]

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

            detail.critical_count += len(critical_timeline)
            detail.count += len(timeline)
            damage_total.critical_count += len(critical_timeline)
            damage_total.count += len(timeline)

            damage_total.damage += detail.damage * len(timeline)
            damage_total.critical_damage += detail.critical_damage * len(timeline)
            damage_total.critical_strike += detail.critical_strike * len(timeline)
            damage_total.expected_damage += detail.expected_damage * len(timeline)
            for attr, residual_damage in detail.gradients.items():
                damage_total.gradients[attr] += residual_damage * len(timeline)

        if damage_total.count:
            total.expected_damage += damage_total.expected_damage
            damage_summary.expected_damage += damage_total.expected_damage
            damage_summary.critical_count += damage_total.critical_strike
            damage_summary.count += damage_total.count
            damage_total.damage /= damage_total.count
            damage_total.critical_damage /= damage_total.count
            damage_total.expected_damage /= damage_total.count
            damage_total.critical_strike /= damage_total.count
            for attr, residual_damage in damage_total.gradients.items():
                total.gradients[attr] += residual_damage
                damage_total.gradients[attr] /= damage_total.count
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
