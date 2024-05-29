from typing import Dict

from base.buff import Buff
from base.gain import Gain
from base.skill import Skill


class 涅果(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[17641].skill_damage_addition += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[17641].skill_damage_addition -= 102


class 明法(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (26989, 26991):
            skills[skill_id].bind_buff = 12479

        skills[17641].post_target_buffs.pop((890, 1))
        skills[17641].post_target_buffs = {(12479, 1): 1}
        for skill_id in (3848, 3849, 3850):
            skills[skill_id].post_target_buffs[(12479, 1)] = 1

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (26989, 26991, 17641):
            skills[skill_id].bind_buff = 890

        skills[17641].post_target_buffs.pop((12479, 1))
        skills[17641].post_target_buffs[(890, 1)] = 1
        for skill_id in (3848, 3849, 3850):
            skills[skill_id].post_target_buffs.pop((12479, 1))


class 众嗔(Gain):
    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[-13910].activate = True

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[-13910].activate = False


class 华香(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (17641, 3848, 3849, 3850, 3814, 3816, 13685):
            skills[skill_id].skill_shield_gain -= 614

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (17641, 3848, 3849, 3850, 3814, 3816, 13685):
            skills[skill_id].skill_shield_gain += 614


TALENT_GAINS: Dict[int, Gain] = {
    5896: 涅果("涅果"),
    6589: 明法("明法"),
    5910: Gain("幻身"),
    30913: Gain("纷纭"),
    37455: Gain("布泽"),
    5913: Gain("降魔渡厄"),
    17730: Gain("金刚怒目"),
    6590: Gain("净果"),
    6586: Gain("三生"),
    6596: 众嗔("众嗔"),
    5906: 华香("华香"),
    32648: Gain("金刚日轮"),
    32651: Gain("业因")
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
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
