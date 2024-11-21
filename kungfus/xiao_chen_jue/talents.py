from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


class 刚健(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (101960, 100662, 100773, 100821, 100775, 100664, 100653):
            skills[skill_id].pre_target_buffs[70188] = {15: 1}
            skills[skill_id].post_target_buffs[70188] = {15: -1}

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (101960, 100662, 100773, 100821, 100775, 100664, 100653):
            skills[skill_id].pre_target_buffs[70188].pop(15)
            skills[skill_id].post_target_buffs[70188].pop(15)


class 载物(Gain):
    @staticmethod
    def pre_effect(parser):
        if parser.current_buff_stacks[70221].get(1) and not any(parser.current_buff_stacks[70167]):
            parser.refresh_buff(70161, 10)
            parser.refresh_buff(70167, 10)

    @staticmethod
    def post_effect(parser):
        if parser.current_buff_stacks[70221].get(1) and any(parser.current_buff_stacks[70167]):
            parser.refresh_buff(70161, 10, -1)
            parser.refresh_buff(70167, 10, -1)

    def add_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            skill.pre_effects.append(self.pre_effect)
            skill.post_effects.append(self.post_effect)

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            skill.pre_effects.remove(self.pre_effect)
            skill.post_effects.remove(self.post_effect)


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            6812: Gain("玄黄", recipes=[(1714, 1)])
        },
        {
            6813: Gain("御龙"),
            6836: Gain("益元"),
            26702: Gain("坚冰")
        },
        {
            6337: Gain("斜打狗背"),
            6845: Gain("自强", recipes=[(4764, 1), (4765, 1)])
        },
        {
            6820: Gain("无疆")
        },
        {
            32725: Gain("酩酊")
        },
        {
            6832: Gain("越渊")
        },
        {
            28818: Gain("温酒")
        },
        {
            6818: Gain("雨龙"),
            30774: Gain("龙醒")
        },
        {
            37339: Gain("易损"),
            38878: Gain("追远"),
            6822: Gain("贞固")
        },
        {
            6843: Gain("含弘"),
            6814: Gain("复礼"),
        },
        {
            14625: Gain("饮江"),
            6838: Gain("不息"),
            25197: Gain("祭湘君")
        },
        {
            14927: Gain("御鸿于天"),
            28989: Gain("城复于隍")
        }
    ],
    1: [
        {
            100849: 刚健("刚健"),
            100850: Gain("无妄", recipes=[(recipe_id, 1) for recipe_id in range(17233, 17237 + 1)])
        },
        {
            100852: Gain("利涉", attributes=dict(physical_critical_power_rate=100))
        },
        {
            100853: 载物("载物")
        },
        {
            100825: Gain("天下无狗")
        }
    ]
}
