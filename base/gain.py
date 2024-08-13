from typing import Dict, Union, List

from base.attribute import Attribute
from base.buff import Buff
from base.dot import Dot
from base.skill import Skill


class Gain:
    skill_id = None
    recipe_type = None
    recipe_mask = None
    value = None

    def __init__(
            self, value: Union[int, float, tuple] = None,
            skill_id: int = None, recipe_type: int = None, recipe_mask: int = 0,
            name: str = None,
    ):
        if name:
            self.gain_name = name
        else:
            self.gain_name = type(self).__name__
        if value is not None:
            self.value = value
        if skill_id:
            self.skill_id = skill_id
        if recipe_type:
            self.recipe_type = recipe_type
        self.recipe_mask = recipe_mask

    def check_skill(self, skill: Skill):
        if skill.skill_id == self.skill_id:
            return True
        if skill.recipe_type == self.recipe_type:
            return True
        if skill.recipe_mask & self.recipe_mask:
            return True
        return False

    def add_attribute(self, attribute: Attribute):
        pass

    def add_skill(self, skill: Skill):
        pass

    def add_skills(self, skills: Dict[int, Skill]):
        return_tag = False
        if not self.skill_id and not self.recipe_type and not self.recipe_mask:
            return return_tag

        for skill_id, skill in skills.items():
            if self.check_skill(skill):
                return_tag = True
                self.add_skill(skill)

        return return_tag

    def add_buffs(self, buffs: Dict[int, Buff]):
        pass

    def add_dots(self, dots: Dict[int, Dot]):
        pass

    def add(self, attribute: Attribute, skills: Dict[int, Skill], dots: Dict[int, Dot], buffs: Dict[int, Buff]):
        self.add_buffs(buffs)
        self.add_dots(dots)
        self.add_attribute(attribute)
        return self.add_skills(skills)

    def sub_attribute(self, attribute: Attribute):
        pass

    def sub_skill(self, skill: Skill):
        pass

    def sub_skills(self, skills: Dict[int, Skill]):
        if not self.skill_id and not self.recipe_type and not self.recipe_mask:
            return
        for skill_id, skill in skills.items():
            if self.check_skill(skill):
                self.sub_skill(skill)

    def sub_buffs(self, buffs: Dict[int, Buff]):
        pass

    def sub_dots(self, dots: Dict[int, Dot]):
        pass

    def sub(self, attribute: Attribute, skills: Dict[int, Skill], dots: Dict[int, Dot], buffs: Dict[int, Buff]):
        self.sub_buffs(buffs)
        self.sub_skills(skills)
        self.sub_dots(dots)
        self.sub_attribute(attribute)


class Gains(Gain):
    gains: List[Gain]

    def __init__(self, name: str = None, gains: List[Gain] = None):
        super().__init__(name=name)
        if gains:
            self.gains = gains
        else:
            self.gains = []

    def add(self, attribute: Attribute, skills: Dict[int, Skill], dots: Dict[int, Dot], buffs: Dict[int, Buff]):
        for gain in self.gains:
            gain.add(attribute, skills, dots, buffs)

    def sub(self, attribute: Attribute, skills: Dict[int, Skill], dots: Dict[int, Dot], buffs: Dict[int, Buff]):
        for gain in self.gains:
            gain.sub(attribute, skills, dots, buffs)
