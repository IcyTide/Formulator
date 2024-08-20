from typing import Dict

from base.buff import Buff
from base.dot import Dot
from base.gain import Gain
from base.skill import Skill
from schools.shan_hai_xin_jue.skills import 射日加成, 白泽加成


class 桑柘(Gain):
    def add_dots(self, dots: Dict[int, Dot]):
        dots[26856].tick_extra += 1

    def sub_dots(self, dots: Dict[int, Dot]):
        dots[26856].tick_extra -= 1


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


TALENTS: Dict[int, Gain] = {
    35715: Gain("素矰", recipes=[(5373, 1)]),
    35714: Gain("彤弓", recipes=[(5369, 1)]),
    35718: Gain("棘矢"),
    35719: 孰湖("孰湖"),
    35721: Gain("襄尺"),
    35725: Gain("长右"),
    35729: Gain("鹿蜀"),
    35736: 桑柘("桑柘"),
    35733: 诸怀("诸怀"),
    35737: Gain("于狩"),
    35745: Gain("卢令", attributes=dict(agility_gain=102)),
    35749: Gain("托月"),
    35751: Gain("佩弦"),
    35754: Gain("丛云隐月"),
    35757: Gain("贯侯", recipes=[(5422, 1)]),
    35764: Gain("朝仪万汇"),
    35761: 朱厌("朱厌"),

    102012: 射日("射日"),
    102013: 白泽("白泽"),
    102014: Gain("伴生"),
    102015: Gain("灵祇"),
    102016: 偕行("偕行"),
    102010: Gain("白虹贯日"),
}

TALENT_CHOICES = [
    [35715, 35714, 102012, 102013],
    [35718, 35719, 102014, 102015],
    [35721, 102016],
    [35725, 102010],
    [35729],
    [35736, 35733],
    [35737],
    [35745],
    [35749],
    [35751, 35754],
    [35757],
    [35764, 35761]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENTS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
