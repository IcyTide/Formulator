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
from schools import yi_jin_jing, hua_jian_you, tian_luo_gui_dao, fen_ying_sheng_jue, tai_xuan_jing, zhou_tian_gong
from schools import zi_xia_gong, bing_xin_jue, du_jing, mo_wen, wu_fang


@dataclass
class School:
    id: int
    name: str
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
    recipes: Dict[Tuple[int, int], Recipe]
    recipe_choices: Dict[str, Dict[str, Tuple[int, int]]]
    gains: Dict[tuple, Gain]

    platform: int = 0

    def __post_init__(self):
        self.talent_decoder = {talent_id: talent.gain_name for talent_id, talent in self.talents.items()}
        self.talent_encoder = {v: k for k, v in self.talent_decoder.items()}


SUPPORT_SCHOOLS = {
    10003: School(
        id=10003, name="易筋经", school="少林", major="元气", kind="内功", attribute=yi_jin_jing.Attribute,
        formation="天鼓雷音阵", prepare=yi_jin_jing.prepare,
        skills=yi_jin_jing.SKILLS, dots=yi_jin_jing.DOTS, buffs=yi_jin_jing.BUFFS,
        talents=yi_jin_jing.TALENTS, talent_choices=yi_jin_jing.TALENT_CHOICES,
        recipes=yi_jin_jing.RECIPES, recipe_choices=yi_jin_jing.RECIPE_CHOICES,
        gains=yi_jin_jing.GAINS,
    ),
    10014: School(
        id=10014, name="紫霞功", school="纯阳", major="根骨", kind="内功", attribute=zi_xia_gong.Attribute,
        formation="九宫八卦阵", prepare=zi_xia_gong.prepare,
        skills=zi_xia_gong.SKILLS, dots=zi_xia_gong.DOTS, buffs=zi_xia_gong.BUFFS,
        talents=zi_xia_gong.TALENTS, talent_choices=zi_xia_gong.TALENT_CHOICES,
        recipes=zi_xia_gong.RECIPES, recipe_choices=zi_xia_gong.RECIPE_CHOICES,
        gains=zi_xia_gong.GAINS,
    ),
    10015: School(
        id=10015, name="太虚剑意", school="纯阳", major="身法", kind="外功", attribute=tai_xu_jian_yi.Attribute,
        formation="北斗七星阵", prepare=tai_xu_jian_yi.prepare,
        skills=tai_xu_jian_yi.SKILLS, dots=tai_xu_jian_yi.DOTS, buffs=tai_xu_jian_yi.BUFFS,
        talents=tai_xu_jian_yi.TALENTS, talent_choices=tai_xu_jian_yi.TALENT_CHOICES,
        recipes=tai_xu_jian_yi.RECIPES, recipe_choices=tai_xu_jian_yi.RECIPE_CHOICES,
        gains=tai_xu_jian_yi.GAINS,
    ),
    10021: School(
        id=10021, name="花间游", school="万花", major="元气", kind="内功", attribute=hua_jian_you.Attribute,
        formation="七绝逍遥阵", prepare=hua_jian_you.prepare,
        skills=hua_jian_you.SKILLS, dots=hua_jian_you.DOTS, buffs=hua_jian_you.BUFFS,
        talents=hua_jian_you.TALENTS, talent_choices=hua_jian_you.TALENT_CHOICES,
        recipes=hua_jian_you.RECIPES, recipe_choices=hua_jian_you.RECIPE_CHOICES,
        gains=hua_jian_you.GAINS,
    ),
    10026: School(
        id=10026, name="傲血战意", school="天策", major="力道", kind="外功", attribute=ao_xue_zhan_yi.Attribute,
        formation="卫公折冲阵", prepare=ao_xue_zhan_yi.prepare,
        skills=ao_xue_zhan_yi.SKILLS, dots=ao_xue_zhan_yi.DOTS, buffs=ao_xue_zhan_yi.BUFFS,
        talents=ao_xue_zhan_yi.TALENTS, talent_choices=ao_xue_zhan_yi.TALENT_CHOICES,
        recipes=ao_xue_zhan_yi.RECIPES, recipe_choices=ao_xue_zhan_yi.RECIPE_CHOICES,
        gains=ao_xue_zhan_yi.GAINS,
    ),
    10081: School(
        id=10081, name="冰心诀", school="七秀", major="根骨", kind="内功", attribute=bing_xin_jue.Attribute,
        formation="九音惊弦阵", prepare=bing_xin_jue.prepare,
        skills=bing_xin_jue.SKILLS, dots=bing_xin_jue.DOTS, buffs=bing_xin_jue.BUFFS,
        talents=bing_xin_jue.TALENTS, talent_choices=bing_xin_jue.TALENT_CHOICES,
        recipes=bing_xin_jue.RECIPES, recipe_choices=bing_xin_jue.RECIPE_CHOICES,
        gains=bing_xin_jue.GAINS,
    ),
    10145: School(
        id=10145, name="问水诀", school="藏剑", major="身法", kind="外功", attribute=wen_shui_jue.Attribute,
        formation="依山观澜阵", prepare=wen_shui_jue.prepare,
        skills=wen_shui_jue.SKILLS, dots=wen_shui_jue.DOTS, buffs=wen_shui_jue.BUFFS,
        talents=wen_shui_jue.TALENTS, talent_choices=wen_shui_jue.TALENT_CHOICES,
        recipes=wen_shui_jue.RECIPES, recipe_choices=wen_shui_jue.RECIPE_CHOICES,
        gains=wen_shui_jue.GAINS,
    ),
    10175: School(
        id=10175, name="毒经", school="五毒", major="根骨", kind="内功", attribute=du_jing.Attribute,
        formation="万蛊噬心阵", prepare=du_jing.prepare,
        skills=du_jing.SKILLS, dots=du_jing.DOTS, buffs=du_jing.BUFFS,
        talents=du_jing.TALENTS, talent_choices=du_jing.TALENT_CHOICES,
        recipes=du_jing.RECIPES, recipe_choices=du_jing.RECIPE_CHOICES,
        gains=du_jing.GAINS,
    ),
    10224: School(
        id=10224, name="惊羽诀", school="唐门", major="力道", kind="外功", attribute=jing_yu_jue.Attribute,
        formation="流星赶月阵", prepare=jing_yu_jue.prepare,
        skills=jing_yu_jue.SKILLS, dots=jing_yu_jue.DOTS, buffs=jing_yu_jue.BUFFS,
        talents=jing_yu_jue.TALENTS, talent_choices=jing_yu_jue.TALENT_CHOICES,
        recipes=jing_yu_jue.RECIPES, recipe_choices=jing_yu_jue.RECIPE_CHOICES,
        gains=jing_yu_jue.GAINS,
    ),
    10225: School(
        id=10225, name="天罗诡道", school="唐门", major="元气", kind="内功", attribute=tian_luo_gui_dao.Attribute,
        formation="千机百变阵", prepare=tian_luo_gui_dao.prepare,
        skills=tian_luo_gui_dao.SKILLS, dots=tian_luo_gui_dao.DOTS, buffs=tian_luo_gui_dao.BUFFS,
        talents=tian_luo_gui_dao.TALENTS, talent_choices=tian_luo_gui_dao.TALENT_CHOICES,
        recipes=tian_luo_gui_dao.RECIPES, recipe_choices=tian_luo_gui_dao.RECIPE_CHOICES,
        gains=tian_luo_gui_dao.GAINS,
    ),
    10242: School(
        id=10242, name="焚影圣诀", school="明教", major="元气", kind="内功", attribute=fen_ying_sheng_jue.Attribute,
        formation="炎威破魔阵", prepare=fen_ying_sheng_jue.prepare,
        skills=fen_ying_sheng_jue.SKILLS, dots=fen_ying_sheng_jue.DOTS, buffs=fen_ying_sheng_jue.BUFFS,
        talents=fen_ying_sheng_jue.TALENTS, talent_choices=fen_ying_sheng_jue.TALENT_CHOICES,
        recipes=fen_ying_sheng_jue.RECIPES, recipe_choices=fen_ying_sheng_jue.RECIPE_CHOICES,
        gains=fen_ying_sheng_jue.GAINS,
    ),
    10268: School(
        id=10268, name="笑尘诀", school="丐帮", major="力道", kind="外功", attribute=xiao_chen_jue.Attribute,
        formation="降龙伏虎阵", prepare=xiao_chen_jue.prepare,
        skills=xiao_chen_jue.SKILLS, dots=xiao_chen_jue.DOTS, buffs=xiao_chen_jue.BUFFS,
        talents=xiao_chen_jue.TALENTS, talent_choices=xiao_chen_jue.TALENT_CHOICES,
        recipes=xiao_chen_jue.RECIPES, recipe_choices=xiao_chen_jue.RECIPE_CHOICES,
        gains=xiao_chen_jue.GAINS,
    ),
    10390: School(
        id=10390, name="分山劲", school="苍云", major="身法", kind="外功", attribute=fen_shan_jing.Attribute,
        formation="锋凌横绝阵", prepare=fen_shan_jing.prepare,
        skills=fen_shan_jing.SKILLS, dots=fen_shan_jing.DOTS, buffs=fen_shan_jing.BUFFS,
        talents=fen_shan_jing.TALENTS, talent_choices=fen_shan_jing.TALENT_CHOICES,
        recipes=fen_shan_jing.RECIPES, recipe_choices=fen_shan_jing.RECIPE_CHOICES,
        gains=fen_shan_jing.GAINS,
    ),
    10447: School(
        id=10447, name="莫问", school="长歌", major="根骨", kind="内功", attribute=mo_wen.Attribute,
        formation="万籁金弦阵", prepare=mo_wen.prepare,
        skills=mo_wen.SKILLS, dots=mo_wen.DOTS, buffs=mo_wen.BUFFS,
        talents=mo_wen.TALENTS, talent_choices=mo_wen.TALENT_CHOICES,
        recipes=mo_wen.RECIPES, recipe_choices=mo_wen.RECIPE_CHOICES,
        gains=mo_wen.GAINS,
    ),
    10464: School(
        id=10464, name="北傲诀", school="霸刀", major="力道", kind="外功", attribute=bei_ao_jue.Attribute,
        formation="霜岚洗锋阵", prepare=bei_ao_jue.prepare,
        skills=bei_ao_jue.SKILLS, dots=bei_ao_jue.DOTS, buffs=bei_ao_jue.BUFFS,
        talents=bei_ao_jue.TALENTS, talent_choices=bei_ao_jue.TALENT_CHOICES,
        recipes=bei_ao_jue.RECIPES, recipe_choices=bei_ao_jue.RECIPE_CHOICES,
        gains=bei_ao_jue.GAINS,
    ),
    10533: School(
        id=10533, name="凌海诀", school="蓬莱", major="身法", kind="外功", attribute=ling_hai_jue.Attribute,
        formation="墟海引归阵", prepare=ling_hai_jue.prepare,
        skills=ling_hai_jue.SKILLS, dots=ling_hai_jue.DOTS, buffs=ling_hai_jue.BUFFS,
        talents=ling_hai_jue.TALENTS, talent_choices=ling_hai_jue.TALENT_CHOICES,
        recipes=ling_hai_jue.RECIPES, recipe_choices=ling_hai_jue.RECIPE_CHOICES,
        gains=ling_hai_jue.GAINS,
    ),
    10585: School(
        id=10585, name="隐龙诀", school="凌雪", major="身法", kind="外功", attribute=yin_long_jue.Attribute,
        formation="龙皇雪风阵", prepare=yin_long_jue.prepare,
        skills=yin_long_jue.SKILLS, dots=yin_long_jue.DOTS, buffs=yin_long_jue.BUFFS,
        talents=yin_long_jue.TALENTS, talent_choices=yin_long_jue.TALENT_CHOICES,
        recipes=yin_long_jue.RECIPES, recipe_choices=yin_long_jue.RECIPE_CHOICES,
        gains=yin_long_jue.GAINS,
    ),
    10615: School(
        id=10615, name="太玄经", school="衍天", major="元气", kind="内功", attribute=tai_xuan_jing.Attribute,
        formation="九星游年阵", prepare=tai_xuan_jing.prepare,
        skills=tai_xuan_jing.SKILLS, dots=tai_xuan_jing.DOTS, buffs=tai_xuan_jing.BUFFS,
        talents=tai_xuan_jing.TALENTS, talent_choices=tai_xuan_jing.TALENT_CHOICES,
        recipes=tai_xuan_jing.RECIPES, recipe_choices=tai_xuan_jing.RECIPE_CHOICES,
        gains=tai_xuan_jing.GAINS,
    ),
    10627: School(
        id=10627, name="无方", school="药宗", major="根骨", kind="内功", attribute=wu_fang.Attribute,
        formation="乱暮浊茵阵", prepare=wu_fang.prepare,
        skills=wu_fang.SKILLS, dots=wu_fang.DOTS, buffs=wu_fang.BUFFS,
        talents=wu_fang.TALENTS, talent_choices=wu_fang.TALENT_CHOICES,
        recipes=wu_fang.RECIPES, recipe_choices=wu_fang.RECIPE_CHOICES,
        gains=wu_fang.GAINS,
    ),
    10698: School(
        id=10698, name="孤锋诀", school="刀宗", major="力道", kind="外功", attribute=gu_feng_jue.Attribute,
        formation="横云破锋阵", prepare=gu_feng_jue.prepare,
        skills=gu_feng_jue.SKILLS, dots=gu_feng_jue.DOTS, buffs=gu_feng_jue.BUFFS,
        talents=gu_feng_jue.TALENTS, talent_choices=gu_feng_jue.TALENT_CHOICES,
        recipes=gu_feng_jue.RECIPES, recipe_choices=gu_feng_jue.RECIPE_CHOICES,
        gains=gu_feng_jue.GAINS,
    ),
    10756: School(
        id=10756, name="山海心诀", school="万灵", major="身法", kind="外功", attribute=shan_hai_xin_jue.Attribute,
        formation="苍梧引灵阵", prepare=shan_hai_xin_jue.prepare,
        skills=shan_hai_xin_jue.SKILLS, dots=shan_hai_xin_jue.DOTS, buffs=shan_hai_xin_jue.BUFFS,
        talents=shan_hai_xin_jue.TALENTS, talent_choices=shan_hai_xin_jue.TALENT_CHOICES,
        recipes=shan_hai_xin_jue.RECIPES, recipe_choices=shan_hai_xin_jue.RECIPE_CHOICES,
        gains=shan_hai_xin_jue.GAINS,
    ),
    10786: School(
        id=10786, name="周天功", school="段氏", major="元气", kind="内功", attribute=zhou_tian_gong.Attribute,
        formation="九天九龙阵", prepare=zhou_tian_gong.prepare,
        skills=zhou_tian_gong.SKILLS, dots=zhou_tian_gong.DOTS, buffs=zhou_tian_gong.BUFFS,
        talents=zhou_tian_gong.TALENTS, talent_choices=zhou_tian_gong.TALENT_CHOICES,
        recipes=zhou_tian_gong.RECIPES, recipe_choices=zhou_tian_gong.RECIPE_CHOICES,
        gains=zhou_tian_gong.GAINS,
    )
}
