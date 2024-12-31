from typing import Dict, List

from base.dot import Dot
from base.gain import Gain
from base.skill import Skill


class 凄骨(Gain):
    @staticmethod
    def post_effect(parser):
        if parser.current_buff_stacks[20054].get(1) == 3:
            parser.refresh_buff(20696, 1)

    def add_skills(self, skills: Dict[int, Skill]):
        skills[27557].post_effects.append(self.post_effect)

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[27557].post_effects.remove(self.post_effect)


class 疾根(Gain):
    def add_dots(self, dots: Dict[int, Dot]):
        dots[20052].tick_add += 1

    def sub_dots(self, dots: Dict[int, Dot]):
        dots[20052].tick_add -= 1


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            38631: Gain("连茹"),
            28338: Gain("怯邪"),
            27530: Gain("川谷", recipes=[(2541, 1)])
        },
        {
            28344: Gain("鸩羽", recipes=[(2549, 1)]),
            28343: Gain("淮茵"),
        },
        {
            28361: Gain("结草")
        },
        {
            29498: Gain("灵荆")
        },
        {
            39661: Gain("逆势"),
            28406: Gain("遍休")
        },
        {
            28410: Gain("坚阴"),
            30507: Gain("渌波"),
            38632: Gain("汲刺")
        },
        {
            28413: Gain("相使")
        },
        {
            28419: 凄骨("凄骨")
        },
        {
            28432: 疾根("疾根")
        },
        {
            38965: Gain("紫伏"),
            28431: Gain("避奚"),
            30734: Gain("折枝拂露")
        },
        {
            28443: Gain("甘遂"),
            28458: Gain("炮阳"),
            28415: Gain("荆障")
        },
        {
            32896: Gain("应理与药"),
            28426: Gain("养荣")
        }
    ],
    1: [
        {
            101419: Gain("鬼门")
        },
        {
            101422: Gain("神莹")
        },
        {
            101423: Gain("济世")
        },
        {
            101370: Gain("苍棘缚地")
        }
    ]
}
