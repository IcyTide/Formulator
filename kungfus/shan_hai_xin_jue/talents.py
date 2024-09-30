from typing import Dict, List

from base.buff import Buff
from base.gain import Gain
from base.skill import Skill
from kungfus.shan_hai_xin_jue.skills import 射日加成, 白泽加成


class 孰湖(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[35695].pet_buffs[26857][1] += 1
        skills[35696].pet_buffs[26857][1] += 1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[35695].pet_buffs[26857][1] -= 1
        skills[35696].pet_buffs[26857][1] -= 1


class 诸怀(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[35695].pet_buffs[-27099] = {1: 1}
        skills[35696].pet_buffs[-27099] = {1: 1}

    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[26857].begin_buffs[-27099] = {1: 1}
        buffs[26857].end_buffs[-27099] = {1: 0}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[35695].pet_buffs.pop(-27099)
        skills[35696].pet_buffs.pop(-27099)

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[26857].begin_buffs.pop(-27099)
        buffs[26857].end_buffs.pop(-27099)


class 朱厌(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[35696].pet_buffs[27406] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[35696].pet_buffs.pop(27406)


class 射日(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 射日加成):
                skill.pre_target_buffs[70188] = {25: 1}
                skill.post_target_buffs[70188] = {25: -1}

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 射日加成):
                skill.pre_target_buffs[70188].pop(25)
                skill.post_target_buffs[70188].pop(25)


class 白泽(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 白泽加成):
                skill.pre_target_buffs[70188] = {30: 1}
                skill.post_target_buffs[70188] = {30: -1}

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 白泽加成):
                skill.pre_target_buffs[70188].pop(30)
                skill.post_target_buffs[70188].pop(30)


class 偕行(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 白泽加成):
                skill.post_target_buffs[71182] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill in skills.values():
            if isinstance(skill, 白泽加成):
                skill.post_target_buffs.pop(71182)


TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            35715: Gain("素矰", recipes=[(5373, 1)]),
            35714: Gain("彤弓", recipes=[(5369, 1)])
        },
        {
            35718: Gain("棘矢"),
            35719: 孰湖("孰湖")
        },
        {
            35721: Gain("襄尺")
        },
        {
            35725: Gain("长右")
        },
        {
            35729: Gain("鹿蜀")
        },
        {
            35733: 诸怀("诸怀")
        },
        {
            35737: Gain("于狩")
        },
        {
            35745: Gain("卢令", attributes=dict(agility_gain=102))
        },
        {
            35757: Gain("贯侯", recipes=[(5422, 1)])
        },
        {
            35751: Gain("佩弦"),
            35754: Gain("丛云隐月")
        },
        {
            35759: Gain("审固")
        },
        {
            35764: Gain("朝仪万汇"),
            35761: 朱厌("朱厌")
        }
    ],
    1: [
        {
            102012: 射日("射日"),
            102013: 白泽("白泽")
        },
        {
            102014: Gain("伴生"),
            102015: Gain("灵祇")
        },
        {
            102016: 偕行("偕行")
        },
        {
            102010: Gain("白虹贯日")
        }
    ]
}
