from dataclasses import dataclass
from typing import Tuple, List, Dict, Type, Union

from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from base.skill import Skill

from schools import bei_ao_jue, shan_hai_xin_jue, ling_hai_jue, wu_fang, gu_feng_jue, tai_xu_jian_yi, tian_luo_gui_dao

SKILL_TYPE = Tuple[int, int, int]
BUFFER_TYPE = Tuple[int, int, int, bool]
# BUFFER_TYPE = Tuple[int, int]
BUFF_TYPE = Tuple[int, int, int]
TIMELINE_TYPE = List[Tuple[int, bool]]
SUB_RECORD_TYPE = Dict[Tuple[tuple, tuple], TIMELINE_TYPE]
RECORD_TYPE = Dict[SKILL_TYPE, SUB_RECORD_TYPE]
STATUS_TYPE = Dict[Tuple[int, int], int]
SNAPSHOT_TYPE = Dict[int, STATUS_TYPE]


@dataclass
class School:
    school: str
    major: str
    kind: str
    attribute: Type[Attribute]
    formation: str
    skills: Dict[int, Skill]
    buffs: Dict[int, Buff]
    talent_gains: Dict[int, Gain]
    talents: List[List[int]]
    talent_decoder: Dict[int, str]
    talent_encoder: Dict[str, int]
    recipe_gains: Dict[str, Dict[str, Gain]]
    recipes: Dict[str, List[str]]
    gains: Dict[Union[Tuple[int, int], int], Gain]
    display_attrs: Dict[str, str]

    def attr_content(self, attribute):
        content = []
        for attr, name in self.display_attrs.items():
            value = getattr(attribute, attr)
            if isinstance(value, int):
                content.append([name, f"{value}"])
            else:
                content.append([name, f"{round(value * 100, 2)}%"])
        return content


PHYSICAL_DISPLAY_ATTRS = {
    "base_physical_attack_power": "基础攻击",
    "physical_attack_power": "攻击",
    "base_physical_critical_strike": "会心等级",
    "physical_critical_strike": "会心",
    "physical_critical_power_base": "会效等级",
    "physical_critical_power": "会效",
    "base_physical_overcome": "基础破防",
    "final_physical_overcome": "最终破防",
    "physical_overcome": "破防",
    "weapon_damage_base": "基础武器伤害",
    "weapon_damage_rand": "浮动武器伤害",
    "strain_base": "无双等级",
    "strain": "无双",
    "surplus": "破招",
}
MAGICAL_DISPLAY_ATTRS = {
    "base_magical_attack_power": "基础攻击",
    "magical_attack_power": "攻击",
    "base_magical_critical_strike": "会心等级",
    "magical_critical_strike": "会心",
    "magical_critical_power_base": "会效等级",
    "magical_critical_power": "会效",
    "base_magical_overcome": "基础破防",
    "final_magical_overcome": "最终破防",
    "magical_overcome": "破防",
    "weapon_damage_base": "基础武器伤害",
    "weapon_damage_rand": "浮动武器伤害",
    "strain_base": "无双等级",
    "strain": "无双",
    "surplus": "破招",
}
MIXING_DISPLAY_ATTRS = {
    "base_magical_attack_power": "基础攻击",
    "magical_attack_power": "攻击",
    "base_physical_critical_strike": "会心等级",
    "physical_critical_strike": "会心",
    "physical_critical_power_base": "会效等级",
    "physical_critical_power": "会效",
    "base_magical_overcome": "基础破防",
    "final_magical_overcome": "最终破防",
    "magical_overcome": "破防",
    "weapon_damage_base": "基础武器伤害",
    "weapon_damage_rand": "浮动武器伤害",
    "strain_base": "无双等级",
    "strain": "无双",
    "surplus": "破招",
}

