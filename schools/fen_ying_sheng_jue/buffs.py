from typing import Dict

from base.buff import Buff
from base.gain import Gain
from base.recipe import CriticalStrikeRecipe
from base.skill import Skill
from general.buffs import GENERAL_BUFFS


class SolarAttackPowerRecipe(Gain):
    def add_skill(self, skill: Skill):
        skill.solar_attack_power_gain += self.value

    def sub_skill(self, skill: Skill):
        skill.solar_attack_power_gain -= self.value


class LunarAttackPowerRecipe(Gain):
    def add_skill(self, skill: Skill):
        skill.lunar_attack_power_gain += self.value

    def sub_skill(self, skill: Skill):
        skill.lunar_attack_power_gain -= self.value


SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        4671: {}, 4754: {}, 6277: {}, 28886: {}, 25721: {},
        4423: dict(gains=[CriticalStrikeRecipe(10000, skill_id, skill_id) for skill_id in (3966, 3967)]),
        -12575: dict(buff_name="用晦而明", interval=8),
        25759: dict(buff_name="明光·日", frame_shift=1,
                    gains=[SolarAttackPowerRecipe(246, skill_id, skill_recipe)
                           for skill_id, skill_recipe in ((0, 3966), (0, 3967), (34348, 0))]),
        25758: dict(buff_name="明光·月", frame_shift=1,
                    gains=[LunarAttackPowerRecipe(246, skill_id, skill_recipe)
                           for skill_id, skill_recipe in ((0, 3966), (4476, 0), (34349, 0))])
    },
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        buff.set_asset()
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
