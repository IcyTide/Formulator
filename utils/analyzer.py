from base.attribute import Attribute
from base.skill import Skill
from utils.parser import School


def filter_status(status, school: School, skill_id):
    buffs = []
    for buff_id, buff_level, buff_stack in status:
        buff = school.buffs[buff_id]
        buff.buff_level, buff.buff_stack = buff_level, buff_stack
        if buff.gain_attributes or skill_id in buff.gain_skills:
            buffs.append(buff)

    return tuple(buffs)


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


def analyze_details(record, duration: int, attribute: Attribute, school: School):
    details = {}
    total_damage = 0
    total_gradients = {attr: 0. for attr in attribute.grad_attrs}
    duration *= 1000

    for skill, status in record.items():
        skill_id, skill_level, skill_stack = skill
        skill: Skill = school.skills[skill_id]
        skill.skill_level, skill.skill_stack = skill_level, skill_stack

        skill_detail = {}
        details[skill.display_name] = skill_detail
        for (current_status, snapshot_status), timeline in status.items():
            hit_timeline, critical_timeline = [], []
            for timestamp, critical in timeline:
                if critical:
                    critical_timeline.append(timestamp)
                else:
                    hit_timeline.append(timestamp)
            timeline = [t for t in timeline if t[0] < duration]
            if not timeline:
                continue

            current_buffs = filter_status(current_status, school, skill_id)
            snapshot_buffs = filter_status(snapshot_status, school, skill_id)
            add_buffs(current_buffs, snapshot_buffs, attribute, skill)

            damage, expected_critical_strike, critical_damage, expected_damage = skill(attribute)
            gradients = analyze_gradients(skill, attribute)

            sub_buffs(current_buffs, snapshot_buffs, attribute, skill)

            total_damage += expected_damage * len(timeline)
            for attr, residual_damage in gradients.items():
                total_gradients[attr] += residual_damage * len(timeline)

            buffs = ",".join(buff.display_name for buff in current_buffs)
            if snapshot_buffs and current_buffs != snapshot_buffs:
                buffs += f"({','.join(buff.display_name for buff in snapshot_buffs)})"

            if not buffs:
                buffs = "~"
            skill_detail[buffs] = dict(
                damage=damage,
                critical_damage=critical_damage,
                expected_damage=expected_damage,
                critical_strike=len(critical_timeline) / (len(critical_timeline) + len(hit_timeline)),
                expected_critical_strike=expected_critical_strike,
                # "timeline": [round(t / 1000, 3) for t in timeline],
                count=len(timeline),
                gradients=gradients
            )

    for attr, residual_damage in total_gradients.items():
        total_gradients[attr] = round(residual_damage / total_damage * 100, 4)

    summary = analyze_summary(details)
    return total_damage, total_gradients, details, summary


def analyze_summary(details):
    summary = {}
    for skill, skill_detail in details.items():
        skill = skill.split("/")[0]
        if skill not in summary:
            summary[skill] = {"count": 0, "critical": 0, "damage": 0}
        for buff, detail in skill_detail.items():
            summary[skill]["count"] += detail['count']
            summary[skill]["critical"] += detail['count'] * detail['expected_critical_strike']
            summary[skill]["damage"] += detail['count'] * detail['expected_damage']

    return summary


def analyze_gradients(skill, attribute):
    results = {}
    for attr, value in attribute.grad_attrs.items():
        origin_value = getattr(attribute, attr)
        setattr(attribute, attr, origin_value + value)
        _, _, _, results[attr] = skill(attribute)
        setattr(attribute, attr, origin_value)
    return results
