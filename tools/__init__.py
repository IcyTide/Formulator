import json
import os.path
import re

import lupa.lua54 as lupa
import pandas as pd

from base.buff import CustomBuff
from general.gains import GENERAL_GAINS
from schools import SUPPORT_SCHOOLS

BASE_DIR = "../JX3TABS"
SAVE_DIR = "assets"

SKILL_TAB = pd.read_csv(os.path.join(BASE_DIR, "settings/skill/skills.tab"), sep="\t", low_memory=False, encoding="gbk")
SKILL_TAB['Platform'] = 0
MOBILE_SKILL_TAB = pd.read_csv(os.path.join(BASE_DIR, "settings/skill_mobile/skills.tab"), sep="\t", low_memory=False,
                               encoding="gbk")
MOBILE_SKILL_TAB['Platform'] = 1
SKILL_TAB = pd.concat([SKILL_TAB, MOBILE_SKILL_TAB], axis=0)
BUFF_TAB = pd.read_csv(os.path.join(BASE_DIR, "settings/skill/buff.tab"), sep="\t", low_memory=False, encoding="gbk")
BUFF_TAB['Platform'] = 0
MOBILE_BUFF_TAB = pd.read_csv(os.path.join(BASE_DIR, "settings/skill_mobile/buff.tab"), sep="\t", low_memory=False,
                              encoding="gbk")
MOBILE_BUFF_TAB['Platform'] = 1
BUFF_TAB = pd.concat([BUFF_TAB, MOBILE_BUFF_TAB], axis=0)
SKILL_TXT = pd.read_csv(os.path.join(BASE_DIR, "ui/Scheme/Case/skill.txt"), sep="\t", low_memory=False, encoding="gbk")
MOBILE_SKILL_TXT = pd.read_csv(os.path.join(BASE_DIR, "ui/Scheme/case_mobile/skill.txt"), sep="\t", low_memory=False,
                               encoding="gbk")
SKILL_TXT = pd.concat([SKILL_TXT, MOBILE_SKILL_TXT], axis=0)
BUFF_TXT = pd.read_csv(os.path.join(BASE_DIR, "ui/Scheme/Case/buff.txt"), sep="\t", low_memory=False, encoding="gbk")
MOBILE_BUFF_TXT = pd.read_csv(os.path.join(BASE_DIR, "ui/Scheme/case_mobile/buff.txt"), sep="\t", low_memory=False,
                              encoding="gbk")
BUFF_TXT = pd.concat([BUFF_TXT, MOBILE_BUFF_TXT], axis=0)

