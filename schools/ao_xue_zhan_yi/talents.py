from typing import Dict

from base.buff import Buff
from base.gain import Gain, Gains
from base.recipe import DamageAdditionRecipe, PhysicalCriticalRecipe
from base.skill import Skill


class 风虎(Gain):
    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[-12608].activate = True

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[-12608].activate = False


class 战心(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[423].pre_buffs[(-26008, 1)] = 1
        skills[702].post_buffs[(-1, 1)] = 3

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[423].pre_buffs.pop((-26008, 1))
        skills[702].post_buffs.pop((-1, 1))


class 骁勇(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id in (18591, 15000, 18610, 26773, 401):
            skill.channel_interval_extra *= 1.12

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (18591, 15000, 18610, 26773, 401):
            skill.channel_interval_extra /= 1.12


class 虎贲(Gain):
    @staticmethod
    def begin_effect(parser):
        parser.current_school.skills[18773].post_buffs[(-1, 1)] = -3

    @staticmethod
    def end_effect(parser):
        parser.current_school.skills[18773].post_buffs[(-1, 1)] = 0

    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[28169].begin_effects.append(self.begin_effect)
        buffs[28169].end_effects.append(self.end_effect)

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[28169].begin_effects.remove(self.begin_effect)
        buffs[28169].end_effects.remove(self.end_effect)


TALENT_GAINS: Dict[int, Gains] = {
    18487: Gains("百折"),
    5656: Gains("封侯", [DamageAdditionRecipe(102, 0, 400)]),
    5657: Gains("扬戈", [PhysicalCriticalRecipe((1000, 102), 400, 400)]),
    5660: Gains("神勇", [PhysicalCriticalRecipe((1000, 102), 415, 415)]),
    5659: Gains("大漠"),
    18602: Gains("骁勇", [骁勇(skill_id=401, recipe_type=401)]),
    24896: Gains("龙驭"),
    18226: Gains("击水"),
    14824: Gains("驰骋"),
    6511: Gains("牧云"),
    5666: Gains("风虎", [风虎()]),
    6781: Gains("战心", [战心()]),
    6524: Gains("破楼兰"),
    2628: Gains("渊"),
    5678: Gains("夜征"),
    15001: Gains("龙血"),
    6517: Gains("虎贲", [虎贲()])
}

TALENTS = [
    [18487, 5656, 5657],
    [5660],
    [5659, 18602],
    [24896, 18226],
    [14824],
    [6511],
    [5666],
    [6781],
    [6524, 2628],
    [5678],
    [15001],
    [6517],
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
