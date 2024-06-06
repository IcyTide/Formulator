from typing import Dict

from base.buff import Buff
from base.gain import Gain
from base.talent import Talent
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

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[28169].begin_effects.remove(self.begin_effect)


TALENT_GAINS: Dict[int, Talent] = {
    18487: Talent("百折"),
    5656: Talent("封侯", [DamageAdditionRecipe(102, 0, 400)]),
    5657: Talent("扬戈", [PhysicalCriticalRecipe((1000, 102), 400, 400)]),
    5660: Talent("神勇", [PhysicalCriticalRecipe((1000, 102), 415, 415)]),
    5659: Talent("大漠"),
    18602: Talent("骁勇", [骁勇(skill_id=401, skill_recipe=401)]),
    24896: Talent("龙驭"),
    14824: Talent("驰骋"),
    6511: Talent("牧云"),
    5666: Talent("风虎", [风虎()]),
    6781: Talent("战心", [战心()]),
    6524: Talent("破楼兰"),
    2628: Talent("渊"),
    5678: Talent("夜征"),
    15001: Talent("龙血"),
    6517: Talent("虎贲", [虎贲()])
}

TALENTS = [
    [18487, 5656, 5657],
    [5660],
    [5659, 18602],
    [24896],
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
