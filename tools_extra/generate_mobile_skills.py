import lupa.lua54 as lupa
from tqdm import tqdm

from kungfus import SUPPORT_KUNGFU
from tools import *


def prepare_skills():
    skills = []
    for kungfu in SUPPORT_KUNGFU.values():
        for skill_id in kungfu.skills:
            skill_id = abs(skill_id)
            if skill_id in skills:
                continue
            skills.append(skill_id)
    return skills


ATTRIBUTE_TYPE = {
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
function GetDesertHorseList()
    return {};
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


def prepare_lua_engine(preset_lua):
    engine = lupa.LuaRuntime()
    engine.execute(preset_lua)
    with open(os.path.join(BASE_DIR, "scripts/include/Skill.lh"), encoding="utf-8") as f:
        engine.execute(INCLUDE_PATTERN.sub('', f.read()))
    with open(os.path.join(BASE_DIR, "scripts/include/NewSkill.lh"), encoding="utf-8") as f:
        engine.execute(INCLUDE_PATTERN.sub('', f.read()))
    return engine


SKILL_TAB = read_tab("settings/skill_mobile/skills.tab")
SKILL_TXT = read_tab("ui/Scheme/case_mobile/skill.txt")

SCRIPTS_PATH = "scripts/skill_mobile"


class SkillLua:
    skill_id = 0
    skill_level = 0
    skill_name = ""
    alias_name = ""

    platform = 0

    kind_type = None
    recipe_type = None
    recipe_mask = None
    event_mask_1 = 0
    event_mask_2 = 0

    weapon_damage_cof = 0

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

    @property
    def damage_call(self):
        return self.physical_damage_call + self.lunar_damage_call + self.solar_damage_call + self.neutral_damage_call + self.poison_damage_call + self.adaptive_damage_call

    @property
    def surplus_call(self):
        return self.physical_surplus_call + self.lunar_surplus_call + self.solar_surplus_call + self.neutral_surplus_call + self.poison_surplus_call

    @staticmethod
    def empty_function(*args):
        return

    def __init__(
            self, skill_id, skill_level, skill_name, kind_type,
            weapon_request, skill_cof, dot_cof, surplus_cof
    ):
        self.skill_id = skill_id
        self.skill_level = skill_level
        if skill_name:
            self.skill_name = skill_name
        self.kind_type = kind_type
        self.weapon_request = weapon_request
        if weapon_request:
            self.weapon_damage_cof = 1024
        self.skill_cof = skill_cof
        self.dot_cof = dot_cof
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
    def nWeaponDamagePercent(self):
        return self.weapon_damage_cof

    @nWeaponDamagePercent.setter
    def nWeaponDamagePercent(self, nWeaponDamagePercent):
        if self.weapon_request:
            self.weapon_damage_cof = nWeaponDamagePercent

    def AddAttribute(self, *args):
        if len(args) < 3:
            return

        attr_type = args[1]
        if attr := ATTRIBUTE_TYPE_MAP.get(attr_type):
            if "call" in attr:
                setattr(self, attr, getattr(self, attr) + 1)
            elif "adaptive" in attr:
                setattr(self, attr, args[3])
            else:
                setattr(self, attr, args[2])

    def __call__(self, *args, **kwargs):
        pass


def parse_lua(skill_id):
    skill_row = SKILL_TAB[SKILL_TAB.SkillID == skill_id].iloc[0]
    alias_name = skill_row.SkillName
    max_level = int(skill_row.MaxLevel)
    kind_type = skill_row.KindType if pd.notna(skill_row.KindType) else ""
    weapon_request = int(skill_row.WeaponRequest)
    skill_cof = int(skill_row.SkillCoefficient) if pd.notna(skill_row.SkillCoefficient) else 0
    dot_cof = int(skill_row.DotCoefficient) if pd.notna(skill_row.DotCoefficient) else 0
    surplus_cof = int(skill_row.SurplusCoefficient) if pd.notna(skill_row.SurplusCoefficient) else 0
    target_file_path = skill_row.ScriptFile.replace('\\', '/')
    lua_code = open(os.path.join(BASE_DIR, SCRIPTS_PATH, target_file_path), encoding="utf-8").read()
    lua_code = INCLUDE_PATTERN.sub('', lua_code)
    skill_args = (
        kind_type, weapon_request, skill_cof, dot_cof, surplus_cof
    )
    return alias_name, max_level, lua_code, skill_args


def collect_result():
    result = []
    lua_engine = prepare_lua_engine(INCLUDE_LUA)
    for skill_id in tqdm(SKILL_TAB.SkillID):
        alias_name, max_level, lua_code, skill_args = parse_lua(skill_id)
        filter_skill_txt = SKILL_TXT[SKILL_TXT.SkillID == skill_id]
        if "ApplyByEditor" not in lua_code:
            continue
        lua_engine.execute(lua_code)
        if filter_skill_txt.empty:
            skill_name = None
        else:
            skill_name = filter_skill_txt.iloc[-1].Name

        skill = SkillLua(skill_id, 1, skill_name, *skill_args)
        skill.alias_name = alias_name
        skill.max_level = max_level
        lua_engine.globals()['ApplyByEditor'](skill)

        if not skill.damage_call:
            del skill.skill_cof
        if not skill.surplus_call and skill.surplus_cof:
            del skill.surplus_cof
        if not skill.physical_damage_call and skill.weapon_damage_cof:
            del skill.weapon_damage_cof
        if not skill.damage_call and not skill.surplus_call and not skill.dot_cof:
            continue

        del skill.weapon_request
        if not skill.dot_cof:
            del skill.dot_cof
        result.append(vars(skill).copy())
    return pd.DataFrame(result)


def generate():
    df = collect_result()
    df = df[['skill_id', 'skill_name', 'alias_name', 'kind_type', 'skill_cof', 'surplus_cof', 'dot_cof']]
    df.to_csv("assets/mobile_skills.csv", index=False)


if __name__ == '__main__':
    generate()
