from typing import Dict, List

from base.gain import Gain
from base.skill import Skill
from kungfus.fen_ying_sheng_jue.skills import 净世破魔击


class 日月同辉(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 净世破魔击):
                if 70188 not in skill.pre_target_buffs:
                    skill.pre_target_buffs[70188] = {}
                skill.pre_target_buffs[70188][30] = 1
                if 70188 not in skill.post_target_buffs:
                    skill.post_target_buffs[70188] = {}
                skill.post_target_buffs[70188][30] = -1

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 净世破魔击):
                skill.pre_target_buffs[70188].pop(30)
                skill.post_target_buffs[70188].pop(30)


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            5972: Gain("腾焰飞芒", recipes=[(1314, 1), (1315, 1)])
        },
        {
            18279: Gain("净身明礼", recipes=[(5149, 1), (5150, 1)])
        },
        {
            22888: Gain("诛邪镇魔")
        },
        {
            6717: Gain("无明业火")
        },
        {
            34383: Gain("明光恒照")
        },
        {
            34395: Gain("日月同辉")
        },
        {
            34372: Gain("靡业报劫")
        },
        {
            17567: Gain("用晦而明", buff_ids=[-12575])},
        {
            25166: Gain("净体不畏"),
            5979: Gain("天地诛戮")
        },
        {
            38526: Gain("降灵尊")
        },
        {
            34347: Gain("悬象著明")
        },
        {
            37337: Gain("崇光斩恶"),
            34370: Gain("日月齐光")
        }
    ],
    1: [
        {
            100788: Gain("圣光破邪")
        },
        {
            100790: 日月同辉("日月同辉"),
        },
        {
            100791: Gain("轮回死生")
        },
        {
            101862: Gain("日月晦")
        }
    ]
}
