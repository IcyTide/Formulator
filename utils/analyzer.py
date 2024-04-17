from dataclasses import dataclass
from collections import defaultdict
from typing import Dict

from base.attribute import Attribute
from base.skill import Skill
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
        if buff.gain_attributes or skill_id in buff.gain_skills:
            buffs.append(buff)

    return tuple(sorted(buffs, key=lambda x: x.buff_id))


def add_buffs(current_buffs, snapshot_buffs, attribute: Attribute, skill: Skill):
    if not snapshot_buffs:
        for buff in current_buffs:
            buff.add_all(attribute, skill)
    else:
        for buff in snapshot_buffs:
            buff.add_snapshot(attribute, skill)
        for buff in current_buffs:
            buff.add_current(attribute, skill)


def sub_buffs(current_buffs, snapshot_buffs, attribute: Attribute, skill: Skill):
    if not snapshot_buffs:
        for buff in current_buffs:
            buff.sub_all(attribute, skill)
    else:
        for buff in snapshot_buffs:
            buff.sub_snapshot(attribute, skill)
        for buff in current_buffs:
            buff.sub_current(attribute, skill)


def concat_buffs(current_buffs, snapshot_buffs):
    buffs = ",".join(buff.display_name for buff in current_buffs)
    if snapshot_buffs and current_buffs != snapshot_buffs:
        buffs += f"({','.join(buff.display_name for buff in snapshot_buffs)})"
    if not buffs:
        buffs = "~"
    return buffs


def analyze_details(record, duration: int, attribute: Attribute, school: School):
    total = Detail()
    details = {}
    summary = {}
    duration *= 1000

    for skill, status in record.items():
        skill_id, skill_level, skill_stack = skill
        skill: Skill = school.skills[skill_id]
        if not skill.activate:
            continue
        skill.skill_level, skill.skill_stack, skill_name = skill_level, skill_stack, skill.skill_name

        skill_detail = details[skill.display_name] = {}
        if not (skill_summary := summary.get(skill_name)):
            skill_summary = summary[skill_name] = Detail()
        skill_total = skill_detail[""] = Detail()
        for (current_status, snapshot_status), timeline in status.items():
            if not (timeline := [t for t in timeline if t[0] < duration]):
                continue
            critical_timeline = [t for t in timeline if t[1]]

            current_buffs = filter_status(current_status, school, skill_id)
            snapshot_buffs = filter_status(snapshot_status, school, skill_id)
            buffs = concat_buffs(current_buffs, snapshot_buffs)

            if not (detail := skill_detail.get(buffs)):
                add_buffs(current_buffs, snapshot_buffs, attribute, skill)
                detail = skill_detail[buffs] = Detail(*skill(attribute))
                detail.gradients = analyze_gradients(skill, attribute)
                sub_buffs(current_buffs, snapshot_buffs, attribute, skill)

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

        total.expected_damage += skill_total.expected_damage
        total.count += skill_total.count
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

    return total, summary, details


def analyze_gradients(skill, attribute):
    results = {}
    for attr, value in attribute.grad_attrs.items():
        origin_value = getattr(attribute, attr)
        setattr(attribute, attr, origin_value + value)
        _, _, results[attr], _ = skill(attribute)
        setattr(attribute, attr, origin_value)
    return results
