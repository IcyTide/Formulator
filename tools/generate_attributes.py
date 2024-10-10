from tqdm import tqdm

from kungfus import SUPPORT_KUNGFU
from tools import *
from tools.generate_skills import prepare_lua_engine, INCLUDE_LUA, SKILL_TAB, SCRIPTS_PATH, INCLUDE_PATTERN


def prepare_attributes():
    attributes = []
    for kungfu in SUPPORT_KUNGFU.values():
        for attribute_id in kungfu.attribute.attribute_id.values():
            attributes.append(attribute_id)
    return attributes


ATTRIBUTE_TYPE = {
    "DST_NPC_DAMAGE_COEFFICIENT": "pve_addition_base",
    "ALL_SHIELD_IGNORE_PERCENT": "all_shield_ignore",
    "SURPLUS_TO_DST_NPC_DAMAGE_COEFFICIENT": "surplus_to_pve_addition",

    "PHYSICS_ATTACK_POWER_BASE": "physical_attack_power_base",
    "MAGIC_ATTACK_POWER_BASE": "magical_attack_power_base",
    "LUNAR_ATTACK_POWER_BASE": "lunar_attack_power_base",
    "SOLAR_ATTACK_POWER_BASE": "solar_attack_power_base",
    "NEUTRAL_ATTACK_POWER_BASE": "neutral_attack_power_base",
    "POISON_ATTACK_POWER_BASE": "poison_attack_power_base",

    "PHYSICS_CRITICAL_STRIKE": "physical_critical_strike_base",
    "PHYSICS_OVERCOME_BASE": "physical_overcome_base",
    "LUNAR_CRITICAL_STRIKE": "lunar_critical_strike_base",
    "NEUTRAL_CRITICAL_STRIKE": "neutral_critical_strike_base",
    "POISON_OVERCOME_BASE": "poison_overcome_base",

    "AGILITY_TO_PHYSICS_ATTACK_POWER_COF": "agility_to_physical_attack_power",
    "AGILITY_TO_PHYSICS_CRITICAL_STRIKE_COF": "agility_to_physical_critical_strike",
    "AGILITY_TO_PHYSICS_OVERCOME_COF": "agility_to_physical_overcome",
    "STRENGTH_TO_PHYSICS_ATTACK_POWER_COF": "strength_to_physical_attack_power",
    "STRENGTH_TO_PHYSICS_CRITICAL_STRIKE_COF": "strength_to_physical_critical_strike",
    "STRENGTH_TO_PHYSICS_OVERCOME_COF": "strength_to_physical_overcome",

    "SPIRIT_TO_LUNAR_ATTACK_POWER_COF": "spirit_to_lunar_attack_power",
    "SPIRIT_TO_NEUTRAL_ATTACK_POWER_COF": "spirit_to_neutral_attack_power",
    "SPIRIT_TO_POISON_ATTACK_POWER_COF": "spirit_to_poison_attack_power",
    "SPIRIT_TO_LUNAR_CRITICAL_STRIKE_COF": "spirit_to_lunar_critical_strike",
    "SPIRIT_TO_NEUTRAL_CRITICAL_STRIKE_COF": "spirit_to_neutral_critical_strike",
    "SPIRIT_TO_POISON_OVERCOME_COF": "spirit_to_poison_overcome",

    "SPUNK_TO_SOLAR_ATTACK_POWER_COF": "spunk_to_solar_attack_power",
    "SPUNK_TO_SOLAR_AND_LUNAR_ATTACK_POWER_COF": "spunk_to_solar_and_lunar_attack_power",
    "SPUNK_TO_NEUTRAL_ATTACK_POWER_COF": "spunk_to_neutral_attack_power",
    "SPUNK_TO_POISON_ATTACK_POWER_COF": "spunk_to_poison_attack_power",
    "SPUNK_TO_PHYSICS_CRITICAL_STRIKE_COF": "spunk_to_physical_critical_strike",
    "SPUNK_TO_SOLAR_CRITICAL_STRIKE_COF": "spunk_to_solar_critical_strike",
    "SPUNK_TO_SOLAR_AND_LUNAR_CRITICAL_STRIKE_COF": "spunk_to_solar_and_lunar_critical_strike",
    "SPUNK_TO_NEUTRAL_CRITICAL_STRIKE_COF": "spunk_to_neutral_critical_strike",
    "SPUNK_TO_NEUTRAL_OVERCOME_COF": "spunk_to_neutral_overcome",
}
ATTRIBUTE_TYPE_CODE = "\n".join(f'{k}={i},' for i, k in enumerate(ATTRIBUTE_TYPE))
ATTRIBUTE_TYPE_MAP = {i: v for i, v in enumerate(ATTRIBUTE_TYPE.values())}
INCLUDE_LUA = INCLUDE_LUA + """
SKILL_KIND_TYPE = {
    PHYSICS = 0,
    SOLAR_MAGIC = 1,
    LUNAR_MAGIC = 2,
    NEUTRAL_MAGIC = 3,
    POISON = 4,
};
PLAYER_ARENA_TYPE = {
    DPS = 0,
    T = 1,
    THERAPY = 2
};
CHARACTER_ENERGY_TYPE = {
    RAGE = 0,
    ENERGY = 1,
    SUN_ENERGY = 2
};
""" + f"""
ATTRIBUTE_TYPE = {{
{ATTRIBUTE_TYPE_CODE}
}};
"""


