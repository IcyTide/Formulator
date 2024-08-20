from dataclasses import dataclass
from typing import Tuple, List, Dict, Type, Callable

from base.attribute import Attribute
from base.buff import Buff
from base.dot import Dot
from base.gain import Gain
from base.recipe import Recipe
from base.skill import Skill
from schools import ao_xue_zhan_yi, jing_yu_jue, xiao_chen_jue, bei_ao_jue, gu_feng_jue
from schools import tai_xu_jian_yi, wen_shui_jue, fen_shan_jing, ling_hai_jue, yin_long_jue, shan_hai_xin_jue
from schools import yi_jin_jing, hua_jian_you, tian_luo_gui_dao, fen_ying_sheng_jue, tai_xuan_jing
from schools import zi_xia_gong, bing_xin_jue, du_jing, mo_wen, wu_fang


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
    talents: Dict[int, Gain]
    talent_choices: List[List[int]]
    talent_decoder: Dict[int, str]
    talent_encoder: Dict[str, int]
    recipes: Dict[Tuple[int, int], Recipe]
    recipe_choices: Dict[str, Dict[str, Tuple[int, int]]]
    gains: Dict[tuple, Gain]

    platform: int = 0


SUPPORT_SCHOOLS = {
    10003: School(
        id=10003, school="少林", major="元气", kind="内功", attribute=yi_jin_jing.Attribute, formation="天鼓雷音阵",
        skills=yi_jin_jing.SKILLS, dots=yi_jin_jing.DOTS, buffs=yi_jin_jing.BUFFS,
        prepare=yi_jin_jing.prepare,
        talents=yi_jin_jing.TALENTS, talent_choices=yi_jin_jing.TALENT_CHOICES,
        talent_decoder=yi_jin_jing.TALENT_DECODER, talent_encoder=yi_jin_jing.TALENT_ENCODER,
        recipes=yi_jin_jing.RECIPES, recipe_choices=yi_jin_jing.RECIPE_CHOICES,
        gains=yi_jin_jing.GAINS,
    ),
    10014: School(
        id=10014, school="纯阳", major="根骨", kind="内功", attribute=zi_xia_gong.Attribute, formation="九宫八卦阵",
        skills=zi_xia_gong.SKILLS, dots=zi_xia_gong.DOTS, buffs=zi_xia_gong.BUFFS,
        prepare=zi_xia_gong.prepare,
        talents=zi_xia_gong.TALENTS, talent_choices=zi_xia_gong.TALENT_CHOICES,
        talent_decoder=zi_xia_gong.TALENT_DECODER, talent_encoder=zi_xia_gong.TALENT_ENCODER,
        recipes=zi_xia_gong.RECIPES, recipe_choices=zi_xia_gong.RECIPE_CHOICES,
        gains=zi_xia_gong.GAINS,
    ),
    10015: School(
        id=10015, school="纯阳", major="身法", kind="外功", attribute=tai_xu_jian_yi.Attribute, formation="北斗七星阵",
        skills=tai_xu_jian_yi.SKILLS, dots=tai_xu_jian_yi.DOTS, buffs=tai_xu_jian_yi.BUFFS,
        prepare=tai_xu_jian_yi.prepare,
        talents=tai_xu_jian_yi.TALENTS, talent_choices=tai_xu_jian_yi.TALENT_CHOICES,
        talent_decoder=tai_xu_jian_yi.TALENT_DECODER, talent_encoder=tai_xu_jian_yi.TALENT_ENCODER,
        recipes=tai_xu_jian_yi.RECIPES, recipe_choices=tai_xu_jian_yi.RECIPE_CHOICES,
        gains=tai_xu_jian_yi.GAINS,
    ),
    10021: School(
        id=10021, school="万花", major="元气", kind="内功", attribute=hua_jian_you.Attribute, formation="七绝逍遥阵",
        skills=hua_jian_you.SKILLS, dots=hua_jian_you.DOTS, buffs=hua_jian_you.BUFFS,
        prepare=hua_jian_you.prepare,
        talents=hua_jian_you.TALENTS, talent_choices=hua_jian_you.TALENT_CHOICES,
        talent_decoder=hua_jian_you.TALENT_DECODER, talent_encoder=hua_jian_you.TALENT_ENCODER,
        recipes=hua_jian_you.RECIPES, recipe_choices=hua_jian_you.RECIPE_CHOICES,
        gains=hua_jian_you.GAINS,
    ),
    10026: School(
        id=10026, school="天策", major="力道", kind="外功", attribute=ao_xue_zhan_yi.Attribute, formation="卫公折冲阵",
        skills=ao_xue_zhan_yi.SKILLS, dots=ao_xue_zhan_yi.DOTS, buffs=ao_xue_zhan_yi.BUFFS,
        prepare=ao_xue_zhan_yi.prepare,
        talents=ao_xue_zhan_yi.TALENTS, talent_choices=ao_xue_zhan_yi.TALENT_CHOICES,
        talent_decoder=ao_xue_zhan_yi.TALENT_DECODER, talent_encoder=ao_xue_zhan_yi.TALENT_ENCODER,
        recipes=ao_xue_zhan_yi.RECIPES, recipe_choices=ao_xue_zhan_yi.RECIPE_CHOICES,
        gains=ao_xue_zhan_yi.GAINS,
    ),
    10081: School(
        id=10081, school="七秀", major="根骨", kind="内功", attribute=bing_xin_jue.Attribute, formation="九音惊弦阵",
        skills=bing_xin_jue.SKILLS, dots=bing_xin_jue.DOTS, buffs=bing_xin_jue.BUFFS,
        prepare=bing_xin_jue.prepare,
        talents=bing_xin_jue.TALENTS, talent_choices=bing_xin_jue.TALENT_CHOICES,
        talent_decoder=bing_xin_jue.TALENT_DECODER, talent_encoder=bing_xin_jue.TALENT_ENCODER,
        recipes=bing_xin_jue.RECIPES, recipe_choices=bing_xin_jue.RECIPE_CHOICES,
        gains=bing_xin_jue.GAINS,
    ),
    10145: School(
        id=10145, school="藏剑", major="身法", kind="外功", attribute=wen_shui_jue.Attribute, formation="依山观澜阵",
        skills=wen_shui_jue.SKILLS, dots=wen_shui_jue.DOTS, buffs=wen_shui_jue.BUFFS,
        prepare=wen_shui_jue.prepare,
        talents=wen_shui_jue.TALENTS, talent_choices=wen_shui_jue.TALENT_CHOICES,
        talent_decoder=wen_shui_jue.TALENT_DECODER, talent_encoder=wen_shui_jue.TALENT_ENCODER,
        recipes=wen_shui_jue.RECIPES, recipe_choices=wen_shui_jue.RECIPE_CHOICES,
        gains=wen_shui_jue.GAINS,
    ),
    10175: School(
        id=10175, school="五毒", major="根骨", kind="内功", attribute=du_jing.Attribute, formation="万蛊噬心阵",
        skills=du_jing.SKILLS, dots=du_jing.DOTS, buffs=du_jing.BUFFS,
        prepare=du_jing.prepare,
        talents=du_jing.TALENTS, talent_choices=du_jing.TALENT_CHOICES,
        talent_decoder=du_jing.TALENT_DECODER, talent_encoder=du_jing.TALENT_ENCODER,
        recipes=du_jing.RECIPES, recipe_choices=du_jing.RECIPE_CHOICES,
        gains=du_jing.GAINS,
    ),
    10224: School(
        id=10224, school="唐门", major="力道", kind="外功", attribute=jing_yu_jue.Attribute, formation="流星赶月阵",
        skills=jing_yu_jue.SKILLS, dots=jing_yu_jue.DOTS, buffs=jing_yu_jue.BUFFS,
        prepare=jing_yu_jue.prepare,
        talents=jing_yu_jue.TALENTS, talent_choices=jing_yu_jue.TALENT_CHOICES,
        talent_decoder=jing_yu_jue.TALENT_DECODER, talent_encoder=jing_yu_jue.TALENT_ENCODER,
        recipes=jing_yu_jue.RECIPES, recipe_choices=jing_yu_jue.RECIPE_CHOICES,
        gains=jing_yu_jue.GAINS,
    ),
    10225: School(
        id=10225, school="唐门", major="元气", kind="内功", attribute=tian_luo_gui_dao.Attribute,
        formation="千机百变阵",
        skills=tian_luo_gui_dao.SKILLS, dots=tian_luo_gui_dao.DOTS, buffs=tian_luo_gui_dao.BUFFS,
        prepare=tian_luo_gui_dao.prepare,
        talents=tian_luo_gui_dao.TALENTS, talent_choices=tian_luo_gui_dao.TALENT_CHOICES,
        talent_decoder=tian_luo_gui_dao.TALENT_DECODER, talent_encoder=tian_luo_gui_dao.TALENT_ENCODER,
        recipes=tian_luo_gui_dao.RECIPES, recipe_choices=tian_luo_gui_dao.RECIPE_CHOICES,
        gains=tian_luo_gui_dao.GAINS,
    ),
    10242: School(
        id=10242, school="明教", major="元气", kind="内功", attribute=fen_ying_sheng_jue.Attribute,
        formation="炎威破魔阵",
        prepare=fen_ying_sheng_jue.prepare,
        skills=fen_ying_sheng_jue.SKILLS, dots=fen_ying_sheng_jue.DOTS, buffs=fen_ying_sheng_jue.BUFFS,
        talents=fen_ying_sheng_jue.TALENTS, talent_choices=fen_ying_sheng_jue.TALENT_CHOICES,
        talent_decoder=fen_ying_sheng_jue.TALENT_DECODER, talent_encoder=fen_ying_sheng_jue.TALENT_ENCODER,
        recipes=fen_ying_sheng_jue.RECIPES, recipe_choices=fen_ying_sheng_jue.RECIPE_CHOICES,
        gains=fen_ying_sheng_jue.GAINS,
    ),
    10268: School(
        id=10268, school="丐帮", major="力道", kind="外功", attribute=xiao_chen_jue.Attribute, formation="降龙伏虎阵",
        skills=xiao_chen_jue.SKILLS, dots=xiao_chen_jue.DOTS, buffs=xiao_chen_jue.BUFFS,
        prepare=xiao_chen_jue.prepare,
        talents=xiao_chen_jue.TALENTS, talent_choices=xiao_chen_jue.TALENT_CHOICES,
        talent_decoder=xiao_chen_jue.TALENT_DECODER, talent_encoder=xiao_chen_jue.TALENT_ENCODER,
        recipes=xiao_chen_jue.RECIPES, recipe_choices=xiao_chen_jue.RECIPE_CHOICES,
        gains=xiao_chen_jue.GAINS,
    ),
    10390: School(
        id=10390, school="苍云", major="身法", kind="外功", attribute=fen_shan_jing.Attribute, formation="锋凌横绝阵",
        skills=fen_shan_jing.SKILLS, dots=fen_shan_jing.DOTS, buffs=fen_shan_jing.BUFFS,
        prepare=fen_shan_jing.prepare,
        talents=fen_shan_jing.TALENTS, talent_choices=fen_shan_jing.TALENT_CHOICES,
        talent_decoder=fen_shan_jing.TALENT_DECODER, talent_encoder=fen_shan_jing.TALENT_ENCODER,
        recipes=fen_shan_jing.RECIPES, recipe_choices=fen_shan_jing.RECIPE_CHOICES,
        gains=fen_shan_jing.GAINS,
    ),
    10447: School(
        id=10447, school="长歌", major="根骨", kind="内功", attribute=mo_wen.Attribute, formation="万籁金弦阵",
        skills=mo_wen.SKILLS, dots=mo_wen.DOTS, buffs=mo_wen.BUFFS,
        prepare=mo_wen.prepare,
        talents=mo_wen.TALENTS, talent_choices=mo_wen.TALENT_CHOICES,
        talent_decoder=mo_wen.TALENT_DECODER, talent_encoder=mo_wen.TALENT_ENCODER,
        recipes=mo_wen.RECIPES, recipe_choices=mo_wen.RECIPE_CHOICES,
        gains=mo_wen.GAINS,
    ),
    10464: School(
        id=10464, school="霸刀", major="力道", kind="外功", attribute=bei_ao_jue.Attribute, formation="霜岚洗锋阵",
        skills=bei_ao_jue.SKILLS, dots=bei_ao_jue.DOTS, buffs=bei_ao_jue.BUFFS,
        prepare=bei_ao_jue.prepare,
        talents=bei_ao_jue.TALENTS, talent_choices=bei_ao_jue.TALENT_CHOICES,
        talent_decoder=bei_ao_jue.TALENT_DECODER, talent_encoder=bei_ao_jue.TALENT_ENCODER,
        recipes=bei_ao_jue.RECIPES, recipe_choices=bei_ao_jue.RECIPE_CHOICES,
        gains=bei_ao_jue.GAINS,
    ),
    10533: School(
        id=10533, school="蓬莱", major="身法", kind="外功", attribute=ling_hai_jue.Attribute, formation="墟海引归阵",
        skills=ling_hai_jue.SKILLS, dots=ling_hai_jue.DOTS, buffs=ling_hai_jue.BUFFS,
        prepare=ling_hai_jue.prepare,
        talents=ling_hai_jue.TALENTS, talent_choices=ling_hai_jue.TALENT_CHOICES,
        talent_decoder=ling_hai_jue.TALENT_DECODER, talent_encoder=ling_hai_jue.TALENT_ENCODER,
        recipes=ling_hai_jue.RECIPES, recipe_choices=ling_hai_jue.RECIPE_CHOICES,
        gains=ling_hai_jue.GAINS,
    ),
    10585: School(
        id=10585, school="凌雪", major="身法", kind="外功", attribute=yin_long_jue.Attribute, formation="龙皇雪风阵",
        skills=yin_long_jue.SKILLS, dots=yin_long_jue.DOTS, buffs=yin_long_jue.BUFFS,
        prepare=yin_long_jue.prepare,
        talents=yin_long_jue.TALENTS, talent_choices=yin_long_jue.TALENT_CHOICES,
        talent_decoder=yin_long_jue.TALENT_DECODER, talent_encoder=yin_long_jue.TALENT_ENCODER,
        recipes=yin_long_jue.RECIPES, recipe_choices=yin_long_jue.RECIPE_CHOICES,
        gains=yin_long_jue.GAINS,
    ),
    10615: School(
        id=10615, school="衍天", major="元气", kind="内功", attribute=tai_xuan_jing.Attribute, formation="九星游年阵",
        skills=tai_xuan_jing.SKILLS, dots=tai_xuan_jing.DOTS, buffs=tai_xuan_jing.BUFFS,
        prepare=tai_xuan_jing.prepare,
        talents=tai_xuan_jing.TALENTS, talent_choices=tai_xuan_jing.TALENT_CHOICES,
        talent_decoder=tai_xuan_jing.TALENT_DECODER, talent_encoder=tai_xuan_jing.TALENT_ENCODER,
        recipes=tai_xuan_jing.RECIPES, recipe_choices=tai_xuan_jing.RECIPE_CHOICES,
        gains=tai_xuan_jing.GAINS,
    ),
    10627: School(
        id=10627, school="药宗", major="根骨", kind="内功", attribute=wu_fang.Attribute, formation="乱暮浊茵阵",
        skills=wu_fang.SKILLS, dots=wu_fang.DOTS, buffs=wu_fang.BUFFS,
        prepare=wu_fang.prepare,
        talents=wu_fang.TALENTS, talent_choices=wu_fang.TALENT_CHOICES,
        talent_decoder=wu_fang.TALENT_DECODER, talent_encoder=wu_fang.TALENT_ENCODER,
        recipes=wu_fang.RECIPES, recipe_choices=wu_fang.RECIPE_CHOICES,
        gains=wu_fang.GAINS,
    ),
    10698: School(
        id=10698, school="刀宗", major="力道", kind="外功", attribute=gu_feng_jue.Attribute, formation="横云破锋阵",
        skills=gu_feng_jue.SKILLS, dots=gu_feng_jue.DOTS, buffs=gu_feng_jue.BUFFS,
        prepare=gu_feng_jue.prepare,
        talents=gu_feng_jue.TALENTS, talent_choices=gu_feng_jue.TALENT_CHOICES,
        talent_decoder=gu_feng_jue.TALENT_DECODER, talent_encoder=gu_feng_jue.TALENT_ENCODER,
        recipes=gu_feng_jue.RECIPES, recipe_choices=gu_feng_jue.RECIPE_CHOICES,
        gains=gu_feng_jue.GAINS,
    ),
    10756: School(
        id=10756, school="万灵", major="身法", kind="外功", attribute=shan_hai_xin_jue.Attribute,
        formation="苍梧引灵阵",
        skills=shan_hai_xin_jue.SKILLS, dots=shan_hai_xin_jue.DOTS, buffs=shan_hai_xin_jue.BUFFS,
        prepare=shan_hai_xin_jue.prepare,
        talents=shan_hai_xin_jue.TALENTS, talent_choices=shan_hai_xin_jue.TALENT_CHOICES,
        talent_decoder=shan_hai_xin_jue.TALENT_DECODER, talent_encoder=shan_hai_xin_jue.TALENT_ENCODER,
        recipes=shan_hai_xin_jue.RECIPES, recipe_choices=shan_hai_xin_jue.RECIPE_CHOICES,
        gains=shan_hai_xin_jue.GAINS,
    ),
}
