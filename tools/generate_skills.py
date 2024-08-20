import lupa.lua54 as lupa
from tqdm import tqdm

from schools import SUPPORT_SCHOOLS
from tools import *


def prepare_skills():
    skills = []
    for school in SUPPORT_SCHOOLS.values():
        for skill_id, skill in school.skills.items():
            if skill_id in skills:
                continue
            skills.append(skill_id)
    return skills


SKILLS = prepare_skills()

ATTRIBUTE_TYPE = {
    "SKILL_PHYSICS_DAMAGE": "physical_damage_base",
    "SKILL_LUNAR_DAMAGE": "lunar_damage_base",
    "SKILL_SOLAR_DAMAGE": "solar_damage_base",
    "SKILL_NEUTRAL_DAMAGE": "neutral_damage_base",
    "SKILL_POISON_DAMAGE": "poison_damage_base",

    "SKILL_PHYSICS_DAMAGE_RAND": "physical_damage_rand",
    "SKILL_LUNAR_DAMAGE_RAND": "lunar_damage_rand",
    "SKILL_SOLAR_DAMAGE_RAND": "solar_damage_rand",
    "SKILL_NEUTRAL_DAMAGE_RAND": "neutral_damage_rand",
    "SKILL_POISON_DAMAGE_RAND": "poison_damage_rand",

    "PHYSICS_ATTACK_POWER_PERCENT": "physical_attack_power_gain",
    "LUNAR_ATTACK_POWER_PERCENT": "lunar_attack_power_gain",
    "SOLAR_ATTACK_POWER_PERCENT": "solar_attack_power_gain",
    "NEUTRAL_ATTACK_POWER_PERCENT": "neutral_attack_power_gain",
    "POISON_ATTACK_POWER_PERCENT": "poison_attack_power_gain",

    "PHYSICS_CRITICAL_STRIKE_BASE_RATE": "physical_critical_power_rate",
    "LUNAR_CRITICAL_STRIKE_BASE_RATE": "lunar_critical_power_rate",
    "SOLAR_CRITICAL_STRIKE_BASE_RATE": "solar_critical_power_rate",
    "NEUTRAL_CRITICAL_STRIKE_BASE_RATE": "neutral_critical_power_rate",
    "POISON_CRITICAL_STRIKE_BASE_RATE": "poison_critical_power_rate",

    "PHYSICS_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE": "physical_critical_power_rate",
    "LUNAR_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE": "lunar_critical_power_rate",
    "SOLAR_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE": "solar_critical_power_rate",
    "NEUTRAL_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE": "neutral_critical_power_rate",
    "POISON_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE": "poison_critical_power_rate",

    "PHYSICS_SHIELD_PERCENT": "physical_shield_gain",
    "LUNAR_MAGIC_SHIELD_PERCENT": "lunar_shield_gain",
    "SOLAR_MAGIC_SHIELD_PERCENT": "solar_shield_gain",
    "NEUTRAL_MAGIC_SHIELD_PERCENT": "neutral_shield_gain",
    "POISON_MAGIC_SHIELD_PERCENT": "poison_shield_gain",

    "GLOBAL_DAMGAGE_FACTOR": "global_damage_factor",
    "DST_NPC_DAMAGE_COEFFICIENT": "pve_addition",
    "ALL_DAMAGE_ADD_PERCENT": "damage_addition",

    "PHYSICS_ATTACK_POWER_BASE": "physical_attack_power_base",
    "MAGIC_ATTACK_POWER_BASE": "magical_attack_power_base",

    "CALL_PHYSICS_DAMAGE": "physical_damage_call",
    "CALL_LUNAR_DAMAGE": "lunar_damage_call",
    "CALL_SOLAR_DAMAGE": "solar_damage_call",
    "CALL_NEUTRAL_DAMAGE": "neutral_damage_call",
    "CALL_POISON_DAMAGE": "poison_damage_call",

    "CALL_ADAPTIVE_DAMAGE": "adaptive_damage_call",

    "CALL_SURPLUS_PHYSICS_DAMAGE": "physical_surplus_call",
    "CALL_SURPLUS_LUNAR_DAMAGE": "lunar_surplus_call",
    "CALL_SURPLUS_SOLAR_DAMAGE": "solar_surplus_call",
    "CALL_SURPLUS_NEUTRAL_DAMAGE": "neutral_surplus_call",
    "CALL_SURPLUS_POISON_DAMAGE": "poison_surplus_call"
}
ATTRIBUTE_TYPE_CODE = "\n".join(f'{k}={i},' for i, k in enumerate(ATTRIBUTE_TYPE))
ATTRIBUTE_TYPE_MAP = {i: v for i, v in enumerate(ATTRIBUTE_TYPE.values())}
INCLUDE_LUA = """
function GetEditorString(param_1, param_2)
    return true;
end

function IsClient()
    return true;
end

ABSORB_ATTRIBUTE_SHIELD_TYPE = {};
RELATION_FORCE = {};
GLOBAL = {
    GAME_FPS = 16
};

ROLE_TYPE = {
    LITTLE_BOY = 2,
    STANDARD_MALE = 3,
    LITTLE_GIRL = 4,
    STANDARD_FEMALE = 5,
};
BUFF_COMPARE_FLAG = {};
SKILL_COMPARE_FLAG = {};
ATTRIBUTE_EFFECT_MODE = {};
""" + f"""
ATTRIBUTE_TYPE = {{
{ATTRIBUTE_TYPE_CODE}
}};
"""

