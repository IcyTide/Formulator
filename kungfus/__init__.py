from typing import Type, Callable, Dict, List, Tuple

from base.attribute import Attribute
from base.buff import Buff
from base.dot import Dot
from base.gain import Gain
from base.recipe import Recipe
from base.skill import Skill
from general.buffs import GENERAL_BUFFS
from general.recipes import GENERAL_RECIPES
from general.skills import GENERAL_SKILLS
from kungfus import ao_xue_zhan_yi, jing_yu_jue, xiao_chen_jue, bei_ao_jue, gu_feng_jue
from kungfus import tai_xu_jian_yi, wen_shui_jue, fen_shan_jing, ling_hai_jue, yin_long_jue, shan_hai_xin_jue
from kungfus import tie_lao_lv, ming_zun_liu_li_ti
from kungfus import yi_jin_jing, hua_jian_you, tian_luo_gui_dao, fen_ying_sheng_jue, tai_xuan_jing, zhou_tian_gong
from kungfus import zi_xia_gong, bing_xin_jue, du_jing, mo_wen, wu_fang


class Kungfu:
    attribute: Type[Attribute]
    prepare: Callable
    buffs: Dict[int, Buff]
    dots: Dict[int, Dot]
    skills: Dict[int, Skill]
    recipes: Dict[Tuple[int, int], Recipe]
    talents: Dict[int, Gain]
    gains: Dict[tuple, Gain]

    talent_choices: List[List[int]]
    talent_encoder: Dict[str, tuple]
    talent_decoder: Dict[int, str]
    recipe_choices: Dict[str, Dict[str, tuple]]

    def __init__(self, kungfu_id, name, school, major, kind, formation, kungfu):
        self.kungfu_id = kungfu_id
        self.name = name
        self.school = school
        self.major = major
        self.kind = kind
        self.formation = formation

        self.attribute = kungfu.Attribute
        self.prepare = kungfu.prepare

        self.build_buffs(kungfu)
        self.build_dots(kungfu)
        self.build_skills(kungfu)
        self.build_gains(kungfu)
        self.build_talents(kungfu)
        self.build_recipes(kungfu)

    def build_buffs(self, kungfu):
        self.buffs = {**GENERAL_BUFFS}
        for buff_class, items in kungfu.BUFFS.items():
            for buff_id, attrs in items.items():
                self.buffs[buff_id] = buff = buff_class(buff_id)
                buff.set_asset(attrs)

    def build_dots(self, kungfu):
        self.dots = {}
        for dot_class, items in kungfu.DOTS.items():
            for dot_id, attrs in items.items():
                self.dots[dot_id] = dot = dot_class(dot_id)
                dot.set_asset(attrs)

    def build_skills(self, kungfu):
        self.skills = {**GENERAL_SKILLS}
        for skill_class, items in kungfu.SKILLS.items():
            for skill_id, attrs in items.items():
                self.skills[skill_id] = skill = skill_class(skill_id)
                skill.set_asset(attrs)

    def build_recipes(self, kungfu):
        self.recipes = {**GENERAL_RECIPES}
        for recipe_class, items in kungfu.RECIPES.items():
            for recipe_key, attrs in items.items():
                if not isinstance(recipe_key, tuple):
                    recipe_key = (recipe_key, 1)
                self.recipes[recipe_key] = recipe = recipe_class(*recipe_key)
                recipe.set_asset(attrs)
        self.recipe_choices = {}
        for skill, recipes in kungfu.RECIPE_CHOICES.items():
            self.recipe_choices[skill] = {}
            for name, recipe_key in recipes.items():
                if not isinstance(recipe_key, tuple):
                    recipe_key = (recipe_key, 1)
                self.recipe_choices[skill][name] = recipe_key

    def build_talents(self, kungfu):
        self.talent_choices, self.talents = [], {}
        self.talent_encoder, self.talent_decoder = {}, {}
        for talent_choices in kungfu.TALENTS:
            talent_choice = []
            self.talent_choices.append(talent_choice)
            for gain_id, gain in talent_choices.items():
                self.gains[(gain_id, 1)] = self.talents[gain_id] = gain
                self.talent_encoder[gain.gain_name] = (gain_id, 1)
                self.talent_decoder[gain_id] = gain.gain_name
                talent_choice.append(gain.gain_name)

    def build_gains(self, kungfu):
        self.gains = {**kungfu.GAINS}


