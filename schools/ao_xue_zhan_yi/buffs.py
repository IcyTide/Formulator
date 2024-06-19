from typing import Dict

from assets.setter import set_buff
from base.buff import Buff, CustomBuff
from base.gain import Gain
from base.recipe import DamageAdditionRecipe
from base.skill import Skill
from general.buffs import GENERAL_BUFFS


class 战心(Gain):
    def add_skill(self, skill: Skill):
        if skill.skill_id in (18591, 15000, 18610, 26773, 401):
            skill.channel_interval_extra *= 1.2

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (18591, 15000, 18610, 26773, 401):
            skill.channel_interval_extra /= 1.2


SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        1428: {}, 6121: {}, 6363: {}, 14981: {}, 7671: {}, 21638: {}, 2779: {}, 28169: {},
        -12608: dict(buff_name="风虎", activate=False, interval=4,
                     gains=[[DamageAdditionRecipe(value, skill_id, skill_id) for value in (51, 102, 154, 205, 256)]
                            for skill_id in (400, 403, 415, 423)]),
        -26008: dict(buff_name="战心", interval=4, gains=[战心(skill_id=401, skill_recipe=401)])
    },
    CustomBuff: {
        -1: dict(buff_name="战意", max_stack=5),
    }
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        set_buff(buff)
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
