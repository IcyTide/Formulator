from typing import Dict, Union

from base.attribute import Attribute
from base.buff import Buff
from base.skill import Skill


class Gain:
    skill_id = None
    skill_recipe = None
    buff_id = None
    buff_recipe = None
    value = None

    def __init__(
            self, value: Union[int, float, tuple] = None,
            skill_id: int = None, skill_recipe: int = None,
            buff_id: int = None, buff_recipe: int = None,
            name: str = None,
    ):
        if name:
            self.gain_name = name
        else:
            self.gain_name = type(self).__name__
        if value:
            self.value = value
        if skill_id:
            self.skill_id = skill_id
        if skill_recipe:
            self.skill_recipe = skill_recipe

    def add_attribute(self, attribute: Attribute):
        pass

    def add_skill(self, skill: Skill):
        pass

    def add_skills(self, skills: Dict[int, Skill]):
        return_tag = False
        if not self.skill_id and not self.skill_recipe:
            return return_tag

        for skill_id, skill in skills.items():
            if skill_id == self.skill_id or skill.recipe_type == self.skill_recipe:
                if self.add_skill(skill):
                    return_tag = True

        return return_tag

    def add_buffs(self, buffs: Dict[int, Buff]):
        pass

    def add(self, attribute: Attribute, skills: Dict[int, Skill], buffs: Dict[int, Buff]):
        return_tags = (self.add_attribute(attribute), self.add_skills(skills), self.add_buffs(buffs))
        return any(return_tags)

    def sub_attribute(self, attribute: Attribute):
        pass

    def sub_skill(self, skill: Skill):
        pass

    def sub_skills(self, skills: Dict[int, Skill]):
        if not self.skill_id and not self.skill_recipe:
            return
        for skill_id, skill in skills.items():
            if skill_id == self.skill_id or skill.recipe_type == self.skill_recipe:
                self.sub_skill(skill)

    def sub_buffs(self, buffs: Dict[int, Buff]):
        pass

    def sub(self, attribute: Attribute, skills: Dict[int, Skill], buffs: Dict[int, Buff]):
        self.sub_attribute(attribute)
        self.sub_skills(skills)
        self.sub_buffs(buffs)
