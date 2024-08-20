from typing import Dict

from base.gain import Gain
from base.recipe import DamageAdditionRecipe, MagicalCriticalRecipe
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


TALENTS: Dict[int, Gain] = {
    5896: Gain("涅果", [DamageAdditionRecipe(102, 232, 232)]),
    6589: Gain("明法", [明法()]),
    6788: Gain("秉心"),
    5910: Gain("幻身"),
    5912: Gain("善心"),
    5915: Gain("身意", [MagicalCriticalRecipe((1000, 102), 2572, 2572)]),
    30913: Gain("纷纭"),
    37455: Gain("布泽"),
    17750: Gain("缩地"),
    5913: Gain("降魔渡厄"),
    17730: Gain("金刚怒目"),
    6590: Gain("净果"),
    6586: Gain("三生"),
    24884: Gain("我闻", [MagicalCriticalRecipe((1000, 205), 235, 235)]),
    6596: Gain("众嗔", [众嗔()]),
    5906: Gain("华香", [华香(-614, skill_id, skill_id) for skill_id in (233, 243, 2572, 232)]),
    32647: Gain("无执"),
    14820: Gain("佛果"),
    32648: Gain("金刚日轮"),
    32651: Gain("业因"),
    32649: Gain("无诤")
}

TALENT_CHOICES = [
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
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
