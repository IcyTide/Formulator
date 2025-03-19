from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


class 凤阙(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[100784].pre_target_buffs[70188] = {30: 1}
        skills[100784].post_target_buffs[70188] = {30: -1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[100784].pre_target_buffs.pop(70188)
        skills[100784].post_target_buffs.pop(70188)


class 澜江(Gain):
    @staticmethod
    def pre_effect(parser):
        if buff_stack := parser.current_buff_stacks[70899].get(1):
            parser.refresh_target_buff(70188, buff_stack * 3)

    @staticmethod
    def post_effect(parser):
        if buff_stack := parser.current_buff_stacks[70899].get(1):
            parser.refresh_target_buff(70188, buff_stack * 3, -1)

    def add_skills(self, skills: Dict[int, Skill]):
        skills[100807].pre_effects.append(self.pre_effect)
        skills[100807].post_effects.append(self.post_effect)

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[100807].pre_effects.remove(self.pre_effect)
        skills[100807].post_effects.remove(self.post_effect)


class 飞来闻踪(Gain):
    @staticmethod
    def pre_effect(parser):
        if parser.current_buff_stacks[70953].get(1):
            parser.refresh_target_buff(70188, 25)
        if parser.current_buff_stacks[70953].get(2):
            parser.refresh_target_buff(70188, 20)
        if parser.current_buff_stacks[70953].get(3):
            parser.refresh_target_buff(70188, 15)

    @staticmethod
    def post_effect(parser):
        if parser.current_buff_stacks[70953].get(1):
            parser.refresh_target_buff(70188, 25, -1)
        if parser.current_buff_stacks[70953].get(2):
            parser.refresh_target_buff(70188, 20, -1)
        if parser.current_buff_stacks[70953].get(3):
            parser.refresh_target_buff(70188, 15, -1)

    def add_skills(self, skills: Dict[int, Skill]):
        skills[100807].pre_effects.append(self.pre_effect)
        skills[100807].post_effects.append(self.post_effect)

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[100807].pre_effects.remove(self.pre_effect)
        skills[100807].post_effects.remove(self.post_effect)


TALENTS: List[Dict[int, Gain]] = {
    0: [
        {
            5953: Gain("淘尽", recipes=[(1235, 1)])
        },
        {
            5954: Gain("清风", recipes=[(1236, 1)])
        },
        {
            5952: Gain("岱宗")
        },
        {
            6537: Gain("斩岳"),
            6549: Gain("残雪")
        },
        {
            5964: Gain("造化")
        },
        {
            5957: Gain("怜光")
        },
        {
            6545: Gain("层云"),
            18682: Gain("景行")
        },
        {
            30862: Gain("山倾")
        },
        {
            6534: Gain("雾锁")
        },
        {
            6548: Gain("碧归"),
            38674: Gain("长晖", recipes=[(5670, 1)])
        },
        {
            14605: Gain("如风")
        },
        {
            25070: Gain("飞来闻踪"),
            30777: Gain("听晓")
        }
    ],
    1: [
        {
            100919: Gain("折梅", attributes=dict(physical_critical_power_rate=100))
        },
        {
            100918: 凤阙("凤阙")
        },
        {
            100921: 澜江("澜江")
        },
        {
            101934: 飞来闻踪("飞来闻踪")
        }
    ]
}
