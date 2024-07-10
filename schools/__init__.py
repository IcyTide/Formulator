from dataclasses import dataclass
from typing import Tuple, List, Dict, Type, Union, Callable

from base.attribute import Attribute
from base.buff import Buff
from base.gain import Gain
from base.skill import Skill, Dot
from base.talent import Talent
from schools import bei_ao_jue, gu_feng_jue, ao_xue_zhan_yi, jing_yu_jue, xiao_chen_jue
from schools import shan_hai_xin_jue, ling_hai_jue, tai_xu_jian_yi, fen_shan_jing, yin_long_jue, wen_shui_jue
from schools import wu_fang, bing_xin_jue, mo_wen, zi_xia_gong, du_jing
from schools import yi_jin_jing, tian_luo_gui_dao, hua_jian_you, tai_xuan_jing, fen_ying_sheng_jue


@dataclass
class School:
    id: int
    school: str
    major: str
    kind: str
    attribute: Type[Attribute]
    formation: str
    prepare: Callable
    skills: Dict[int, Skill]
    dots: Dict[int, Dot]
    buffs: Dict[int, Buff]
    talent_gains: Dict[int, Talent]
    talents: List[List[int]]
    talent_decoder: Dict[int, str]
    talent_encoder: Dict[str, int]
    recipe_gains: Dict[str, Dict[str, Gain]]
    recipes: Dict[str, List[str]]
    gains: Dict[Union[Tuple[int, int], int], Gain]
    display_attrs: Dict[str, str]

    platform: int = 0

    def attr_content(self, attribute):
        content = []
        for attr, name in self.display_attrs.items():
            value = getattr(attribute, attr)
            if isinstance(value, int):
                content.append([name, f"{value}"])
            else:
                content.append([name, f"{round(value * 100, 2)}%"])
        return content


GENERAL_DISPLAY_ATTRS = {
    "base_weapon_damage": "基础武器伤害",
    "weapon_damage_rand": "浮动武器伤害",
    "strain_base": "无双等级",
    "strain": "无双",
    "surplus": "破招",
}
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
    **GENERAL_DISPLAY_ATTRS
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
    **GENERAL_DISPLAY_ATTRS
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
    **GENERAL_DISPLAY_ATTRS
}

