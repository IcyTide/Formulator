from dataclasses import dataclass
from collections import defaultdict
from typing import Dict

from base.attribute import Attribute
from base.constant import FRAME_PER_SECOND
from base.skill import Skill, DotDamage, PetDamage
from utils.parser import School


@dataclass
class Detail:
    damage: int = 0
    critical_damage: int = 0
    expected_damage: float = 0.
    critical_strike: float = 0.

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


def filter_status(status, school: School, skill_id):
    buffs = []
    for buff_id, buff_level, buff_stack in status:
        buff = school.buffs[buff_id]
        if not buff.activate:
            continue
        buff.buff_level, buff.buff_stack = buff_level, buff_stack
        if buff.gain_attributes:
            buffs.append(buff)
        elif skill_id in buff.gain_skills:
            buffs.append(buff)

    return tuple(sorted(buffs, key=lambda x: x.buff_id))


def add_buffs(current_buffs, snapshot_buffs, target_buffs, attribute: Attribute, skill: Skill):
    final_buffs = []
    if not snapshot_buffs:
        for buff in current_buffs:
            buff.add_all(attribute, skill)
            final_buffs.append(buff)
    elif isinstance(skill, DotDamage):
        for buff in snapshot_buffs:
            if buff.add_dot(attribute, skill, True):
                final_buffs.append(buff)
        for buff in current_buffs:
            if buff.add_dot(attribute, skill, False):
                final_buffs.append(buff)
    elif isinstance(skill, PetDamage):
        for buff in snapshot_buffs:
            buff.add_all(attribute, skill)
            final_buffs.append(buff)
    for buff in target_buffs:
        buff.add_all(attribute, skill)

    return final_buffs + list(target_buffs)


def sub_buffs(current_buffs, snapshot_buffs, target_buffs, attribute: Attribute, skill: Skill):
    if not snapshot_buffs:
        for buff in current_buffs:
            buff.sub_all(attribute, skill)
    elif isinstance(skill, DotDamage):
        for buff in snapshot_buffs:
            buff.sub_dot(attribute, skill, True)
        for buff in current_buffs:
            buff.sub_dot(attribute, skill, False)
    elif isinstance(skill, PetDamage):
        for buff in snapshot_buffs:
            buff.sub_all(attribute, skill)
    for buff in target_buffs:
        buff.sub_all(attribute, skill)


def concat_buffs(buffs):
    buffs = ",".join(buff.display_name for buff in buffs)
    if not buffs:
        buffs = "~"
    return buffs


def analyze_details(record, duration: int, attribute: Attribute, school: School):
    total = Detail()
    details = {}
    summary = {}
    duration *= FRAME_PER_SECOND

    for skill, status in record.items():
        skill_id, skill_level, skill_stack = skill
        skill: Skill = school.skills[skill_id]
        if not skill.activate:
            continue
        skill.skill_level, skill.skill_stack = skill_level, skill_stack
        skill_name = skill.skill_name

        skill_detail = details[skill.display_name] = {}
        if not (skill_summary := summary.get(skill_name)):
            skill_summary = summary[skill_name] = Detail()
        skill_total = skill_detail[""] = Detail()
        for (current_status, snapshot_status, target_status), timeline in status.items():
            if not (timeline := [t for t in timeline if t[0] < duration]):
                continue
            critical_timeline = [t for t in timeline if t[1]]

            current_buffs = filter_status(current_status, school, skill_id)
            snapshot_buffs = filter_status(snapshot_status, school, skill_id)
            target_buffs = filter_status(target_status, school, skill_id)

            buffs = add_buffs(current_buffs, snapshot_buffs, target_buffs, attribute, skill)
            buffs = concat_buffs(buffs)
            detail = skill_detail[buffs] = Detail(*skill(attribute))
            detail.gradients = analyze_gradients(skill, attribute)
            sub_buffs(current_buffs, snapshot_buffs, target_buffs, attribute, skill)

            detail.critical_count += len(critical_timeline)
            detail.count += len(timeline)
            skill_total.critical_count += len(critical_timeline)
            skill_total.count += len(timeline)

            skill_total.damage += detail.damage * len(timeline)
            skill_total.critical_damage += detail.critical_damage * len(timeline)
            skill_total.expected_damage += detail.expected_damage * len(timeline)
            skill_total.critical_strike += detail.critical_strike * len(timeline)
            for attr, residual_damage in detail.gradients.items():
                skill_total.gradients[attr] += residual_damage * len(timeline)

        if skill_total.count:
            total.expected_damage += skill_total.expected_damage
            skill_summary.expected_damage += skill_total.expected_damage
            skill_summary.critical_count += skill_total.critical_strike
            skill_summary.count += skill_total.count
            skill_total.damage /= skill_total.count
            skill_total.critical_damage /= skill_total.count
            skill_total.expected_damage /= skill_total.count
            skill_total.critical_strike /= skill_total.count
            for attr, residual_damage in skill_total.gradients.items():
                total.gradients[attr] += residual_damage
                skill_total.gradients[attr] /= skill_total.count
        else:
            details.pop(skill.display_name)

    summary = {skill: detail for skill, detail in summary.items() if detail.count}
    return total, summary, details


def analyze_gradients(skill, attribute):
    results = {}
    for attr, value in attribute.grad_attrs.items():
        origin_value = getattr(attribute, attr)
        setattr(attribute, attr, origin_value + value)
        _, _, results[attr], _ = skill(attribute)
        setattr(attribute, attr, origin_value)
    return results
