from typing import Dict, List, Tuple

from base.attribute import Attribute
from base.buff import Buff
from base.dot import Dot
from base.skill import Skill


class Gain:
    gain_name: str
    recipes: List[Tuple[int, int]] = []
    attributes: Dict[str, int] = {}
    dot_ids: List[int] = []
    buff_ids: List[int] = []
    skill_ids: List[int] = []
    skill_events: List[Tuple[int, int, float, float, int, int]] = []

    def __init__(
            self, name: str = None, recipes: List[Tuple[int, int]] = None, attributes: Dict[str, int] = None,
            buff_ids: List[int] = None, dot_ids: List[int] = None, skill_ids: List[int] = None,
            skill_events: List[Tuple[int, int, float, float, int, int]] = None
    ):
        if name:
            self.gain_name = name
        else:
            self.gain_name = type(self).__name__
        if recipes:
            self.recipes = recipes
        if attributes:
            self.attributes = attributes
        if buff_ids:
            self.buff_ids = buff_ids
        if dot_ids:
            self.dot_ids = dot_ids
        if skill_ids:
            self.skill_ids = skill_ids
        if skill_events:
            self.skill_events = skill_events

    def add_attribute(self, attribute: Attribute):
        for attr, value in self.attributes.items():
            attribute[attr] += value

    def add_buffs(self, buffs: Dict[int, Buff]):
        for buff_id in self.buff_ids:
            buffs[buff_id].activate = True

    def add_dots(self, dots: Dict[int, Dot]):
        for dot_id in self.dot_ids:
            dots[dot_id].activate = True

    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].activate = True
        for skill_id, skill_level, hit_prob, critical_prob, event_mask_1, event_mask_2 in self.skill_events:
            skills[skill_id].hit_prob, skills[skill_id].critical_prob = hit_prob, critical_prob
            for skill in skills.values():
                if skill.event_mask_1 & event_mask_1 or skill.event_mask_2 & event_mask_2:
                    skill.sub_skills.append((skill_id, skill_level))

    def add(self, attribute: Attribute, buffs: Dict[int, Buff], dots: Dict[int, Dot], skills: Dict[int, Skill]):
        self.add_attribute(attribute)
        self.add_buffs(buffs)
        self.add_dots(dots)
        self.add_skills(skills)

    def sub_attribute(self, attribute: Attribute):
        for attr, value in self.attributes.items():
            attribute[attr] -= value

    def sub_buffs(self, buffs: Dict[int, Buff]):
        for buff_id in self.buff_ids:
            buffs[buff_id].activate = False

    def sub_dots(self, dots: Dict[int, Dot]):
        for dot_id in self.dot_ids:
            dots[dot_id].activate = False

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in self.skill_ids:
            skills[skill_id].activate = False
        for skill_id, skill_level, _, _, event_mask_1, event_mask_2 in self.skill_events:
            skills[skill_id].hit_prob, skills[skill_id].critical_prob = 0, 0
            for skill in skills.values():
                if skill.event_mask_1 & event_mask_1 or skill.event_mask_2 & event_mask_2:
                    skill.sub_skills.remove((skill_id, skill_level))

    def sub(self, attribute: Attribute, buffs: Dict[int, Buff], dots: Dict[int, Dot], skills: Dict[int, Skill]):
        self.sub_attribute(attribute)
        self.sub_buffs(buffs)
        self.sub_dots(dots)
        self.sub_skills(skills)
