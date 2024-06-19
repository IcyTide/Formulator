from assets.buffs import BUFFS
from assets.dots import DOTS
from assets.skills import SKILLS
from base.buff import Buff
from base.skill import Skill, Dot


def set_skill(skill: Skill):
    skill_id = skill.skill_id
    if isinstance(skill, Dot):
        for attr, value in DOTS.get(skill_id, {}).items():
            setattr(skill, attr, value)
    else:
        for attr, value in SKILLS.get(skill_id, {}).items():
            setattr(skill, attr, value)


def set_buff(buff: Buff):
    buff_id = buff.buff_id
    if buff_id < 0:
        buff_id = -buff_id
    for attr, value in BUFFS.get(buff_id, {}).items():
        setattr(buff, attr, value)
