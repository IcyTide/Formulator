from typing import Dict

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, MagicalCriticalRecipe
from base.skill import Skill
from base.talent import Talent


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
    def add_effect(parser):
        if parser.current_dot_ticks.get(743):
            parser.refresh_buff(-13910, 1)

    @staticmethod
    def remove_effect(parser):
        parser.clear_buff(-13910, 1)

    def add_skills(self, skills: Dict[int, Skill]):
        skills[271].pre_effects.append(self.remove_effect)
        for skill_id in (271, 243, 233):
            skills[skill_id].post_effects.append(self.add_effect)

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[271].pre_effects.remove(self.remove_effect)
        for skill_id in (271, 243, 233):
            skills[skill_id].post_effects.remove(self.add_effect)


class 华香(Gain):
    skill_ids = (list(range(13681, 13686 + 1)) + list(range(3842, 3850 + 1)) + list(range(3814, 3816 + 1)) +
                 [2866, 3833, 3836, 3839, 6787, 17641, 17642])

    def add_skill(self, skill: Skill):
        if skill.skill_id in self.skill_ids:
            skill.solar_shield_gain_extra += self.value

    def sub_skill(self, skill: Skill):
        if skill.skill_id in self.skill_ids:
            skill.solar_shield_gain_extra -= self.value


TALENT_GAINS: Dict[int, Talent] = {
    5896: Talent("涅果", [DamageAdditionRecipe(102, 232, 232)]),
    6589: Talent("明法", [明法()]),
    6788: Talent("秉心"),
    5910: Talent("幻身"),
    5912: Talent("善心"),
    5915: Talent("身意", [MagicalCriticalRecipe((1000, 102), 2572, 2572)]),
    30913: Talent("纷纭"),
    37455: Talent("布泽"),
    17750: Talent("缩地"),
    5913: Talent("降魔渡厄"),
    17730: Talent("金刚怒目"),
    6590: Talent("净果"),
    6586: Talent("三生"),
    24884: Talent("我闻", [MagicalCriticalRecipe((1000, 205), 235, 235)]),
    6596: Talent("众嗔", [众嗔()]),
    5906: Talent("华香", [华香(-614, skill_id, skill_id) for skill_id in (233, 243, 2572, 232)]),
    32647: Talent("无执"),
    14820: Talent("佛果"),
    32648: Talent("金刚日轮"),
    32651: Talent("业因"),
    32649: Talent("无诤")
}

TALENTS = [
    [6589, 5896, 6788],
    [5910, 5912],
    [30913, 5915],
    [37455, 17750],
    [5913],
    [17730],
    [6590],
    [6586, 24884],
    [6596],
    [5906, 32647],
    [32648, 14820],
    [32651, 32649]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
