from dataclasses import dataclass
from typing import Dict, Union

from assets.recipes import RECIPES
from base.attribute import Attribute
from base.buff import Buff
from base.dot import Dot
from base.skill import Skill


@dataclass
class Recipe:
    recipe_id: int
    recipe_level: int
    recipe_name: str = ""

    def __post_init__(self):
        if not self.recipe_name:
            self.recipe_name = type(self).__name__

    def set_asset(self, attrs):
        for attr, value in RECIPES.get(self.recipe_id, {}).get(self.recipe_level, {}).items():
            setattr(self, attr, value)
        for attr, value in attrs.items():
            setattr(self, attr, value)

    def add_attribute(self, attribute: Attribute):
        pass

    def add_buffs(self, buffs: Dict[int, Buff]):
        pass

    def add_dots(self, dots: Dict[int, Dot]):
        pass

    def add_skills(self, skills: Dict[int, Skill]):
        pass

    def add(self, attribute: Attribute, buffs: Dict[int, Buff], dots: Dict[int, Dot], skills: Dict[int, Skill]):
        self.add_attribute(attribute)
        self.add_buffs(buffs)
        self.add_dots(dots)
        return self.add_skills(skills)

    def sub_attribute(self, attribute: Attribute):
        pass

    def sub_skills(self, skills: Dict[int, Skill]):
        pass

    def sub_buffs(self, buffs: Dict[int, Buff]):
        pass

    def sub_dots(self, dots: Dict[int, Dot]):
        pass

    def sub(self, attribute: Attribute, buffs: Dict[int, Buff], dots: Dict[int, Dot], skills: Dict[int, Skill]):
        self.sub_attribute(attribute)
        self.sub_buffs(buffs)
        self.sub_dots(dots)
        self.sub_skills(skills)


class SkillRecipe(Recipe):
    skill_id = None
    recipe_type = None
    recipe_mask = 0

    clone_id = None

    damage_addition: int = 0
    prepare_frame: int = 0
    value: Union[int, float, tuple] = 0

    def check_skill(self, skill: Skill):
        if skill.skill_id == self.skill_id or skill.skill_id == self.clone_id:
            return True
        if skill.recipe_type == self.recipe_type or skill.recipe_type == self.clone_id:
            return True
        if skill.recipe_mask & self.recipe_mask:
            return True
        return False

    def add_skill(self, skill: Skill):
        skill.damage_addition_extra += self.damage_addition
        skill.prepare_frame_extra += self.prepare_frame

    def add_skills(self, skills: Dict[int, Skill]):
        return_tag = False
        for skill in skills.values():
            if self.check_skill(skill):
                self.add_skill(skill)
                return_tag = True
        return return_tag

    def sub_skill(self, skill: Skill):
        skill.damage_addition_extra -= self.damage_addition
        skill.prepare_frame_extra -= self.prepare_frame

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if self.check_skill(skill):
                self.sub_skill(skill)


class DotRecipe(Recipe):
    buff_id: int = None
    clone_id: int = None

    interval: int = 0
    tick: int = 0

    def check_dot(self, dot: Dot):
        if dot.buff_id == self.buff_id or dot.buff_id == self.clone_id:
            return True
        return False

    def add_dot(self, dot: Dot):
        dot.interval_extra += self.interval
        dot.tick_extra += self.interval

    def add_dots(self, dots: Dict[int, Dot]):
        for dot in dots.values():
            if self.check_dot(dot):
                self.add_dot(dot)

    def sub_dot(self, dot: Dot):
        dot.interval_extra -= self.interval
        dot.tick_extra -= self.interval

    def sub_dots(self, dots: Dict[int, Dot]):
        for dot in dots.values():
            if self.check_dot(dot):
                self.sub_dot(dot)
