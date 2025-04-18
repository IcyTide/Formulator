from collections import defaultdict

from copy import copy
from dataclasses import dataclass
from functools import cached_property
from typing import Dict, Union, List

from assets.constant import MOBILE_RECIPE_ID_START
from base.attribute import Attribute
from base.buff import Buff
from base.constant import FRAME_PER_SECOND
from base.dot import Dot
from base.gain import Gain
from base.skill import Skill, PetSkill
from kungfus import Kungfu


@dataclass
class Detail:
    hit_damage: int = 0
    critical_damage: int = 0
    critical_strike: float = 0.
    expected_damage: float = 0.

    expected_count: float = 0
    timeline: List[tuple] = None
    gradients: Dict[str, float] = None

    EPSILON: float = 5e-2

    def __post_init__(self):
        if not self.timeline:
            self.timeline = []
        if not self.gradients:
            self.gradients = defaultdict(float)

    @property
    def actual_count(self):
        return len(self.timeline)

    @cached_property
    def expected_critical_count(self):
        return self.critical_strike * self.expected_count

    @cached_property
    def actual_critical_count(self):
        return len([t for t in self.timeline if t[1]])

    @cached_property
    def actual_critical_strike(self):
        return self.actual_critical_count / self.actual_count

    @cached_property
    def total_expected_damage(self):
        return self.expected_damage * self.expected_count

    @cached_property
    def total_actual_damage(self):
        return sum([t[-1] for t in self.timeline if t[-1]])

    @cached_property
    def actual_damage(self):
        return self.total_actual_damage / self.actual_count

    @property
    def anomaly_detail(self):
        anomaly_timeline = []
        for frame, critical, damage in self.timeline:
            if not self.hit_damage or not damage:
                anomaly_timeline.append((frame, critical, damage))
            elif critical and abs(damage - self.critical_damage) / self.critical_damage > self.EPSILON:
                anomaly_timeline.append((frame, critical, damage))
            elif not critical and abs(damage - self.hit_damage) / self.hit_damage > self.EPSILON:
                anomaly_timeline.append((frame, critical, damage))
        if anomaly_timeline:
            return Detail(
                self.hit_damage, self.critical_damage, self.critical_strike, self.expected_damage,
                timeline=anomaly_timeline
            )
        else:
            return None


class BaseAnalyzer:
    kungfu: Kungfu
    attribute: Attribute


