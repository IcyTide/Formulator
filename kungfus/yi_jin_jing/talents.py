from typing import Dict, List

from base.gain import Gain
from base.skill import Skill
from kungfus.yi_jin_jing.skills import 罗汉棍法


class 明法(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (17641, 17642):
            skills[skill_id].post_target_buffs = {12479: {1: 1}}
        for skill_id in (3848, 3849, 3850):
            skills[skill_id].post_target_buffs[12479] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (17641, 17642):
            skills[skill_id].post_target_buffs = {890: {1: 1}}
        for skill_id in (3848, 3849, 3850):
            skills[skill_id].post_target_buffs.pop(12479)


class 众嗔(Gain):
    @staticmethod
    def post_effect(parser):
        if parser.current_dot_ticks.get(743):
            parser.refresh_buff(-13910, 1)

    def add_skills(self, skills: Dict[int, Skill]):
        skills[271].pre_buffs[-13910] = {1: -1}
        for skill_id in (271, 243, 233):
            skills[skill_id].post_effects.append(self.post_effect)

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[271].pre_buffs.pop(-13910)
        for skill_id in (271, 243, 233):
            skills[skill_id].post_effects.remove(self.post_effect)


class 如来(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 罗汉棍法):
                if 70188 not in skill.pre_target_buffs:
                    skill.pre_target_buffs[70188] = {}
                skill.pre_target_buffs[70188][25] = 1
                if 70188 not in skill.post_target_buffs:
                    skill.post_target_buffs[70188] = {}
                skill.post_target_buffs[70188][25] = -1

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 罗汉棍法):
                skill.pre_target_buffs[70188].pop(25)
                skill.post_target_buffs[70188].pop(25)


class 法界(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[101796].pre_target_buffs[70188] = {30: 1}
        skills[101796].post_target_buffs[70188] = {30: -1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[101796].pre_target_buffs.pop(70188)
        skills[101796].post_target_buffs.pop(70188)


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            5896: Gain("涅果", recipes=[(959, 3)]),
            6589: 明法("明法"),
            6788: Gain("秉心")
        },
        {
            5910: Gain("幻身"),
            5912: Gain("善心")
        },
        {
            5915: Gain("身意", recipes=[(2299, 1)]),
            30913: Gain("纷纭")
        },
        {
            37455: Gain("布泽"),
            17750: Gain("缩地")
        },
        {
            5913: Gain("降魔渡厄")
        },
        {
            17730: Gain("金刚怒目")
        },
        {
            6590: Gain("净果")
        },
        {
            6586: Gain("三生"),
            24884: Gain("我闻", recipes=[(5157, 1)])
        },
        {
            6596: 众嗔("众嗔"),
            24885: Gain("诸行")
        },
        {
            38957: Gain("华香"),
            32647: Gain("无执")
        },
        {
            32648: Gain("金刚日轮")
        },
        {
            32651: Gain("业因"),
            32649: Gain("无诤")
        }
    ],
    1: [
        {
            101780: 如来("如来")
        },
        {
            101783: Gain("无垢")
        },
        {
            101784: 法界("法界")
        },
        {
            101762: Gain("醍醐灌顶")
        }
    ]
}