INCLUDE_PATTERN = re.compile(r'Include\("([^"]+)"\)')
LUA = lupa.LuaRuntime()
LUA.execute(INCLUDE_LUA)
with open(os.path.join(BASE_DIR, "scripts/include/Skill.lh"), encoding="gbk") as f:
    LUA.execute(INCLUDE_PATTERN.sub('', f.read()))

SKILL_TAB = read_tab("settings/skill/skills.tab")
SKILL_TAB['Platform'] = 0
MOBILE_SKILL_TAB = read_tab("settings/skill_mobile/skills.tab")
MOBILE_SKILL_TAB['Platform'] = 1
SKILL_TAB = pd.concat([SKILL_TAB, MOBILE_SKILL_TAB], axis=0)
SKILL_TXT = read_tab("ui/Scheme/Case/skill.txt")
MOBILE_SKILL_TXT = read_tab("ui/Scheme/case_mobile/skill.txt")
SKILL_TXT = pd.concat([SKILL_TXT, MOBILE_SKILL_TXT], axis=0)

SCRIPTS_PATH = {
    0: "scripts/skill",
    1: "scripts/skill_mobile",
}


class SkillLua:
    skill_id = 0
    skill_level = 0
    skill_name = ""

    platform = 0

    kind_type = None
    recipe_type = None
    recipe_mask = None
    event_mask_1 = 0
    event_mask_2 = 0

    physical_damage_base = 0
    physical_damage_rand = 0
    lunar_damage_base = 0
    lunar_damage_rand = 0
    solar_damage_base = 0
    solar_damage_rand = 0
    neutral_damage_base = 0
    neutral_damage_rand = 0
    poison_damage_base = 0
    poison_damage_rand = 0

    prepare_frame = 0
    channel_interval = 0
    skill_cof = 0
    dot_cof = 0
    surplus_cof = 0
    weapon_damage_cof = 0
    global_damage_factor = 0

    physical_attack_power_gain = 0
    physical_critical_strike_rate = 0
    physical_critical_power_rate = 0
    physical_shield_gain = 0
    solar_attack_power_gain = 0
    solar_critical_strike_rate = 0
    solar_critical_power_rate = 0
    solar_shield_gain = 0
    lunar_attack_power_gain = 0
    lunar_critical_strike_rate = 0
    lunar_critical_power_rate = 0
    lunar_shield_gain = 0
    neutral_attack_power_gain = 0
    neutral_critical_strike_rate = 0
    neutral_critical_power_rate = 0
    neutral_shield_gain = 0
    poison_attack_power_gain = 0
    poison_critical_strike_rate = 0
    poison_critical_power_rate = 0
    poison_shield_gain = 0

    pve_addition = 0

    physical_damage_call = 0
    lunar_damage_call = 0
    solar_damage_call = 0
    neutral_damage_call = 0
    poison_damage_call = 0
    adaptive_damage_call = 0

    physical_surplus_call = 0
    lunar_surplus_call = 0
    solar_surplus_call = 0
    neutral_surplus_call = 0
    poison_surplus_call = 0

    physical_attack_power_base = 0
    magical_attack_power_base = 0

    @staticmethod
    def empty_function(*args):
        return

    def __init__(
            self, skill_id, skill_level, skill_name, kind_type, recipe_type, recipe_mask,
            weapon_request, use_skill_cof, platform, skill_cof, dot_cof, surplus_cof
    ):
        self.skill_id = skill_id
        self.skill_level = skill_level
        if skill_name:
            self.skill_name = skill_name
        self.kind_type = kind_type
        self.recipe_type = recipe_type
        self.recipe_mask = recipe_mask
        self.weapon_request = weapon_request
        if weapon_request:
            self.weapon_damage_cof = 1024
        self.use_skill_cof = use_skill_cof
        self.platform = platform
        if use_skill_cof and not platform:
            self.channel_interval = 16
        if skill_cof:
            self.skill_cof = skill_cof
        if dot_cof:
            self.dot_cof = dot_cof
        if surplus_cof:
            self.surplus_cof = surplus_cof

    def __getitem__(self, key):
        if key in dir(self):
            return getattr(self, key)
        else:
            return self.empty_function

    def __setitem__(self, key, value):
        if key in dir(self):
            setattr(self, key, value)

    @property
    def dwSkillID(self):
        return self.skill_id

    @dwSkillID.setter
    def dwSkillID(self, dwSkillID):
        self.skill_id = dwSkillID

    @property
    def dwLevel(self):
        return self.skill_level

    @dwLevel.setter
    def dwLevel(self, dwLevel):
        self.skill_level = dwLevel

    @property
    def nChannelInterval(self):
        return self.channel_interval

    @nChannelInterval.setter
    def nChannelInterval(self, nChannelInterval):
        if self.use_skill_cof and not self.platform:
            self.channel_interval = nChannelInterval

    @property
    def nPrepareFrames(self):
        return self.prepare_frame

    @nPrepareFrames.setter
    def nPrepareFrames(self, nPrepareFrames):
        if nPrepareFrames and self.use_skill_cof and not self.platform:
            self.prepare_frame = nPrepareFrames

    @property
    def nWeaponDamagePercent(self):
        return self.weapon_damage_cof

    @nWeaponDamagePercent.setter
    def nWeaponDamagePercent(self, nWeaponDamagePercent):
        if self.weapon_request:
            self.weapon_damage_cof = nWeaponDamagePercent

    def AddAttribute(self, *args):
        if len(args) < 3:
            return

        attr_type, param = args[1], args[2]
        if attr := ATTRIBUTE_TYPE_MAP.get(attr_type):
            if "call" in attr:
                setattr(self, attr, getattr(self, attr) + 1)
            else:
                setattr(self, attr, param)

    def __call__(self, *args, **kwargs):
        pass