class AttributeLua:
    level: int = 0

    def __init__(self, attribute_id, platform, alias_name, level):
        self.attribute_id = attribute_id
        self.platform = platform
        self.alias_name = alias_name
        self.level = level

    @staticmethod
    def empty_function(*args):
        return

    def __getitem__(self, key):
        if key in dir(self):
            return getattr(self, key)
        else:
            return self.empty_function

    def __setitem__(self, key, value):
        if key in dir(self):
            setattr(self, key, value)

    def AddAttribute(self, *args):
        if len(args) < 3:
            return

        attr_type, param = args[1], args[2]
        if attr := ATTRIBUTE_TYPE_MAP.get(attr_type):
            setattr(self, attr, param)

    @property
    def dwLevel(self):
        return self.level

    @dwLevel.setter
    def dwLevel(self, dwLevel):
        self.level = dwLevel

    def __call__(self, *args, **kwargs):
        pass


def parse_lua(attribute_id):
    attribute_row = SKILL_TAB[SKILL_TAB.SkillID == attribute_id].iloc[0]
    alias_name = attribute_row.SkillName
    max_level = int(attribute_row.MaxLevel)
    platform = attribute_row.Platform
    lua_code = open(os.path.join(BASE_DIR, SCRIPTS_PATH[platform], attribute_row.ScriptFile), encoding="utf-8").read()
    lua_code = INCLUDE_PATTERN.sub('', lua_code)
    return max_level, lua_code, (attribute_id, platform, alias_name)


def collect_result():
    result = []
    lua_engine = prepare_lua_engine(INCLUDE_LUA)
    for skill_id in tqdm(prepare_attributes()):
        max_level, lua_code, attribute_args = parse_lua(skill_id)
        lua_engine.execute(lua_code)
        for level in range(max_level):
            level += 1

            attribute = AttributeLua(*attribute_args, level)
            attribute.max_level = max_level
            lua_engine.globals()['GetSkillLevelData'](attribute)

            result.append(vars(attribute).copy())
    return pd.DataFrame(result)


def convert_json(result):
    exclude_columns = ["attribute_id", "level", "alias_name", "platform"]
    float_columns = []
    result_json = {}
    for column in result.columns:
        result[column] = result[column].fillna(0)
        if column in float_columns:
            # result[column] = result[column].apply(format_float)
            pass
        elif pd.api.types.is_numeric_dtype(result[column]):
            result[column] = result[column].astype(int)
    for attribute_id in result.attribute_id.unique().tolist():
        filter_result = result[result.attribute_id == attribute_id]
        first_row = filter_result.iloc[0]
        result_json[attribute_id] = dict(
            alias_name=first_row.alias_name
        )
        for column in result.columns:
            if column in exclude_columns:
                continue
            if filter_result[column].isna().all():
                continue
            if filter_result[column].nunique() == 1:
                if value := filter_result[column].tolist()[0]:
                    result_json[attribute_id][column] = value
            else:
                result_json[attribute_id][column] = filter_result[column].tolist()

    save_code("attributes", result_json)


def generate():
    convert_json(collect_result())


if __name__ == '__main__':
    generate()
