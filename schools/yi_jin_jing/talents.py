from typing import Dict

from base.gain import Gain
from base.talent import Talent
from base.recipe import DamageAdditionRecipe
from base.skill import Skill


class 明法(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[17641].post_target_buffs = {(12479, 1): 1}
        for skill_id in (3848, 3849, 3850):
            skills[skill_id].post_target_buffs[(12479, 1)] = 1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[17641].post_target_buffs = {(890, 1): 1}
        for skill_id in (3848, 3849, 3850):
            skills[skill_id].post_target_buffs.pop((12479, 1))


class 众嗔(Gain):
    @staticmethod
    def pre_effect(parser):
        if 743 in parser.current_dot_ticks:
            parser.refresh_buff(-13910, 1)

    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (3848, 3849, 3850, 13685):
            skills[skill_id].pre_effects.append(self.pre_effect)

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (3848, 3849, 3850, 13685):
            skills[skill_id].pre_effects.remove(self.pre_effect)


class 华香(Gain):
    skill_ids = (list(range(13681, 13686 + 1)) + list(range(3842, 3850 + 1)) + list(range(3814, 3816 + 1)) +
                 [2866, 3833, 3836, 3839, 6787, 17641, 17642])

    def add_skill(self, skill: Skill):
        if skill.skill_id in self.skill_ids:
            skill.magical_shield_gain_extra -= 614

    def sub_skill(self, skill: Skill):
        if skill.skill_id in self.skill_ids:
            skill.magical_shield_gain_extra += 614


TALENT_GAINS: Dict[int, Talent] = {
    5896: Talent("涅果", [DamageAdditionRecipe(102, 232, 232)]),
    6589: Talent("明法", [明法()]),
    5910: Talent("幻身"),
    30913: Talent("纷纭"),
    37455: Talent("布泽"),
    5913: Talent("降魔渡厄"),
    17730: Talent("金刚怒目"),
    6590: Talent("净果"),
    6586: Talent("三生"),
    6596: Talent("众嗔", [众嗔()]),
    5906: Talent("华香", [华香(skill_id=skill_id, skill_recipe=skill_id) for skill_id in (233, 243, 2572, 232)]),
    32648: Talent("金刚日轮"),
    32651: Talent("业因")
}

TALENTS = [
    [6589, 5896],
    [5910],
    [30913],
    [37455],
    [5913],
    [17730],
    [6590],
    [6586],
    [6596],
    [5906],
    [32648],
    [32651]
]
TALENT_DECODER = {talent_id: talent.talent_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
