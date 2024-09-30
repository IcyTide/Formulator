from typing import Dict, List

from base.gain import Gain
from base.skill import Skill


class 神门(Gain):
    @staticmethod
    def pre_effect(parser):
        if parser.current_buff_stacks[28756].get(1):
            parser.refresh_buff(29254, 1)

    def add_skills(self, skills: Dict[int, Skill]):
        skills[38083].pre_effects.append(self.pre_effect)

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[38083].pre_effects.remove(self.pre_effect)


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            38465: Gain("阳池", recipes=[(5578, 1)]),
            38466: Gain("玄气", recipes=[(5610, 1)]),
            38467: Gain("凝阴")
        },
        {
            38468: Gain("涌泉", recipes=[(5617, 1)]),
            38469: Gain("浥尘"),
            38470: Gain("启霁")
        },
        {
            38471: Gain("疾掠"),
            38472: Gain("然谷"),
            38473: Gain("封府"),
            38474: Gain('清激')
        },
        {
            38476: Gain("山雨重楼"),
            38477: Gain("反朴"),
            38478: Gain("轻岚"),
            38480: Gain("见飓")
        },
        {
            38479: Gain("静霂"),
            38481: Gain("神封"),
            38482: Gain("皎夜"),
            38492: Gain("霏微"),
        },
        {
            38483: Gain("飒星"),
            38484: Gain("悬枢"),
            38485: Gain("太溪"),
            38486: Gain("霰珠")
        },
        {
            38487: Gain("泽前"),
            38488: Gain("止蔌"),
            38489: Gain("心俞"),
            38490: 神门("神门")
        },
        {
            38475: Gain("纷飙", recipes=[(5620, 1)]),
            38549: Gain("朔风扬尘"),
            38493: Gain("零露"),
            38494: Gain("通里"),
            38495: Gain("出岫")
        },
        {
            38496: Gain("梨盏"),
            38497: Gain("意舍"),
            38498: Gain("流絮"),
            38499: Gain("郁潆"),
            38500: Gain("玉枕")
        },
        {
            38501: Gain("茫缈", recipes=[(5640, 1)]),
            38502: Gain("卫分"),
            38503: Gain("百会"),
            38504: Gain("既晓"),
            38505: Gain("滃从", recipes=[(5645, 1), (5646, 1), (5647, 1)])
        },
        {
            38506: Gain("欺霜"),
            38507: Gain("摧烟"),
            38508: Gain("丘墟"),
            38509: Gain("灵台"),
            38510: Gain("青霭")
        },
        {
            38511: Gain("一阳来复"),
            38512: Gain("逆脉"),
            38513: Gain("徙溟"),
            38514: Gain("相息"),
            38515: Gain("胧雾观花")
        }
    ],
    1: [
        {
            102293: Gain("驭风")
        },
        {
            102296: Gain("风扬")
        },
        {
            102298: Gain("奇脉")
        },
        {
            102290: Gain("一阳化生")
        }
    ]
}