SUPPORT_KUNGFU = {
    10003: Kungfu(
        10003, "易筋经", "少林", "元气", "内功", "天鼓雷音阵", yi_jin_jing
    ),
    10014: Kungfu(
        10014, "紫霞功", "纯阳", "根骨", "内功", "九宫八卦阵", zi_xia_gong
    ),
    10015: Kungfu(
        10015, "太虚剑意", "纯阳", "身法", "外功", "北斗七星阵", tai_xu_jian_yi
    ),
    10021: Kungfu(
        10021, "花间游", "万花", "元气", "内功", "七绝逍遥阵", hua_jian_you
    ),
    10026: Kungfu(
        10026, "傲血战意", "天策", "力道", "外功", "卫公折冲阵", ao_xue_zhan_yi
    ),
    # 10062: Kungfu(
    #     10062, "铁牢律", "天策", "", "防御", "", tie_lao_lv
    # ),
    10081: Kungfu(
        10081, "冰心诀", "七秀", "根骨", "内功", "九音惊弦阵", bing_xin_jue
    ),
    10144: Kungfu(
        10144, "问水诀", "藏剑", "身法", "外功", "依山观澜阵", wen_shui_jue
    ),
    10145: Kungfu(
        10145, "问水诀", "藏剑", "身法", "外功", "依山观澜阵", wen_shui_jue
    ),
    10175: Kungfu(
        10175, "毒经", "五毒", "根骨", "内功", "万蛊噬心阵", du_jing
    ),
    10224: Kungfu(
        10224, "惊羽诀", "唐门", "力道", "外功", "流星赶月阵", jing_yu_jue
    ),
    10225: Kungfu(
        10225, "天罗诡道", "唐门", "元气", "内功", "千机百变阵", tian_luo_gui_dao
    ),
    10242: Kungfu(
        10242, "焚影圣诀", "明教", "元气", "内功", "炎威破魔阵", fen_ying_sheng_jue
    ),
    # 10243: Kungfu(
    #     10243, "明尊琉璃体", "明教", "", "防御", "", ming_zun_liu_li_ti
    # ),
    # 10268: Kungfu(
    #     10268, "笑尘诀", "丐帮", "力道", "外功", "降龙伏虎阵", xiao_chen_jue
    # ),
    10390: Kungfu(
        10390, "分山劲", "苍云", "身法", "外功", "锋凌横绝阵", fen_shan_jing
    ),
    10447: Kungfu(
        10447, "莫问", "长歌", "根骨", "内功", "万籁金弦阵", mo_wen
    ),
    10464: Kungfu(
        10464, "北傲诀", "霸刀", "力道", "外功", "霜岚洗锋阵", bei_ao_jue
    ),
    10533: Kungfu(
        10533, "凌海诀", "蓬莱", "身法", "外功", "墟海引归阵", ling_hai_jue
    ),
    10585: Kungfu(
        10585, "隐龙诀", "凌雪", "身法", "外功", "龙皇雪风阵", yin_long_jue
    ),
    10615: Kungfu(
        10615, "太玄经", "衍天", "元气", "内功", "九星游年阵", tai_xuan_jing
    ),
    10627: Kungfu(
        10627, "无方", "药宗", "根骨", "内功", "乱暮浊茵阵", wu_fang
    ),
    10698: Kungfu(
        10698, "孤锋诀", "刀宗", "力道", "外功", "横云破锋阵", gu_feng_jue
    ),
    10756: Kungfu(
        10756, "山海心诀", "万灵", "身法", "外功", "苍梧引灵阵", shan_hai_xin_jue
    ),
    10786: Kungfu(
        10786, "周天功", "段氏", "元气", "内功", "含章挺秀阵", zhou_tian_gong
    )
}