SUPPORT_SCHOOLS = {
    10003: School(
        id=10003, school="少林", major="元气", kind="内功", attribute=yi_jin_jing.YiJinJing, formation="天鼓雷音阵",
        skills=yi_jin_jing.SKILLS,  dots=yi_jin_jing.DOTS, buffs=yi_jin_jing.BUFFS, prepare=yi_jin_jing.prepare,
        talent_gains=yi_jin_jing.TALENT_GAINS, talents=yi_jin_jing.TALENTS,
        talent_decoder=yi_jin_jing.TALENT_DECODER, talent_encoder=yi_jin_jing.TALENT_ENCODER,
        recipe_gains=yi_jin_jing.RECIPE_GAINS, recipes=yi_jin_jing.RECIPES,
        gains=yi_jin_jing.GAINS, display_attrs={"spunk": "元气", **MAGICAL_DISPLAY_ATTRS}
    ),
    10014: School(
        id=10014, school="纯阳", major="根骨", kind="内功", attribute=zi_xia_gong.ZiXiaGong, formation="九宫八卦阵",
        skills=zi_xia_gong.SKILLS,  dots=zi_xia_gong.DOTS, buffs=zi_xia_gong.BUFFS, prepare=zi_xia_gong.prepare,
        talent_gains=zi_xia_gong.TALENT_GAINS, talents=zi_xia_gong.TALENTS,
        talent_decoder=zi_xia_gong.TALENT_DECODER, talent_encoder=zi_xia_gong.TALENT_ENCODER,
        recipe_gains=zi_xia_gong.RECIPE_GAINS, recipes=zi_xia_gong.RECIPES,
        gains=zi_xia_gong.GAINS, display_attrs={"spirit": "根骨", **MAGICAL_DISPLAY_ATTRS}
    ),
    10015: School(
        id=10015, school="纯阳", major="身法", kind="外功", attribute=tai_xu_jian_yi.TaiXuJianYi,
        formation="北斗七星阵",
        skills=tai_xu_jian_yi.SKILLS,  dots=tai_xu_jian_yi.DOTS, buffs=tai_xu_jian_yi.BUFFS, prepare=tai_xu_jian_yi.prepare,
        talent_gains=tai_xu_jian_yi.TALENT_GAINS, talents=tai_xu_jian_yi.TALENTS,
        talent_decoder=tai_xu_jian_yi.TALENT_DECODER, talent_encoder=tai_xu_jian_yi.TALENT_ENCODER,
        recipe_gains=tai_xu_jian_yi.RECIPE_GAINS, recipes=tai_xu_jian_yi.RECIPES,
        gains=tai_xu_jian_yi.GAINS, display_attrs={"agility": "身法", **PHYSICAL_DISPLAY_ATTRS}
    ),
    10021: School(
        id=10021, school="万花", major="元气", kind="内功", attribute=hua_jian_you.HuaJianYou, formation="七绝逍遥阵",
        skills=hua_jian_you.SKILLS,  dots=hua_jian_you.DOTS, buffs=hua_jian_you.BUFFS, prepare=hua_jian_you.prepare,
        talent_gains=hua_jian_you.TALENT_GAINS, talents=hua_jian_you.TALENTS,
        talent_decoder=hua_jian_you.TALENT_DECODER, talent_encoder=hua_jian_you.TALENT_ENCODER,
        recipe_gains=hua_jian_you.RECIPE_GAINS, recipes=hua_jian_you.RECIPES,
        gains=hua_jian_you.GAINS, display_attrs={"spunk": "元气", **MAGICAL_DISPLAY_ATTRS}
    ),
    10026: School(
        id=10026, school="天策", major="力道", kind="外功", attribute=ao_xue_zhan_yi.AoXueZhanYi,
        formation="卫公折冲阵",
        skills=ao_xue_zhan_yi.SKILLS,  dots=ao_xue_zhan_yi.DOTS, buffs=ao_xue_zhan_yi.BUFFS, prepare=ao_xue_zhan_yi.prepare,
        talent_gains=ao_xue_zhan_yi.TALENT_GAINS, talents=ao_xue_zhan_yi.TALENTS,
        talent_decoder=ao_xue_zhan_yi.TALENT_DECODER, talent_encoder=ao_xue_zhan_yi.TALENT_ENCODER,
        recipe_gains=ao_xue_zhan_yi.RECIPE_GAINS, recipes=ao_xue_zhan_yi.RECIPES,
        gains=ao_xue_zhan_yi.GAINS, display_attrs={"strength": "力道", **PHYSICAL_DISPLAY_ATTRS}
    ),
    10081: School(
        id=10081, school="七秀", major="根骨", kind="内功", attribute=bing_xin_jue.BingXinJue, formation="九音惊弦阵",
        skills=bing_xin_jue.SKILLS,  dots=bing_xin_jue.DOTS, buffs=bing_xin_jue.BUFFS, prepare=bing_xin_jue.prepare,
        talent_gains=bing_xin_jue.TALENT_GAINS, talents=bing_xin_jue.TALENTS,
        talent_decoder=bing_xin_jue.TALENT_DECODER, talent_encoder=bing_xin_jue.TALENT_ENCODER,
        recipe_gains=bing_xin_jue.RECIPE_GAINS, recipes=bing_xin_jue.RECIPES,
        gains=bing_xin_jue.GAINS, display_attrs={"spirit": "根骨", **MAGICAL_DISPLAY_ATTRS}
    ),
    10145: School(
        id=10145, school="藏剑", major="身法", kind="外功", attribute=wen_shui_jue.WenShuiJue,
        formation="依山观澜阵",
        skills=wen_shui_jue.SKILLS,  dots=wen_shui_jue.DOTS, buffs=wen_shui_jue.BUFFS, prepare=wen_shui_jue.prepare,
        talent_gains=wen_shui_jue.TALENT_GAINS, talents=wen_shui_jue.TALENTS,
        talent_decoder=wen_shui_jue.TALENT_DECODER, talent_encoder=wen_shui_jue.TALENT_ENCODER,
        recipe_gains=wen_shui_jue.RECIPE_GAINS, recipes=wen_shui_jue.RECIPES,
        gains=wen_shui_jue.GAINS, display_attrs={"agility": "身法", **PHYSICAL_DISPLAY_ATTRS}
    ),
    10175: School(
        id=10175, school="五毒", major="根骨", kind="内功", attribute=du_jing.DuJing, formation="万蛊噬心阵",
        skills=du_jing.SKILLS,  dots=du_jing.DOTS, buffs=du_jing.BUFFS, prepare=du_jing.prepare,
        talent_gains=du_jing.TALENT_GAINS, talents=du_jing.TALENTS,
        talent_decoder=du_jing.TALENT_DECODER, talent_encoder=du_jing.TALENT_ENCODER,
        recipe_gains=du_jing.RECIPE_GAINS, recipes=du_jing.RECIPES,
        gains=du_jing.GAINS, display_attrs={"spirit": "根骨", **MAGICAL_DISPLAY_ATTRS}
    ),
    10224: School(
        id=10224, school="唐门", major="力道", kind="外功", attribute=jing_yu_jue.JingYuJue, formation="流星赶月阵",
        skills=jing_yu_jue.SKILLS,  dots=jing_yu_jue.DOTS, buffs=jing_yu_jue.BUFFS, prepare=jing_yu_jue.prepare,
        talent_gains=jing_yu_jue.TALENT_GAINS, talents=jing_yu_jue.TALENTS,
        talent_decoder=jing_yu_jue.TALENT_DECODER, talent_encoder=jing_yu_jue.TALENT_ENCODER,
        recipe_gains=jing_yu_jue.RECIPE_GAINS, recipes=jing_yu_jue.RECIPES,
        gains=jing_yu_jue.GAINS, display_attrs={"strength": "力道", **PHYSICAL_DISPLAY_ATTRS}
    ),
    10225: School(
        id=10225, school="唐门", major="元气", kind="内功", attribute=tian_luo_gui_dao.TianLuoGuiDao,
        formation="千机百变阵",
        skills=tian_luo_gui_dao.SKILLS,  dots=tian_luo_gui_dao.DOTS, buffs=tian_luo_gui_dao.BUFFS, prepare=tian_luo_gui_dao.prepare,
        talent_gains=tian_luo_gui_dao.TALENT_GAINS, talents=tian_luo_gui_dao.TALENTS,
        talent_decoder=tian_luo_gui_dao.TALENT_DECODER, talent_encoder=tian_luo_gui_dao.TALENT_ENCODER,
        recipe_gains=tian_luo_gui_dao.RECIPE_GAINS, recipes=tian_luo_gui_dao.RECIPES,
        gains=tian_luo_gui_dao.GAINS, display_attrs={"spunk": "元气", **MIXING_DISPLAY_ATTRS}
    ),
    10242: School(
        id=10242, school="明教", major="元气", kind="内功", attribute=fen_ying_sheng_jue.FenYingShengJue,
        formation="炎威破魔阵",
        skills=fen_ying_sheng_jue.SKILLS,  dots=fen_ying_sheng_jue.DOTS, buffs=fen_ying_sheng_jue.BUFFS, prepare=fen_ying_sheng_jue.prepare,
        talent_gains=fen_ying_sheng_jue.TALENT_GAINS, talents=fen_ying_sheng_jue.TALENTS,
        talent_decoder=fen_ying_sheng_jue.TALENT_DECODER, talent_encoder=fen_ying_sheng_jue.TALENT_ENCODER,
        recipe_gains=fen_ying_sheng_jue.RECIPE_GAINS, recipes=fen_ying_sheng_jue.RECIPES,
        gains=fen_ying_sheng_jue.GAINS, display_attrs={"spunk": "元气", **MAGICAL_DISPLAY_ATTRS}
    ),
    10268: School(
        id=10268, school="丐帮", major="力道", kind="外功", attribute=xiao_chen_jue.XiaoChenJue, formation="降龙伏虎阵",
        skills=xiao_chen_jue.SKILLS,  dots=xiao_chen_jue.DOTS, buffs=xiao_chen_jue.BUFFS, prepare=xiao_chen_jue.prepare,
        talent_gains=xiao_chen_jue.TALENT_GAINS, talents=xiao_chen_jue.TALENTS,
        talent_decoder=xiao_chen_jue.TALENT_DECODER, talent_encoder=xiao_chen_jue.TALENT_ENCODER,
        recipe_gains=xiao_chen_jue.RECIPE_GAINS, recipes=xiao_chen_jue.RECIPES,
        gains=xiao_chen_jue.GAINS, display_attrs={"strength": "力道", **PHYSICAL_DISPLAY_ATTRS}
    ),
    10390: School(
        id=10390, school="苍云", major="身法", kind="外功", attribute=fen_shan_jing.FenShanJing, formation="锋凌横绝阵",
        skills=fen_shan_jing.SKILLS,  dots=fen_shan_jing.DOTS, buffs=fen_shan_jing.BUFFS, prepare=fen_shan_jing.prepare,
        talent_gains=fen_shan_jing.TALENT_GAINS, talents=fen_shan_jing.TALENTS,
        talent_decoder=fen_shan_jing.TALENT_DECODER, talent_encoder=fen_shan_jing.TALENT_ENCODER,
        recipe_gains=fen_shan_jing.RECIPE_GAINS, recipes=fen_shan_jing.RECIPES,
        gains=fen_shan_jing.GAINS, display_attrs={"agility": "身法", **PHYSICAL_DISPLAY_ATTRS}
    ),
    10447: School(
        id=10447, school="长歌", major="根骨", kind="内功", attribute=mo_wen.MoWen, formation="万籁金弦阵",
        skills=mo_wen.SKILLS,  dots=mo_wen.DOTS, buffs=mo_wen.BUFFS, prepare=mo_wen.prepare,
        talent_gains=mo_wen.TALENT_GAINS, talents=mo_wen.TALENTS,
        talent_decoder=mo_wen.TALENT_DECODER, talent_encoder=mo_wen.TALENT_ENCODER,
        recipe_gains=mo_wen.RECIPE_GAINS, recipes=mo_wen.RECIPES,
        gains=mo_wen.GAINS, display_attrs={"spirit": "根骨", **MAGICAL_DISPLAY_ATTRS}
    ),
    10464: School(
        id=10464, school="霸刀", major="力道", kind="外功", attribute=bei_ao_jue.BeiAoJue, formation="霜岚洗锋阵",
        skills=bei_ao_jue.SKILLS,  dots=bei_ao_jue.DOTS, buffs=bei_ao_jue.BUFFS, prepare=bei_ao_jue.prepare,
        talent_gains=bei_ao_jue.TALENT_GAINS, talents=bei_ao_jue.TALENTS,
        talent_decoder=bei_ao_jue.TALENT_DECODER, talent_encoder=bei_ao_jue.TALENT_ENCODER,
        recipe_gains=bei_ao_jue.RECIPE_GAINS, recipes=bei_ao_jue.RECIPES,
        gains=bei_ao_jue.GAINS, display_attrs={"strength": "力道", **PHYSICAL_DISPLAY_ATTRS}
    ),
    10533: School(
        id=10533, school="蓬莱", major="身法", kind="外功", attribute=ling_hai_jue.LingHaiJue, formation="墟海引归阵",
        skills=ling_hai_jue.SKILLS,  dots=ling_hai_jue.DOTS, buffs=ling_hai_jue.BUFFS, prepare=ling_hai_jue.prepare,
        talent_gains=ling_hai_jue.TALENT_GAINS, talents=ling_hai_jue.TALENTS,
        talent_decoder=ling_hai_jue.TALENT_DECODER, talent_encoder=ling_hai_jue.TALENT_ENCODER,
        recipe_gains=ling_hai_jue.RECIPE_GAINS, recipes=ling_hai_jue.RECIPES,
        gains=ling_hai_jue.GAINS, display_attrs={"agility": "身法", **PHYSICAL_DISPLAY_ATTRS}
    ),
    10585: School(
        id=10585, school="凌雪", major="身法", kind="外功", attribute=yin_long_jue.YinLongJue, formation="龙皇雪风阵",
        skills=yin_long_jue.SKILLS,  dots=yin_long_jue.DOTS, buffs=yin_long_jue.BUFFS, prepare=yin_long_jue.prepare,
        talent_gains=yin_long_jue.TALENT_GAINS, talents=yin_long_jue.TALENTS,
        talent_decoder=yin_long_jue.TALENT_DECODER, talent_encoder=yin_long_jue.TALENT_ENCODER,
        recipe_gains=yin_long_jue.RECIPE_GAINS, recipes=yin_long_jue.RECIPES,
        gains=yin_long_jue.GAINS, display_attrs={"agility": "身法", **PHYSICAL_DISPLAY_ATTRS}
    ),
    10615: School(
        id=10615, school="衍天", major="元气", kind="内功", attribute=tai_xuan_jing.TaiXuanJing, formation="九星游年阵",
        skills=tai_xuan_jing.SKILLS,  dots=tai_xuan_jing.DOTS, buffs=tai_xuan_jing.BUFFS, prepare=tai_xuan_jing.prepare,
        talent_gains=tai_xuan_jing.TALENT_GAINS, talents=tai_xuan_jing.TALENTS,
        talent_decoder=tai_xuan_jing.TALENT_DECODER, talent_encoder=tai_xuan_jing.TALENT_ENCODER,
        recipe_gains=tai_xuan_jing.RECIPE_GAINS, recipes=tai_xuan_jing.RECIPES,
        gains=tai_xuan_jing.GAINS, display_attrs={"spunk": "元气", **MAGICAL_DISPLAY_ATTRS}
    ),
    10627: School(
        id=10627, school="药宗", major="根骨", kind="内功", attribute=wu_fang.WuFang, formation="乱暮浊茵阵",
        skills=wu_fang.SKILLS,  dots=wu_fang.DOTS, buffs=wu_fang.BUFFS, prepare=wu_fang.prepare,
        talent_gains=wu_fang.TALENT_GAINS, talents=wu_fang.TALENTS,
        talent_decoder=wu_fang.TALENT_DECODER, talent_encoder=wu_fang.TALENT_ENCODER,
        recipe_gains=wu_fang.RECIPE_GAINS, recipes=wu_fang.RECIPES,
        gains=wu_fang.GAINS, display_attrs={"spirit": "根骨", **MAGICAL_DISPLAY_ATTRS}
    ),
    10698: School(
        id=10698, school="刀宗", major="力道", kind="外功", attribute=gu_feng_jue.GuFengJue, formation="横云破锋阵",
        skills=gu_feng_jue.SKILLS,  dots=gu_feng_jue.DOTS, buffs=gu_feng_jue.BUFFS, prepare=gu_feng_jue.prepare,
        talent_gains=gu_feng_jue.TALENT_GAINS, talents=gu_feng_jue.TALENTS,
        talent_decoder=gu_feng_jue.TALENT_DECODER, talent_encoder=gu_feng_jue.TALENT_ENCODER,
        recipe_gains=gu_feng_jue.RECIPE_GAINS, recipes=gu_feng_jue.RECIPES,
        gains=gu_feng_jue.GAINS, display_attrs={"strength": "力道", **PHYSICAL_DISPLAY_ATTRS}
    ),
    10756: School(
        id=10756, school="万灵", major="身法", kind="外功", attribute=shan_hai_xin_jue.ShanHaiXinJue,
        formation="苍梧引灵阵",
        skills=shan_hai_xin_jue.SKILLS,  dots=shan_hai_xin_jue.DOTS, buffs=shan_hai_xin_jue.BUFFS, prepare=shan_hai_xin_jue.prepare,
        talent_gains=shan_hai_xin_jue.TALENT_GAINS, talents=shan_hai_xin_jue.TALENTS,
        talent_decoder=shan_hai_xin_jue.TALENT_DECODER, talent_encoder=shan_hai_xin_jue.TALENT_ENCODER,
        recipe_gains=shan_hai_xin_jue.RECIPE_GAINS, recipes=shan_hai_xin_jue.RECIPES,
        gains=shan_hai_xin_jue.GAINS, display_attrs={"agility": "身法", **PHYSICAL_DISPLAY_ATTRS}
    ),
}
