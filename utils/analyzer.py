from base.attribute import Attribute
from qt.scripts.top import School


def refresh_status(existed_buffs, buffs, attribute: Attribute, school: School):
    for buff in [buff for buff in existed_buffs if buff not in buffs]:
        existed_buffs.remove(buff)
        buff_id, buff_level, buff_stack = buff
        buff = school.buffs[buff_id]
        buff.buff_level, buff.buff_stack = buff_level, buff_stack
        attribute = attribute - buff
        school.skills = school.skills - buff

    for buff in [buff for buff in buffs if buff not in existed_buffs]:
        existed_buffs.append(buff)
        buff_id, buff_level, buff_stack = buff
        buff = school.buffs[buff_id]
        buff.buff_level, buff.buff_stack = buff_level, buff_stack
        attribute = attribute + buff
        school.skills = school.skills + buff


def analyze_details(record, attribute: Attribute, school: School):
    details = {}
    total_damage = 0
    total_gradients = {attr: 0 for attr in attribute.grad_attrs}

    existed_buffs = []
    for skill, status in record.items():
        skill_id, skill_level = skill
        skill = school.skills[skill_id]
        skill.skill_level = skill_level

        skill_detail = {}
        details[skill.display_name] = skill_detail
        for buffs, timeline in status.items():
            refresh_status(existed_buffs, buffs, attribute, school)

            damage, critical_strike, critical_damage, expected_damage = skill(attribute)
            gradients = analyze_gradients(skill, attribute)

            total_damage += expected_damage * len(timeline)
            for attr, residual_damage in gradients.items():
                total_gradients[attr] += residual_damage * len(timeline)

            buffs = ";".join(school.buffs[buff_id].display_name for buff_id, _, _ in buffs)
            if not buffs:
                buffs = "~-~-~"
            skill_detail[buffs] = dict(
                damage=damage,
                critical_strike=critical_strike,
                critical_damage=critical_damage,
                expected_damage=expected_damage,
                # "timeline": [round(t / 1000, 3) for t in timeline],
                count=len(timeline),
                gradients=gradients
            )

    refresh_status(existed_buffs, [], attribute, school)

    for attr, residual_damage in total_gradients.items():
        total_gradients[attr] = round(residual_damage / total_damage * 100, 4)

    summary = analyze_summary(details)
    return total_damage, total_gradients, details, summary


def analyze_summary(details):
    summary = {}
    for skill, skill_detail in details.items():
        skill = skill.split("/")[0]
        if skill not in summary:
            summary[skill] = {"count": 0, "hit": 0, "critical": 0, "damage": 0}
        for buff, detail in skill_detail.items():
            summary[skill]["count"] += detail['count']
            summary[skill]["critical"] += detail['count'] * detail['critical_strike']
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
