from typing import Dict, List

from base.gain import Gain
from base.skill import Skill
from kungfus.bei_ao_jue.skills import 项王击鼎秘章


class 含风(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in range(16610, 16614 + 1):
            skills[skill_id].pre_buffs[23066] = {2: 1}
        for skill_id in range(16913, 16918 + 1):
            skills[skill_id].pre_buffs[23066] = {2: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in range(16610, 16614 + 1):
            skills[skill_id].pre_buffs.pop(23066)
        for skill_id in range(16913, 16918 + 1):
            skills[skill_id].pre_buffs.pop(23066)


class 斩纷(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in range(16615, 16619 + 1):
            skills[skill_id].pre_buffs[19510] = {1: 1}
        for skill_id in range(16920, 16925 + 1):
            skills[skill_id].pre_buffs[19510] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in range(16615, 16619 + 1):
            skills[skill_id].pre_buffs.pop(19510)
        for skill_id in range(16920, 16925 + 1):
            skills[skill_id].pre_buffs.pop(19510)


class 征踏(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id, skill in skills.items():
            if isinstance(skill, 项王击鼎秘章) or skill_id in [101108, 101109, 101110] + list(range(101256, 101260)):
                skill.pre_target_buffs[70188] = {10: 1}
                skill.post_target_buffs[70188] = {10: -1}

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id, skill in skills.items():
            if isinstance(skill, 项王击鼎秘章) or skill_id in [101108, 101109, 101110] + list(range(101256, 101260)):
                skill.pre_target_buffs[70188].pop(10)
                skill.post_target_buffs[70188].pop(10)


class 裁魂(Gain):
    @staticmethod
    def pre_effect(parser):
        if 70454 in parser.current_target_buff_stacks:
            parser.refresh_target_buff(70188, 20)

    @staticmethod
    def post_effect(parser):
        if 70454 in parser.current_target_buff_stacks:
            parser.refresh_target_buff(70188, 20, -1)

    def add_skills(self, skills: Dict[int, Skill]):
        skills[101080].pre_effects.append(self.pre_effect)
        skills[101080].post_effects.append(self.post_effect)
        skills[101198].post_target_buffs[70454] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[101080].pre_effects.remove(self.pre_effect)
        skills[101080].post_effects.remove(self.post_effect)
        skills[101198].post_target_buffs.pop(70454)


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            17045: Gain("孤漠"),
            16691: Gain("龙息"),
            16692: Gain("虎踞", recipes=[(4214, 1)])
        },
        {
            16847: Gain("归酣"),
            16777: Gain("沧雪"),
            16816: Gain("碎影")
        },
        {
            17042: Gain("阳关", recipes=[(4298, 1)]),
            26904: Gain("冥鼓", recipes=[(2510, 1), (2511, 1)])
        },
        {
            16799: Gain("霜天"),
            16728: Gain("星火", attributes=dict(strength_gain=102, strain_gain=307)),
        },
        {
            26735: Gain("砺锋"),
            16724: Gain("击瑕")
        },
        {
            32857: Gain("见尘"),
            37982: Gain("临江")
        },
        {
            17047: Gain("分疆"),
            16733: 斩纷("斩纷"),
            18625: Gain("百战")
        },
        {
            25258: Gain("掠关"),
            16779: Gain("化蛟"),
            34677: Gain("绝河")
        },
        {
            16748: Gain("逐鹿"),
            38535: Gain("楚歌")
        },
        {
            17056: Gain("绝期", recipes=[(4319, 1), (2833, 1)])
        },
        {
            25633: 含风("含风"),
            16893: Gain("重烟"),
            16977: Gain("冷川")
        },
        {
            21858: Gain("斩狂枭"),
            16912: Gain("心镜")
        }
    ],
    1: [
        {
            101296: 征踏("征踏")
        },
        {
            101299: 裁魂("裁魂")
        },
        {
            101300: Gain("霸王")
        },
        {
            101015: Gain("上将军印")
        }
    ]
}