class BuffAnalyzer(BaseAnalyzer):
    DOT_SNAPSHOT_ATTRS = [
        "attack_power", "critical_strike", "critical_power", "surplus", "strain", "damage_addition", "pve_addition"
    ]
    PET_SNAPSHOT_ATTRS = [
        "attack_power", "critical_power", "overcome", "surplus", "strain"
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
        # elif isinstance(damage, NpcSkill):
        #     display_current_buffs, display_snapshot_buffs = self.add_buffs_all(current_buffs, snapshot_buffs, damage)
        elif isinstance(damage, PetSkill):
            display_current_buffs, display_snapshot_buffs = self.add_buffs_pet(current_buffs, snapshot_buffs, damage)
        else:
            display_current_buffs, display_snapshot_buffs = self.add_buffs_all(current_buffs, snapshot_buffs, damage)

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
            self.sub_buff_attributes_all(buff)
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
        # elif isinstance(damage, NpcSkill):
        #     self.sub_buffs_all(current_buffs, snapshot_buffs, damage)
        elif isinstance(damage, PetSkill):
            self.sub_buffs_pet(current_buffs, snapshot_buffs, damage)
        else:
            self.sub_buffs_all(current_buffs, snapshot_buffs, damage)
        self.sub_buffs_target(target_buffs)

    @staticmethod
    def concat_buffs(current_buffs, snapshot_buffs, target_buffs):
        buffs = [
            ",".join(buff.display_name for buff in sorted(current_buffs)),
            ",".join(buff.display_name for buff in sorted(snapshot_buffs)),
            ",".join(buff.display_name for buff in sorted(target_buffs))
        ]
        buffs = "|".join(buffs)
        return buffs


class SkillAnalyzer(BaseAnalyzer):

    def split_damage(self, damage_tuple):
        damage_tuple, dot_skill_tuple, consume_skill_tuple = damage_tuple
        if dot_skill_tuple:
            dot_id, dot_level, dot_tick = damage_tuple
            damage, damage.buff_level = self.kungfu.dots[dot_id], dot_level
            dot_skill_id, dot_skill_level, dot_stack = dot_skill_tuple
            dot_skill, dot_skill.skill_level = self.kungfu.skills[dot_skill_id], dot_skill_level
            damage.dot_skill, damage.dot_stack, damage.dot_tick = dot_skill, dot_stack, dot_tick
            if consume_skill_tuple:
                consume_skill_id, consume_skill_level, consume_tick = consume_skill_tuple
                consume_skill, consume_skill.skill_level = self.kungfu.skills[consume_skill_id], consume_skill_level
                damage.consume_skill, damage.consume_tick = consume_skill, consume_tick
            else:
                damage.consume_skill, damage.consume_tick = None, 1
            damage_name = damage.buff_name
        else:
            skill_id, skill_level = damage_tuple
            damage, damage.skill_level = self.kungfu.skills[skill_id], skill_level
            damage_name = damage.skill_name
        return damage, damage_name


class Analyzer(BuffAnalyzer, SkillAnalyzer):
    def __init__(self, kungfu: Kungfu, target_level: int, start_time: float, end_time: float, record):
        self.kungfu = kungfu
        self.attribute = kungfu.attribute()
        self.attribute.target.level = target_level
        self.gains = []
        self.recipes = []

        self.add_recipes(self.attribute.recipes)

        self.start_time = start_time
        self.start_frame = int(start_time * FRAME_PER_SECOND)
        self.end_time = end_time
        self.end_frame = int(end_time * FRAME_PER_SECOND)
        self.record = record
        self.total = Detail()
        self.details = defaultdict(dict)
        self.summary = defaultdict(Detail)

    def add_attrs(self, attrs):
        for attr, value in attrs.items():
            self.attribute[attr] += value

    def sub_attrs(self, attrs):
        for attr, value in attrs.items():
            self.attribute[attr] -= value

    def add_gains(self, gains):
        not_support_gains = []
        for gain in gains:
            if not isinstance(gain, Gain):
                if gain not in self.kungfu.gains:
                    not_support_gains.append(str(gain))
                    continue
                gain = self.kungfu.gains[gain]

            gain.add(self.attribute, self.kungfu.buffs, self.kungfu.dots, self.kungfu.skills)
            self.add_recipes(gain.recipes)
            self.gains.append(gain)
        return not_support_gains

    def sub_gains(self):
        for gain in self.gains:
            gain.sub(self.attribute, self.kungfu.buffs, self.kungfu.dots, self.kungfu.skills)

    def add_recipes(self, recipes):
        not_support_recipes = []
        for recipe_key in recipes:
            if recipe_key not in self.kungfu.recipes:
                if recipe_key[0] < MOBILE_RECIPE_ID_START:
                    not_support_recipes.append(str(recipe_key))
                continue
            recipe = self.kungfu.recipes[recipe_key]
            recipe.add(self.attribute, self.kungfu.buffs, self.kungfu.dots, self.kungfu.skills)
            self.recipes.append(recipe)
        return not_support_recipes

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

    def cal_detail(self, damage, status_tuple):
        damage_detail = self.details[damage.display_name]
        if "" not in damage_detail:
            damage_detail[""] = Detail()
        buffs_tuple = [self.filter_status(status) for status in status_tuple]

        display_buffs = self.add_buffs(*buffs_tuple, damage)
        buffs = self.concat_buffs(*display_buffs)
        if buffs in damage_detail:
            detail = damage_detail[buffs]
        else:
            detail = damage_detail[buffs] = Detail(*damage(self.attribute))
            detail.gradients = self.cal_delta(damage)
        self.sub_buffs(*buffs_tuple, damage)
        return detail

    def analyze_timeline(self, damage, detail, timeline):
        damage_total = self.details[damage.display_name][""]
        if isinstance(damage, Skill) and damage.prob:
            count = 0
            actual_timeline = []
            for item in timeline:
                if item[-1]:
                    actual_timeline.append(item)
                else:
                    count += damage.hit_prob + damage.critical_prob * detail.critical_strike
            detail.timeline += actual_timeline
            damage_total.timeline += actual_timeline
        else:
            count = len(timeline)
            detail.timeline += timeline
            damage_total.timeline += timeline
        return count

    def analyze_detail(self, damage, detail, count):
        damage_total = self.details[damage.display_name][""]

        detail.expected_count += count
        damage_total.expected_count += count
        damage_total.hit_damage += detail.hit_damage * count
        damage_total.critical_damage += detail.critical_damage * count
        damage_total.critical_strike += detail.critical_strike * count
        damage_total.expected_damage += detail.expected_damage * count
        for attr, residual_damage in detail.gradients.items():
            self.total.gradients[attr] += residual_damage * count

    def analyze_total(self, damage, damage_name):
        if not self.details[damage.display_name]:
            self.details.pop(damage.display_name)
            return

        damage_total = self.details[damage.display_name][""]
        if damage_total.expected_count:
            self.total.expected_damage += damage_total.expected_damage
            self.summary[damage_name].critical_strike += damage_total.critical_strike
            self.summary[damage_name].expected_damage += damage_total.expected_damage
            self.summary[damage_name].expected_count += damage_total.expected_count
            self.summary[damage_name].timeline += damage_total.timeline
            damage_total.hit_damage /= damage_total.expected_count
            damage_total.critical_damage /= damage_total.expected_count
            damage_total.expected_damage /= damage_total.expected_count
            damage_total.critical_strike /= damage_total.expected_count
        else:
            self.details.pop(damage.display_name)

    def sort_details(self):
        for detail in self.summary.values():
            detail.critical_strike /= detail.expected_count
        self.summary = {
            damage: detail
            for damage, detail in
            sorted(self.summary.items(), key=lambda x: x[1].expected_damage, reverse=True)
        }
        self.details = {
            damage: {
                buff: detail
                for buff, detail in
                sorted(details.items(), key=lambda x: x[1].total_expected_damage, reverse=True)
            }
            for damage, details in
            sorted(self.details.items(), key=lambda x: x[1][""].total_expected_damage, reverse=True)
        }

    def analyze_details(self):

        for damage, status in self.record.items():
            damage, damage_name = self.split_damage(damage)
            if not damage.activate:
                continue

            for status_tuple, timeline in status.items():
                if not (timeline := [t for t in timeline if self.start_frame <= t[0] <= self.end_frame]):
                    continue

                detail = self.cal_detail(damage, status_tuple)
                count = self.analyze_timeline(damage, detail, timeline)
                self.analyze_detail(damage, detail, count)

            self.analyze_total(damage, damage_name)

        self.sort_details()