SUPPORT_SCHOOL = {
    10015: School(
        school="纯阳", major="身法", kind="外功", attribute=tai_xu_jian_yi.TaiXuJianYi, formation="北斗七星阵",
        skills=tai_xu_jian_yi.SKILLS, buffs=tai_xu_jian_yi.BUFFS,
        talent_gains=tai_xu_jian_yi.TALENT_GAINS, talents=tai_xu_jian_yi.TALENTS,
        talent_decoder=tai_xu_jian_yi.TALENT_DECODER, talent_encoder=tai_xu_jian_yi.TALENT_ENCODER,
        recipe_gains=tai_xu_jian_yi.RECIPE_GAINS, recipes=tai_xu_jian_yi.RECIPES,
        gains=tai_xu_jian_yi.GAINS, display_attrs={"agility": "身法", **PHYSICAL_DISPLAY_ATTRS}
    ),
    10225: School(
        school="唐门", major="元气", kind="内功", attribute=tian_luo_gui_dao.TianLuoGuiDao, formation="千机百变阵",
        skills=tian_luo_gui_dao.SKILLS, buffs=tian_luo_gui_dao.BUFFS,
        talent_gains=tian_luo_gui_dao.TALENT_GAINS, talents=tian_luo_gui_dao.TALENTS,
        talent_decoder=tian_luo_gui_dao.TALENT_DECODER, talent_encoder=tian_luo_gui_dao.TALENT_ENCODER,
        recipe_gains=tian_luo_gui_dao.RECIPE_GAINS, recipes=tian_luo_gui_dao.RECIPES,
        gains=tian_luo_gui_dao.GAINS, display_attrs={"spunk": "元气", **MIXING_DISPLAY_ATTRS}
    ),
    10464: School(
        school="霸刀", major="力道", kind="外功", attribute=bei_ao_jue.BeiAoJue, formation="霜岚洗锋阵",
        skills=bei_ao_jue.SKILLS, buffs=bei_ao_jue.BUFFS,
        talent_gains=bei_ao_jue.TALENT_GAINS, talents=bei_ao_jue.TALENTS,
        talent_decoder=bei_ao_jue.TALENT_DECODER, talent_encoder=bei_ao_jue.TALENT_ENCODER,
        recipe_gains=bei_ao_jue.RECIPE_GAINS, recipes=bei_ao_jue.RECIPES,
        gains=bei_ao_jue.GAINS, display_attrs={"strength": "力道", **PHYSICAL_DISPLAY_ATTRS}
    ),
    10533: School(
        school="蓬莱", major="身法", kind="外功", attribute=ling_hai_jue.LingHaiJue, formation="墟海引归阵",
        skills=ling_hai_jue.SKILLS, buffs=ling_hai_jue.BUFFS,
        talent_gains=ling_hai_jue.TALENT_GAINS, talents=ling_hai_jue.TALENTS,
        talent_decoder=ling_hai_jue.TALENT_DECODER, talent_encoder=ling_hai_jue.TALENT_ENCODER,
        recipe_gains=ling_hai_jue.RECIPE_GAINS, recipes=ling_hai_jue.RECIPES,
        gains=ling_hai_jue.GAINS, display_attrs={"agility": "身法", **PHYSICAL_DISPLAY_ATTRS}
    ),
    10627: School(
        school="药宗", major="根骨", kind="内功", attribute=wu_fang.WuFang, formation="乱暮浊茵阵",
        skills=wu_fang.SKILLS, buffs=wu_fang.BUFFS,
        talent_gains=wu_fang.TALENT_GAINS, talents=wu_fang.TALENTS,
        talent_decoder=wu_fang.TALENT_DECODER, talent_encoder=wu_fang.TALENT_ENCODER,
        recipe_gains=wu_fang.RECIPE_GAINS, recipes=wu_fang.RECIPES,
        gains=wu_fang.GAINS, display_attrs={"spirit": "根骨", **MAGICAL_DISPLAY_ATTRS}
    ),
    10698: School(
        school="刀宗", major="力道", kind="外功", attribute=gu_feng_jue.GuFengJue, formation="横云破锋阵",
        skills=gu_feng_jue.SKILLS, buffs=gu_feng_jue.BUFFS,
        talent_gains=gu_feng_jue.TALENT_GAINS, talents=gu_feng_jue.TALENTS,
        talent_decoder=gu_feng_jue.TALENT_DECODER, talent_encoder=gu_feng_jue.TALENT_ENCODER,
        recipe_gains=gu_feng_jue.RECIPE_GAINS, recipes=gu_feng_jue.RECIPES,
        gains=gu_feng_jue.GAINS, display_attrs={"strength": "力道", **PHYSICAL_DISPLAY_ATTRS}
    ),
    10756: School(
        school="万灵", major="身法", kind="外功", attribute=shan_hai_xin_jue.ShanHaiXinJue, formation="苍梧引灵阵",
        skills=shan_hai_xin_jue.SKILLS, buffs=shan_hai_xin_jue.BUFFS,
        talent_gains=shan_hai_xin_jue.TALENT_GAINS, talents=shan_hai_xin_jue.TALENTS,
        talent_decoder=shan_hai_xin_jue.TALENT_DECODER, talent_encoder=shan_hai_xin_jue.TALENT_ENCODER,
        recipe_gains=shan_hai_xin_jue.RECIPE_GAINS, recipes=shan_hai_xin_jue.RECIPES,
        gains=shan_hai_xin_jue.GAINS, display_attrs={"agility": "身法", **PHYSICAL_DISPLAY_ATTRS}
    ),
}