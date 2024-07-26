from typing import Dict

from base.attribute import Attribute
from base.buff import Buff
from base.dot import Dot
from base.gain import Gain
from base.recipe import ExtraTickRecipe
from base.skill import Skill
from base.talent import Talent
from schools.shan_hai_xin_jue.skills import 射日加成, 白泽加成


class 彤弓(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id == 35866:
            skill.physical_critical_strike_rate_extra += 1000
            skill.physical_critical_power_rate_extra += 102

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 35866:
            skill.physical_critical_strike_rate_extra -= 1000
            skill.physical_critical_power_rate_extra -= 102


class 素矰(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id == 35771:
            skill.channel_interval_extra *= 1.05

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 35771:
            skill.channel_interval_extra /= 1.05


class 孰湖(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[35695].pet_buffs[(26857, 1)] += 1
        skills[35696].pet_buffs[(26857, 1)] += 1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[35695].pet_buffs[(26857, 1)] -= 1
        skills[35696].pet_buffs[(26857, 1)] -= 1


class 诸怀(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[35695].pet_buffs[(-27099, 1)] = 1
        skills[35696].pet_buffs[(-27099, 1)] = 1

    def add_buffs(self, buffs: Dict[int, Buff]):
        buffs[26857].begin_buffs[(-27099, 1)] = 1
        buffs[26857].end_buffs[(-27099, 1)] = -1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[35695].pet_buffs.pop((-27099, 1))
        skills[35696].pet_buffs.pop((-27099, 1))

    def sub_buffs(self, buffs: Dict[int, Buff]):
        buffs[26857].begin_buffs.pop((-27099, 1))
        buffs[26857].end_buffs.pop((-27099, 1))


class 卢令(Gain):
    def add_attribute(self, attribute: Attribute):
        attribute.agility_gain += 102

    def sub_attribute(self, attribute: Attribute):
        attribute.agility_gain -= 102


class 贯侯(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id == 36157:
            skill.pve_addition_extra += 205

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 36157:
            skill.pve_addition_extra -= 205


class 朱厌(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[35696].pet_buffs[(27406, 1)] = 1

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[35696].pet_buffs.pop((27406, 1))


class 射日(Gain):
    def add(self, attribute: Attribute, skills: Dict[int, Skill], dots: Dict[int, Dot], buffs: Dict[int, Buff]):
        射日加成.talent_activate = True

    def sub(self, attribute: Attribute, skills: Dict[int, Skill], dots: Dict[int, Dot], buffs: Dict[int, Buff]):
        射日加成.talent_activate = False


class 白泽(Gain):
    def add(self, attribute: Attribute, skills: Dict[int, Skill], dots: Dict[int, Dot], buffs: Dict[int, Buff]):
        白泽加成.talent_activate_1 = True

    def sub(self, attribute: Attribute, skills: Dict[int, Skill], dots: Dict[int, Dot], buffs: Dict[int, Buff]):
        白泽加成.talent_activate_1 = False


class 偕行(Gain):
    def add(self, attribute: Attribute, skills: Dict[int, Skill], dots: Dict[int, Dot], buffs: Dict[int, Buff]):
        白泽加成.talent_activate_2 = True

    def sub(self, attribute: Attribute, skills: Dict[int, Skill], dots: Dict[int, Dot], buffs: Dict[int, Buff]):
        白泽加成.talent_activate_2 = False


TALENT_GAINS: Dict[int, Talent] = {
    35715: Talent("素矰", [素矰(skill_id=35771, skill_recipe=35771)]),
    35714: Talent("彤弓", [彤弓(skill_id=0, skill_recipe=35659)]),
    35718: Talent("棘矢"),
    35719: Talent("孰湖", [孰湖()]),
    35721: Talent("襄尺"),
    35725: Talent("长右"),
    35729: Talent("鹿蜀"),
    35736: Talent("桑柘", [ExtraTickRecipe(1, 26856, 0)]),
    35733: Talent("诸怀", [诸怀()]),
    35737: Talent("于狩"),
    35745: Talent("卢令", [卢令()]),
    35749: Talent("托月"),
    35751: Talent("佩弦"),
    35754: Talent("丛云隐月"),
    35757: Talent("贯侯", [贯侯(skill_id=36157, skill_recipe=36157)]),
    35764: Talent("朝仪万汇"),
    35761: Talent("朱厌", [朱厌()]),

    102012: Talent("射日", [射日()]),
    102013: Talent("白泽", [白泽()]),
    102014: Talent("伴生"),
    102016: Talent("偕行", [偕行()]),
    102010: Talent("白虹贯日"),
}

TALENTS = [
    [35715, 35714, 102012, 102013],
    [35718, 35719, 102014],
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
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
