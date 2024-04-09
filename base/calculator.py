from base.attribute import Attribute
from qt.scripts.top import Parser, School


def refresh_status(existed_buffs, buffs, attribute: Attribute, school: School):
    for buff in [buff for buff in existed_buffs if buff not in buffs]:
        existed_buffs.remove(buff)
        buff_id, buff_level, buff_stack = buff
        buff = school.buffs[buff_id]
        buff.buff_level = buff_level
        for _ in range(buff_stack):
            attribute, school.skills = (attribute, school.skills) - buff

    for buff in [buff for buff in buffs if buff not in existed_buffs]:
        existed_buffs.append(buff)
        buff_id, buff_level, buff_stack = buff
        buff = school.buffs[buff_id]
        buff.buff_level = buff_level
        for _ in range(buff_stack):
            attribute, school.skills = (attribute, school.skills) + buff


def analyze_details(parser: Parser, attribute: Attribute):
    existed_buffs = []
    for start_time, record in parser.records.items():
        for skill, status in record.items():
            skill_id, skill_level = skill
            skill = parser.school.skills[skill_id]
            skill.skill_level = skill_level
            for buffs, timeline in status.items():
                refresh_status(existed_buffs, buffs, attribute, parser.school)

                damage, critical_damage, expected_damage = skill(attribute)

                status[buffs] = {
                    "damage": damage, "critical_damage": critical_damage, "expected_damage": expected_damage,
                    "timeline": [round(t / 1000, 2) for t in timeline],
                    "gradients": analyze_gradients(skill, attribute)
                }
        refresh_status(existed_buffs, [], attribute, parser.school)


def analyze_gradients(skill, attribute):
    results = {}
    for attr, value in attribute.grad_attrs.items():
        origin_value = getattr(attribute, attr)
        setattr(attribute, attr, origin_value + value)
        _, _, results[attr] = skill(attribute)
        setattr(attribute, attr, origin_value)
    return results
