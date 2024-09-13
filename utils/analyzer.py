from collections import defaultdict
from copy import copy
from dataclasses import dataclass
from functools import cached_property
from typing import Dict, Union, List

from base.attribute import Attribute
from base.buff import Buff
from base.constant import FRAME_PER_SECOND
from base.dot import Dot
from base.gain import Gain
from base.skill import Skill, NpcSkill, PetSkill
from kungfus import Kungfu


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


class BaseAnalyzer:
    kungfu: Kungfu
    attribute: Attribute


class BuffAnalyzer(BaseAnalyzer):
    DOT_SNAPSHOT_ATTRS = [
        "attack_power", "critical_strike", "critical_power", "surplus", "strain", "damage_addition", "pve_addition"
    ]
    PET_SNAPSHOT_ATTRS = [
        "attack_power", "critical_power", "overcome", "surplus", "strain", "damage_addition", "pve_addition"
    ]

    def filter_status(self, status):
        buffs = []
        for buff_id, buff_level, buff_stack in status:
            buff, buff.buff_level, buff.buff_stack = self.kungfu.buffs[buff_id], buff_level, buff_stack
            if not buff.activate:
                continue
            buffs.append(copy(buff))

        return sorted(buffs, key=lambda x: abs(x.buff_id))

    def add_buff_attributes_all(self, buff: Buff):
        return_tag = False
        for attr, value in buff.attributes.items():
            self.attribute[attr] += value
            return_tag = True
        return return_tag

    def add_buff_attributes_dot(self, buff: Buff, snapshot: bool):
        return_tag = False
        for attr, value in buff.attributes.items():
            if snapshot and any(snapshot_attr in attr for snapshot_attr in self.DOT_SNAPSHOT_ATTRS):
                self.attribute[attr] += value
                return_tag = True
            if not snapshot and all(snapshot_attr not in attr for snapshot_attr in self.DOT_SNAPSHOT_ATTRS):
                self.attribute[attr] += value
                return_tag = True
        return return_tag

    def add_buff_attributes_pet(self, buff: Buff):
        return_tag = False
        for attr, value in buff.attributes.items():
            if any(snapshot_attr in attr for snapshot_attr in self.PET_SNAPSHOT_ATTRS):
                self.attribute[attr] += value
                return_tag = True
        return return_tag

    def add_buff_attributes_target(self, buff: Buff):
        return_tag = False
        for attr, value in buff.attributes.items():
            self.attribute.target[attr] += value
            return_tag = True
        return return_tag

    def sub_buff_attributes_all(self, buff: Buff):
        for attr, value in buff.attributes.items():
            self.attribute[attr] -= value

    def sub_buff_attributes_dot(self, buff: Buff, snapshot: bool):
        for attr, value in buff.attributes.items():
            if snapshot and any(snapshot_attr in attr for snapshot_attr in self.DOT_SNAPSHOT_ATTRS):
                self.attribute[attr] -= value
            if not snapshot and all(snapshot_attr not in attr for snapshot_attr in self.DOT_SNAPSHOT_ATTRS):
                self.attribute[attr] -= value

    def sub_buff_attributes_pet(self, buff: Buff):
        for attr, value in buff.attributes.items():
            if any(snapshot_attr in attr for snapshot_attr in self.PET_SNAPSHOT_ATTRS):
                self.attribute[attr] -= value

    def sub_buff_attributes_target(self, buff: Buff):
        for attr, value in buff.attributes.items():
            self.attribute.target[attr] -= value

    def add_buff_recipes(self, skill: Skill, buff: Buff) -> bool:
        return_tag = False
        for recipe_key in buff.recipes.items():
            if self.kungfu.recipes[recipe_key].add(self.attribute, {}, {}, {skill.skill_id: skill}):
                return_tag = True
        return return_tag

    def sub_buff_recipes(self, skill: Skill, buff: Buff):
        for recipe_key in buff.recipes.items():
            self.kungfu.recipes[recipe_key].sub(self.attribute, {}, {}, {skill.skill_id: skill})

    def add_buffs_all(self, current_buffs: List[Buff], snapshot_buffs: List[Buff], damage: Skill):
        display_current_buffs, display_snapshot_buffs = [], []
        for buff in current_buffs:
            if any((self.add_buff_attributes_all(buff), self.add_buff_recipes(damage, buff))):
                display_current_buffs.append(buff)
        for buff in snapshot_buffs:
            if any((self.add_buff_attributes_all(buff), self.add_buff_recipes(damage, buff))):
                display_snapshot_buffs.append(buff)
        return display_current_buffs, display_snapshot_buffs

    def add_buffs_dot(self, current_buffs: List[Buff], snapshot_buffs: List[Buff], damage: Dot):
        display_current_buffs, display_snapshot_buffs = [], []
        for buff in current_buffs:
            if self.add_buff_attributes_dot(buff, False):
                display_current_buffs.append(buff)
        for buff in snapshot_buffs:
            if any((self.add_buff_attributes_dot(buff, True), self.add_buff_recipes(damage.dot_skill, buff))):
                display_snapshot_buffs.append(buff)
        return display_current_buffs, display_snapshot_buffs

    def add_buffs_pet(self, current_buffs: List[Buff], snapshot_buffs: List[Buff], damage: Skill):
        display_current_buffs, display_snapshot_buffs = [], []
        for buff in current_buffs:
            if any((self.add_buff_attributes_all(buff), self.add_buff_recipes(damage, buff))):
                display_current_buffs.append(buff)
        for buff in snapshot_buffs:
            if any((self.add_buff_attributes_pet(buff), self.add_buff_recipes(damage, buff))):
                display_snapshot_buffs.append(buff)
        return display_current_buffs, display_snapshot_buffs

    def add_buffs_target(self, target_buffs: List[Buff]):
        display_target_buffs = []
        for buff in target_buffs:
            if self.add_buff_attributes_target(buff):
                display_target_buffs.append(buff)
        return display_target_buffs

    def add_buffs(self, current_buffs, snapshot_buffs, target_buffs, damage: Union[Dot, Skill]):
        if isinstance(damage, Dot):
            display_current_buffs, display_snapshot_buffs = self.add_buffs_dot(current_buffs, snapshot_buffs, damage)
        elif isinstance(damage, NpcSkill):
            display_current_buffs, display_snapshot_buffs = self.add_buffs_all(current_buffs, snapshot_buffs, damage)
        elif isinstance(damage, PetSkill):
            display_current_buffs, display_snapshot_buffs = self.add_buffs_pet(current_buffs, snapshot_buffs, damage)
        else:
            display_current_buffs, display_snapshot_buffs = self.add_buffs_all(current_buffs, [], damage)

        display_target_buffs = self.add_buffs_target(target_buffs)
        return display_current_buffs, display_snapshot_buffs, display_target_buffs

    def sub_buffs_all(self, current_buffs: List[Buff], snapshot_buffs: List[Buff], damage: Skill):
        for buff in current_buffs:
            self.sub_buff_attributes_all(buff)
            self.sub_buff_recipes(damage, buff)
        for buff in snapshot_buffs:
            self.sub_buff_attributes_all(buff)
            self.sub_buff_recipes(damage, buff)

    def sub_buffs_dot(self, current_buffs: List[Buff], snapshot_buffs: List[Buff], damage: Dot):
        for buff in current_buffs:
            self.sub_buff_attributes_dot(buff, False)
        for buff in snapshot_buffs:
            self.sub_buff_attributes_dot(buff, True)
            self.sub_buff_recipes(damage.dot_skill, buff)

    def sub_buffs_pet(self, current_buffs: List[Buff], snapshot_buffs: List[Buff], damage: Skill):
        for buff in current_buffs:
            self.sub_buff_attributes_pet(buff)
            self.sub_buff_recipes(damage, buff)
        for buff in snapshot_buffs:
            self.sub_buff_attributes_pet(buff)
            self.sub_buff_recipes(damage, buff)

    def sub_buffs_target(self, target_buffs: List[Buff]):
        for buff in target_buffs:
            self.sub_buff_attributes_target(buff)

    def sub_buffs(self, current_buffs, snapshot_buffs, target_buffs, damage: Union[Dot, Skill]):
        if isinstance(damage, Dot):
            self.sub_buffs_dot(current_buffs, snapshot_buffs, damage)
        elif isinstance(damage, NpcSkill):
            self.sub_buffs_all(current_buffs, snapshot_buffs, damage)
        elif isinstance(damage, PetSkill):
            self.sub_buffs_pet(current_buffs, snapshot_buffs, damage)
        else:
            self.sub_buffs_all(current_buffs, [], damage)
        self.sub_buffs_target(target_buffs)

    @staticmethod
    def concat_buffs(current_buffs, snapshot_buffs, target_buffs):
        buffs = []
        if current_buffs:
            buffs.append(",".join(buff.display_name for buff in sorted(current_buffs)))
        if snapshot_buffs:
            buffs.append(",".join(buff.display_name for buff in sorted(snapshot_buffs)))
        if target_buffs:
            buffs.append(",".join(buff.display_name for buff in sorted(target_buffs)))

        if buffs:
            buffs = "|".join(buffs)
        else:
            buffs = "~"
        return buffs


