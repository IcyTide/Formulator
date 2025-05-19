from typing import Dict, List

from base.dot import Dot
from base.gain import Gain
from base.skill import Skill


class 孰湖(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[35695].pet_buffs[26857][1] += 1
        skills[35696].pet_buffs[26857][1] += 1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[35695].pet_buffs[26857][1] -= 1
        skills[35696].pet_buffs[26857][1] -= 1


class 诸怀(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[35695].pet_buffs[27099] = {1: 1}
        skills[35696].pet_buffs[27099] = {1: 1}

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[35695].pet_buffs.pop(27099)
        skills[35696].pet_buffs.pop(27099)


class 桑柘(Gain):
    def add_dots(self, dots: Dict[int, Dot]):
        dots[26856].tick_add += 1

    def sub_dots(self, dots: Dict[int, Dot]):
        dots[26856].tick_add -= 1


TALENTS: List[Dict[int, Gain]] = [
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
        35733: 诸怀("诸怀", buff_ids=[27099]),
        35763: Gain("星烨", buff_ids=[26952])
    },
    {
        35737: Gain("于狩", skill_ids=[40717])
    },
    {
        35745: Gain("卢令", attributes=dict(agility_gain=102, strain_gain=102)),
    },
    {
        35757: Gain("贯侯", recipes=[(5422, 1)])
    },
    {
        35751: Gain("佩弦", recipes=[(5748, 1)]),
        35754: Gain("丛云隐月")
    },
    {
        35736: 桑柘("桑柘")
    },
    {
        35764: Gain("朝仪万汇", skill_ids=[36453]),
        40240: Gain("聚势摧霆", skill_ids=[40347, 40720])
    }
]