ATTRIBUTE_TYPE = dict(
    SKILL_PHYSICS_DAMAGE="physical_damage_base",
    SKILL_LUNAR_DAMAGE="lunar_damage_base",
    SKILL_SOLAR_DAMAGE="solar_damage_base",
    SKILL_NEUTRAL_DAMAGE="neutral_damage_base",
    SKILL_POISON_DAMAGE="poison_damage_base",

    SKILL_PHYSICS_DAMAGE_RAND="physical_damage_rand",
    SKILL_LUNAR_DAMAGE_RAND="lunar_damage_rand",
    SKILL_SOLAR_DAMAGE_RAND="solar_damage_rand",
    SKILL_NEUTRAL_DAMAGE_RAND="neutral_damage_rand",
    SKILL_POISON_DAMAGE_RAND="poison_damage_rand",

    PHYSICS_ATTACK_POWER_PERCENT="physical_attack_power_gain",
    LUNAR_ATTACK_POWER_PERCENT="lunar_attack_power_gain",
    SOLAR_ATTACK_POWER_PERCENT="solar_attack_power_gain",
    NEUTRAL_ATTACK_POWER_PERCENT="neutral_attack_power_gain",
    POISON_ATTACK_POWER_PERCENT="poison_attack_power_gain",

    PHYSICS_CRITICAL_STRIKE_BASE_RATE="physical_critical_power_rate",
    LUNAR_CRITICAL_STRIKE_BASE_RATE="lunar_critical_power_rate",
    SOLAR_CRITICAL_STRIKE_BASE_RATE="solar_critical_power_rate",
    NEUTRAL_CRITICAL_STRIKE_BASE_RATE="neutral_critical_power_rate",
    POISON_CRITICAL_STRIKE_BASE_RATE="poison_critical_power_rate",

    PHYSICS_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE="physical_critical_power_rate",
    LUNAR_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE="lunar_critical_power_rate",
    SOLAR_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE="solar_critical_power_rate",
    NEUTRAL_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE="neutral_critical_power_rate",
    POISON_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE="poison_critical_power_rate",

    PHYSICS_SHIELD_PERCENT="physical_shield_gain",
    LUNAR_MAGIC_SHIELD_PERCENT="lunar_shield_gain",
    SOLAR_MAGIC_SHIELD_PERCENT="solar_shield_gain",
    NEUTRAL_MAGIC_SHIELD_PERCENT="neutral_shield_gain",
    POISON_MAGIC_SHIELD_PERCENT="poison_shield_gain",

    GLOBAL_DAMGAGE_FACTOR="global_damage_factor",
    DST_NPC_DAMAGE_COEFFICIENT="pve_addition",
    ALL_DAMAGE_ADD_PERCENT="damage_addition",

    PHYSICS_ATTACK_POWER_BASE="physical_attack_power_base",
    MAGIC_ATTACK_POWER_BASE="magical_attack_power_base",

    CALL_PHYSICS_DAMAGE="physical_damage_call",
    CALL_LUNAR_DAMAGE="lunar_damage_call",
    CALL_SOLAR_DAMAGE="solar_damage_call",
    CALL_NEUTRAL_DAMAGE="neutral_damage_call",
    CALL_POISON_DAMAGE="poison_damage_call",

    CALL_ADAPTIVE_DAMAGE="adaptive_damage_call",

    CALL_SURPLUS_PHYSICS_DAMAGE="physical_surplus_call",
    CALL_SURPLUS_LUNAR_DAMAGE="lunar_surplus_call",
    CALL_SURPLUS_SOLAR_DAMAGE="solar_surplus_call",
    CALL_SURPLUS_NEUTRAL_DAMAGE="neutral_surplus_call",
    CALL_SURPLUS_POISON_DAMAGE="poison_surplus_call"
)
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
JSON_STR_KEY_PATTERN = re.compile(r'"(\d+)":')


def remove_include(code):
    new_code = INCLUDE_PATTERN.sub('', code)
    return new_code


def prepare_lua_runtime(lua):
    lua.execute(INCLUDE_LUA)
    with open(os.path.join(BASE_DIR, "scripts/include/Skill.lh"), encoding="gbk") as f:
        lua_code = remove_include(f.read())
    lua.execute(lua_code)


LUA = lupa.LuaRuntime()
prepare_lua_runtime(LUA)


def save_code(prefix, code):
    code = json.dumps(code, indent=4, ensure_ascii=False)
    code = f"{prefix.upper()} = " + JSON_STR_KEY_PATTERN.sub(r'\1:', code)
    with open(os.path.join(SAVE_DIR, f"{prefix.lower()}.py"), "w", encoding="utf-8") as f:
        f.write(code)


def prepare_data():
    skills, dots, buffs = [], [], []

    for school in SUPPORT_SCHOOLS.values():
        for skill_id, skill in school.skills.items():
            if skill_id in skills:
                continue
            skills.append(skill_id)
        for dot_id, dot in school.dots.items():
            if dot_id in dots:
                continue
            dots.append(dot_id)
        for buff_id, buff in school.buffs.items():
            if buff_id in buffs:
                continue
            if isinstance(buff, CustomBuff):
                continue
            if buff_id < 0:
                buff_id = -buff_id
            buffs.append(buff_id)
    for buff_id, buff in GENERAL_GAINS.items():
        if buff_id in buffs:
            continue
        if isinstance(buff, CustomBuff):
            continue
        if buff_id < 0:
            buff_id = -buff_id
        buffs.append(buff_id)
    return skills, dots, buffs


SKILLS, DOTS, BUFFS = prepare_data()
