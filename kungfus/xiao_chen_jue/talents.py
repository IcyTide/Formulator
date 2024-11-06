from typing import Dict, List

from base.gain import Gain
from base.skill import Skill
from kungfus.xiao_chen_jue.skills import 刚健加成


class 刚健(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 刚健加成):
                skill.pre_target_buffs[70188] = {15: 1}
                skill.post_target_buffs[70188] = {15: -1}

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 刚健加成):
                skill.pre_target_buffs[70188].pop(15)
                skill.post_target_buffs[70188].pop(15)


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
            100849: 刚健("刚健")
        },
        {
            100852: Gain("利涉", attributes=dict(physical_critical_power_rate=100))
        },
        {
            100853: Gain("载物")
        },
        {
            100825: Gain("天下无狗")
        }
    ]
}
