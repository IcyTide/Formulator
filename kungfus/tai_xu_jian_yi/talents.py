from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


class 风逝(Gain):
    @staticmethod
    def trigger_effect(parser):
        if parser.current_buff_stacks[29204].get(1):
            parser.refresh_target_buff(29451, 1)

    @staticmethod
    def consume_pre_effect(parser):
        if buff_stack := parser.current_target_buff_stacks[29451].get(1):
            parser.refresh_target_buff(-29451, 1, buff_stack)

    @staticmethod
    def consume_post_effect(parser):
        parser.clear_target_buff(-29451)
        parser.clear_target_buff(29451)

    def add_skills(self, skills: Dict[int, Skill]):
        skills[394].post_effects.append(self.trigger_effect)
        skills[4954].pre_effects.append(self.consume_pre_effect)
        skills[4954].post_effects.append(self.consume_post_effect)

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[394].post_effects.remove(self.trigger_effect)
        skills[4954].pre_effects.remove(self.consume_pre_effect)
        skills[4954].post_effects.remove(self.consume_post_effect)


class 无欲(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[2681].post_buffs[2757] = {5: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[2681].post_buffs[2757] = {1: 1}


TALENTS: List[Dict[int, Gain]] = {
    0: [
        {
            5807: Gain("心固", recipes=[(638, 3)])
        },
        {
            32407: Gain("和光", recipes=[(5722, 1)])
        },
        {
            5800: Gain("白虹"),
            357: Gain("化三清"),
            38539: Gain("无尤"),
            38540: Gain("浑沦")
        },
        {
            5818: Gain("无意", recipes=[(2263, 1)]),
            21812: Gain("云中剑")
        },
        {
            14833: Gain("玄门"),
            36106: Gain("瑞氛"),
            24969: Gain("合虚")
        },
        {
            5821: Gain("叠刃")
        },
        {
            6481: Gain("雾外江山"),
            6758: Gain("切玉"),
            21725: Gain("长生")
        },
        {
            14829: Gain("负阴"),
            24962: Gain("裂云"),
            14598: Gain("若水")
        },
        {
            18799: Gain("故长")
        },
        {
            6472: Gain("期声"),
            34656: Gain("剑入")
        },
        {
            14832: Gain("虚极", recipes=[(4583, 1), (5173, 1)]),
            17731: 无欲("无欲")
        },
        {
            17742: 风逝("风逝"),
            24972: Gain("凌云剑"),
            15187: Gain("行天道")
        }
    ],
    1: [
        {
            100448: Gain("周行")
        },
        {
            100449: Gain("神灵")
        },
        {
            100451: Gain("固强")
        },
        {
            100015: Gain("行剑千风")
        }
    ]
}