def parse_lua(skill_id):
    skill_row = SKILL_TAB[SKILL_TAB.SkillID == skill_id].iloc[0]
    max_level = int(skill_row.MaxLevel)
    kind_type = skill_row.KindType if pd.notna(skill_row.KindType) else ""
    recipe_type = skill_row.RecipeType if pd.notna(skill_row.RecipeType) else 0
    recipe_mask = skill_row.RecipeTagMask if pd.notna(skill_row.RecipeTagMask) else 0
    # event_mask_1 = int(skill_row.SkillEventMask1) if pd.notna(skill_row.SkillEventMask1) else 0
    # event_mask_2 = int(skill_row.SkillEventMask2) if pd.notna(skill_row.SkillEventMask2) else 0
    weapon_request = int(skill_row.WeaponRequest)
    use_skill_cof = int(skill_row.UseSkillCoefficient)
    platform = skill_row.Platform
    skill_cof = int(skill_row.SkillCoefficient) if pd.notna(skill_row.SkillCoefficient) else 0
    dot_cof = int(skill_row.DotCoefficient) if pd.notna(skill_row.DotCoefficient) else 0
    surplus_cof = int(skill_row.SurplusCoefficient) if pd.notna(skill_row.SurplusCoefficient) else 0
    lua_code = open(os.path.join(BASE_DIR, SCRIPTS_PATH[platform], skill_row.ScriptFile), encoding="gbk").read()
    lua_code = INCLUDE_PATTERN.sub('', lua_code)
    skill_args = (
        kind_type, recipe_type, recipe_mask, weapon_request, use_skill_cof, platform, skill_cof, dot_cof, surplus_cof
    )
    return max_level, lua_code, skill_args


def collect_result():
    result = []
    for skill_id in tqdm(SKILLS):
        max_level, lua_code, skill_args = parse_lua(skill_id)
        filter_skill_txt = SKILL_TXT[SKILL_TXT.SkillID == skill_id]
        LUA.execute(lua_code)
        for skill_level in range(max_level):
            skill_level += 1
            if filter_skill_txt.empty:
                skill_name = None
            elif skill_level in filter_skill_txt.Level.tolist():
                skill_name = filter_skill_txt[filter_skill_txt.Level == skill_level].iloc[0].Name
            else:
                skill_name = filter_skill_txt.iloc[-1].Name

            skill = SkillLua(skill_id, skill_level, skill_name, *skill_args)
            LUA.globals()['GetSkillLevelData'](skill)
            if not skill.physical_damage_call and skill.weapon_damage_cof:
                del skill.weapon_damage_cof

            result.append(skill.__dict__.copy())
    return pd.DataFrame(result)


def convert_json(result):
    exclude_columns = [
        "skill_id", "skill_level", "weapon_request", "use_skill_cof",
        "kind_type", "recipe_type", "recipe_mask", "platform"
    ]
    float_columns = [
        "prepare_frame", "channel_interval", "weapon_damage_cof", "global_damage_factor",
    ]
    result_json = {}
    for skill_id in result.skill_id.unique().tolist():
        filter_result = result[result.skill_id == skill_id]
        first_row = filter_result.iloc[0]
        result_json[skill_id] = dict(
            kind_type=first_row.kind_type, platform=int(first_row.platform),
            recipe_type=int(first_row.recipe_type), recipe_mask=int(first_row.recipe_mask),
        )
        for column in result.columns:
            if column in exclude_columns:
                continue
            if filter_result[column].isna().all():
                continue
            filter_column = filter_result[column].fillna(0)
            if column not in float_columns and pd.api.types.is_numeric_dtype(filter_column):
                filter_column = filter_column.astype(int)
            if filter_column.nunique() == 1:
                result_json[skill_id][column] = filter_column.tolist()[0]
            else:
                result_json[skill_id][column] = filter_column.tolist()

    save_code("skills", result_json)


def generate():
    convert_json(collect_result())


if __name__ == '__main__':
    generate()
