import pandas as pd

from base.attribute import Attribute
from base.skill import Skill, DotDamage, NpcDamage, PetDamage
from utils.parser import School, Parser, CALCULATE_COLUMNS

DAMAGE_COLUMNS = ["damage", "critical_damage", "critical_strike", "expected_damage"]


def filter_status(status, school: School):
    buffs = []
    for buff_id, buff_level, buff_stack in status:
        buff = school.buffs[buff_id]
        if buff.activate:
            buffs.append(buff)

    return buffs


def add_buffs(current_buffs, snapshot_buffs, target_buffs, attribute: Attribute, skill: Skill):
    if not snapshot_buffs:
        for buff in current_buffs:
            buff.add_all(attribute, skill)
    elif isinstance(skill, DotDamage):
        for buff in snapshot_buffs:
            buff.add_dot(attribute, skill, True)
        for buff in current_buffs:
            buff.add_dot(attribute, skill, False)
    elif isinstance(skill, NpcDamage):
        for buff in snapshot_buffs:
            buff.add_all(attribute, skill)
    elif isinstance(skill, PetDamage):
        for buff in snapshot_buffs:
            buff.add_all(attribute, skill)
    for buff in target_buffs:
        buff.add_all(attribute, skill)


def sub_buffs(current_buffs, snapshot_buffs, target_buffs, attribute: Attribute, skill: Skill):
    if not snapshot_buffs:
        for buff in current_buffs:
            buff.sub_all(attribute, skill)
    elif isinstance(skill, DotDamage):
        for buff in snapshot_buffs:
            buff.sub_dot(attribute, skill, True)
        for buff in current_buffs:
            buff.sub_dot(attribute, skill, False)
    elif isinstance(skill, NpcDamage):
        for buff in snapshot_buffs:
            buff.sub_all(attribute, skill)
    elif isinstance(skill, PetDamage):
        for buff in snapshot_buffs:
            buff.sub_all(attribute, skill)
    for buff in target_buffs:
        buff.sub_all(attribute, skill)


def analyze_records(parser: Parser, duration: int, attribute: Attribute):
    records: pd.DataFrame = parser.current_records
    school = parser.current_school
    condition = (records.player_id == parser.current_player) & (records.time < duration)
    if parser.current_target:
        condition = condition & (records.target_id == parser.current_target)
    records = records[condition].copy()

    damage_columns = [(0 for _ in DAMAGE_COLUMNS)] * len(records)
    grad_attrs = list(attribute.grad_attrs)
    gradient_columns = [(0 for _ in grad_attrs)] * len(records)

    for row, indices in records.groupby(CALCULATE_COLUMNS).indices.items():
        skill_id, skill_level, skill_stack, current_status, target_status, snapshot_index = row
        skill: Skill = school.skills[skill_id]
        skill.skill_level, skill.skill_stack = skill_level, skill_stack

        current_buffs = filter_status(current_status, school)
        target_buffs = filter_status(target_status, school)
        if snapshot_index < 0:
            snapshot_buffs = tuple()
        else:
            snapshot_buffs = filter_status(records.loc[snapshot_index].current_status, school)

        add_buffs(current_buffs, snapshot_buffs, target_buffs, attribute, skill)
        damage_tuple = skill(attribute)
        gradient_tuple = analyze_gradients(skill, attribute)
        for index in indices:
            damage_columns[index] = damage_tuple
            gradient_columns[index] = gradient_tuple
        sub_buffs(current_buffs, snapshot_buffs, target_buffs, attribute, skill)

    records[DAMAGE_COLUMNS] = damage_columns
    records[grad_attrs] = gradient_columns

    return records


def analyze_gradients(skill, attribute):
    results = []
    for attr, value in attribute.grad_attrs.items():
        origin_value = getattr(attribute, attr)
        setattr(attribute, attr, origin_value + value)
        _, _, _, expected_damage = skill(attribute)
        results.append(expected_damage)
        setattr(attribute, attr, origin_value)
    return results