class SkillAnalyzer(BaseAnalyzer):

    def split_damage(self, damage_tuple):
        damage_tuple, dot_skill_tuple, consume_skill_tuple = damage_tuple
        if dot_skill_tuple:
            dot_id, dot_level = damage_tuple
            damage, damage.buff_level = self.kungfu.dots[dot_id], dot_level
            dot_skill_id, dot_skill_level, dot_stack = dot_skill_tuple
            dot_skill, dot_skill.skill_level = self.kungfu.skills[dot_skill_id], dot_skill_level
            damage.dot_skill, damage.dot_stack = dot_skill, dot_stack
            if consume_skill_tuple:
                consume_skill_id, consume_skill_level, consume_tick = consume_skill_tuple
                consume_skill, consume_skill.skill_level = self.kungfu.skills[consume_skill_id], consume_skill_level
                damage.consume_skill, damage.consume_tick = consume_skill, consume_tick
            else:
                damage.consume_skill, damage.consume_tick = None, 1
            damage_name = damage.buff_name
        else:
            skill_id, skill_level = damage_tuple
            damage, damage.skill_level, = self.kungfu.skills[skill_id], skill_level
            damage_name = damage.skill_name
        return damage, damage_name


class Analyzer(BuffAnalyzer, SkillAnalyzer):
    def __init__(self, kungfu: Kungfu, target_level):
        self.kungfu = kungfu
        self.attribute = kungfu.attribute(kungfu.platform)
        self.attribute.target.level = target_level
        self.gains = []
        self.recipes = []

        self.add_recipes(self.attribute.recipes)

    def add_attrs(self, attrs):
        for attr, value in attrs.items():
            self.attribute[attr] += value

    def sub_attrs(self, attrs):
        for attr, value in attrs.items():
            self.attribute[attr] -= value

    def add_gains(self, gains):
        for gain in gains:
            if not isinstance(gain, Gain):
                gain = self.kungfu.gains[gain]
            gain.add(self.attribute, self.kungfu.buffs, self.kungfu.dots, self.kungfu.skills)
            self.add_recipes(gain.recipes)
            self.gains.append(gain)

    def sub_gains(self):
        for gain in self.gains:
            gain.sub(self.attribute, self.kungfu.buffs, self.kungfu.dots, self.kungfu.skills)

    def add_recipes(self, recipes):
        for recipe_key in recipes:
            recipe = self.kungfu.recipes[recipe_key]
            recipe.add(self.attribute, self.kungfu.buffs, self.kungfu.dots, self.kungfu.skills)
            self.recipes.append(recipe)

    def sub_recipes(self):
        for recipe in self.recipes:
            recipe.sub(self.attribute, self.kungfu.buffs, self.kungfu.dots, self.kungfu.skills)

    def cal_delta(self, damage):
        results = {}
        for attr, value in self.attribute.grad_attrs.items():
            origin_value = getattr(self.attribute, attr)
            setattr(self.attribute, attr, origin_value + value)
            _, _, _, results[attr] = damage(self.attribute)
            setattr(self.attribute, attr, origin_value)
        return results

    def analyze_details(self, record, start_frame, end_frame):
        total = Detail()
        details = {}
        summary = defaultdict(Detail)
        start_frame = int(start_frame * FRAME_PER_SECOND)
        end_frame = int(end_frame * FRAME_PER_SECOND)

        for damage, status in record.items():
            damage, damage_name = self.split_damage(damage)
            if not damage.activate:
                continue
            damage_detail = details[damage.display_name] = {}
            damage_summary = summary[damage_name]
            damage_total = damage_detail[""] = Detail()
            for status_tuple, timeline in status.items():
                if not (timeline := [t for t in timeline if start_frame <= t[0] < end_frame]):
                    continue

                buffs_tuple = [self.filter_status(status) for status in status_tuple]

                display_buffs = self.add_buffs(*buffs_tuple, damage)
                buffs = self.concat_buffs(*display_buffs)
                if buffs in damage_detail:
                    detail = damage_detail[buffs]
                else:
                    detail = damage_detail[buffs] = Detail(*damage(self.attribute))
                    detail.gradients = self.cal_delta(damage)
                self.sub_buffs(*buffs_tuple, damage)

                detail.timeline += timeline
                damage_total.timeline += timeline

                damage_total.damage += detail.damage * len(timeline)
                damage_total.critical_damage += detail.critical_damage * len(timeline)
                damage_total.critical_strike += detail.critical_strike * len(timeline)
                damage_total.expected_damage += detail.expected_damage * len(timeline)
                for attr, residual_damage in detail.gradients.items():
                    total.gradients[attr] += residual_damage * len(timeline)

            if damage_total.timeline:
                total.expected_damage += damage_total.expected_damage
                damage_summary.critical_strike += damage_total.critical_strike
                damage_summary.expected_damage += damage_total.expected_damage
                damage_summary.timeline += damage_total.timeline
                damage_total.damage /= len(damage_total.timeline)
                damage_total.critical_damage /= len(damage_total.timeline)
                damage_total.expected_damage /= len(damage_total.timeline)
                damage_total.critical_strike /= len(damage_total.timeline)
            else:
                details.pop(damage.display_name)

        summary = {damage: detail for damage, detail in summary.items() if detail.count}
        return total, summary, details
