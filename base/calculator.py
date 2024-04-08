from base.attribute import Attribute
from parse import Parser


def analyze_details(parser: Parser, attribute: Attribute):
    existed_buffs = []
    for skill, status in parser.summary.items():
        skill_id, skill_level = skill
        skill = parser.skills[skill_id]
        skill.skill_level = skill_level
        for buffs, count in status.items():
            for buff in [buff for buff in existed_buffs if buff not in buffs]:
                existed_buffs.remove(buff)
                buff_id, buff_level, buff_stack = buff
                buff = parser.buffs[buff_id]
                buff.buff_level = buff_level
                for _ in range(buff_stack):
                    attribute, parser.skills = (attribute, parser.skills) - buff

            for buff in [buff for buff in buffs if buff not in existed_buffs]:
                existed_buffs.append(buff)
                buff_id, buff_level, buff_stack = buff
                buff = parser.buffs[buff_id]
                buff.buff_level = buff_level
                for _ in range(buff_stack):
                    attribute, parser.skills = (attribute, parser.skills) + buff

            damage, critical_damage, expected_damage = skill(attribute)
            status[buffs] = {
                "damage": damage, "critical_damage": critical_damage, "expected_damage": expected_damage, "count": count
            }
