from functools import cached_property
from typing import Type, Callable, Dict, List, Tuple

from base.attribute import Attribute
from base.buff import Buff
from base.dot import Dot
from base.gain import Gain
from base.recipe import Recipe
from base.skill import Skill
from general.buffs import GENERAL_BUFFS
from general.skills import GENERAL_SKILLS
from kungfus import ao_xue_zhan_yi, jing_yu_jue, xiao_chen_jue, bei_ao_jue, gu_feng_jue
from kungfus import tai_xu_jian_yi, wen_shui_jue, fen_shan_jing, ling_hai_jue, yin_long_jue, shan_hai_xin_jue
from kungfus import yi_jin_jing, hua_jian_you, tian_luo_gui_dao, fen_ying_sheng_jue, tai_xuan_jing, zhou_tian_gong
from kungfus import zi_xia_gong, bing_xin_jue, du_jing, mo_wen, wu_fang


class Kungfu:
    platform: int = 0

    attribute: Type[Attribute]
    prepare: Callable
    _buffs: Dict[int, Dict[int, Buff]]
    _dots: Dict[int, Dict[int, Dot]]
    _skills: Dict[int, Dict[int, Skill]]
    talents: Dict[int, Gain]
    talent_choices: List[List[int]]
    recipes: Dict[Tuple[int, int], Recipe]
    recipe_choices: Dict[str, Dict[str, Tuple[int, int]]]
    gains: Dict[tuple, Gain]

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
        self.build_talents(kungfu)
        self.build_recipes(kungfu)
        self.build_gains(kungfu)

    def build_buffs(self, kungfu):
        self._buffs = {0: {**GENERAL_BUFFS}, 1: {**GENERAL_BUFFS}}
        for platform, buffs in kungfu.BUFFS.items():
            for buff_class, items in buffs.items():
                for buff_id, attrs in items.items():
                    self._buffs[platform][buff_id] = buff = buff_class(buff_id)
                    buff.set_asset(attrs)

    @property
    def buffs(self):
        return self._buffs[self.platform]

    @property
    def dots(self):
        return self._dots[self.platform]

    @property
    def skills(self):
        return self._skills[self.platform]

    def build_dots(self, kungfu):
        self._dots = {0: {**GENERAL_BUFFS}, 1: {**GENERAL_BUFFS}}
        for platform, dots in kungfu.DOTS.items():
            for dot_class, items in dots.items():
                for dot_id, attrs in items.items():
                    self._dots[platform][dot_id] = dot = dot_class(dot_id)
                    dot.set_asset(attrs)

    def build_skills(self, kungfu):
        self._skills = {0: {**GENERAL_SKILLS}, 1: {**GENERAL_SKILLS}}
        for platform, skills in kungfu.SKILLS.items():
            for skill_class, items in skills.items():
                for skill_id, attrs in items.items():
                    self._skills[platform][skill_id] = skill = skill_class(skill_id)
                    skill.set_asset(attrs)

    def build_talents(self, kungfu):
        self.talent_choices = kungfu.TALENT_CHOICES
        self.talents = kungfu.TALENTS

    def build_recipes(self, kungfu):
        self.recipe_choices = kungfu.RECIPE_CHOICES
        self.recipes = kungfu.RECIPES

    def build_gains(self, kungfu):
        self.gains = kungfu.GAINS

    @cached_property
    def talent_decoder(self):
        return {talent_id: talent.gain_name for talent_id, talent in self.talents.items()}

    @cached_property
    def talent_encoder(self):
        return {v: k for k, v in self.talent_decoder.items()}


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
    10081: Kungfu(
        10081, "冰心诀", "七秀", "根骨", "内功", "九音惊弦阵", bing_xin_jue
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
    10268: Kungfu(
        10268, "笑尘诀", "丐帮", "力道", "外功", "降龙伏虎阵", xiao_chen_jue
    ),
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
        10786, "周天功", "段氏", "元气", "内功", "九天九龙阵", zhou_tian_gong
    )
}
