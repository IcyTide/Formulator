from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


class 用晦而明(Gain):
    @staticmethod
    def pre_effect_1(parser):
        if not parser.current_buff_stacks[30642]:
            return
        buff_level = 1
        if parser.current_buff_stacks[30644]:
            buff_level = 2
        parser.refresh_buff(12575, buff_level)

    @staticmethod
    def pre_effect_2(parser):
        if not parser.current_buff_stacks[30643]:
            return
        buff_level = 1
        if parser.current_buff_stacks[306445]:
            buff_level = 2
        parser.refresh_buff(12575, buff_level)

    @staticmethod
    def post_effect(parser):
        parser.clear_buff(12501)

    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id, skill in skills.items():
            if skill_id in [14701, 40088, 6257, 34348, 34354, 34356, 34361, 34363]:
                skill.pre_effects.append(self.pre_effect_1)
            elif skill_id in [4476, 40089, 6258, 34349, 34353, 34355, 34359, 34362]:
                skill.pre_effects.append(self.pre_effect_2)
            elif skill_id == 37336:
                skill.pre_effects.append(self.pre_effect_1)
            elif skill_id == 4480:
                skill.pre_effects.append(self.pre_effect_2)
            elif skill_id == 32816:
                skill.pre_effects = [
                    self.pre_effect_1, self.pre_effect_2, self.pre_effect_1, self.pre_effect_2, self.pre_effect_1
                ]
            else:
                continue
            skill.post_effects.append(self.post_effect)


TALENTS: List[Dict[int, Gain]] = [
    {
        5974: Gain("血泪成悦"),
        5972: Gain("腾焰飞芒", recipes=[(1314, 1), (1315, 1)])
    },
    {
        18279: Gain("净身明礼", skill_ids=[18280, 18281], recipes=[(5149, 1), (5150, 1)])
    },
    {
        22888: Gain("诛邪镇魔", buff_ids=[28886], skill_ids=[26916])
    },
    {
        6717: Gain("无明业火", buff_ids=[6277])
    },
    {
        34383: Gain("明光恒照", buff_ids=[25758, 25759])
    },
    {
        34395: Gain("日月同辉")
    },
    {
        25166: Gain("净体不畏", skill_ids=[26708, 26707]),
        34372: Gain("靡业报劫", dot_ids=[25725, 25726], skill_ids=[34373, 34374])
    },
    {
        17567: 用晦而明("用晦而明", buff_ids=[30642, 30643, 30644, 30645, 12575])},
    {
        5979: Gain("天地诛戮", buff_ids=[4754])
    },
    {
        38526: Gain("降灵尊", skill_ids=[34985])
    },
    {
        34347: Gain("明赦尊谕", skill_ids=[
            skill_id for skill_id in range(34348, 34363 + 1) if skill_id not in [34350, 34351, 34352, 34358]
        ])
    },
    {
        37337: Gain("崇光斩恶")
    }
]
