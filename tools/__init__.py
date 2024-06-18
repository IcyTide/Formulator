import json
import os.path
import re

import lupa.lua54 as lupa
import pandas as pd

from base.buff import CustomBuff
from base.skill import Dot
from schools import SUPPORT_SCHOOLS

BASE_DIR = "../JX3TABS"
SAVE_DIR = "assets"

SKILL_TAB = pd.read_csv(os.path.join(BASE_DIR, "settings/skill/skills.tab"), sep="\t", low_memory=False, encoding="gbk")
BUFF_TAB = pd.read_csv(os.path.join(BASE_DIR, "settings/skill/buff.tab"), sep="\t", low_memory=False, encoding="gbk")
SKILL_TXT = pd.read_csv(os.path.join(BASE_DIR, "ui/Scheme/Case/skill.txt"), sep="\t", low_memory=False, encoding="gbk")
BUFF_TXT = pd.read_csv(os.path.join(BASE_DIR, "ui/Scheme/Case/buff.txt"), sep="\t", low_memory=False, encoding="gbk")

ATTRIBUTE_TYPE = {
    -1: "physical_damage_base",
    -2: "magical_damage_base",
    -3: "physical_damage_rand",
    -4: "magical_damage_rand",
    -5: "physical_attack_power_gain",
    -6: "magical_attack_power_gain",
    -7: "physical_critical_strike_rate",
    -8: "magical_critical_strike_rate",
    -9: "physical_critical_power_rate",
    -10: "magical_critical_power_rate",
    -11: "physical_shield_gain",
    -12: "magical_shield_gain",
    -13: "global_damage_cof",
    -14: "pve_addition",
    -15: "damage_addition"
}
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
ATTRIBUTE_TYPE = {
    SKILL_PHYSICS_DAMAGE = -1,
    SKILL_LUNAR_DAMAGE = -2,
    SKILL_SOLAR_DAMAGE = -2,
    SKILL_NEUTRAL_DAMAGE = -2,
    SKILL_POISON_DAMAGE = -2,

    SKILL_PHYSICS_DAMAGE_RAND = -3,
    SKILL_LUNAR_DAMAGE_RAND = -4,
    SKILL_SOLAR_DAMAGE_RAND = -4,
    SKILL_NEUTRAL_DAMAGE_RAND = -4,
    SKILL_POISON_DAMAGE_RAND = -4,

    PHYSICS_ATTACK_POWER_PERCENT = -5,
    LUNAR_ATTACK_POWER_PERCENT = -6,
    SOLAR_ATTACK_POWER_PERCENT = -6,
    NEUTRAL_ATTACK_POWER_PERCENT = -6,
    POISON_ATTACK_POWER_PERCENT = -6,

    PHYSICS_CRITICAL_STRIKE_BASE_RATE = -7,
    LUNAR_CRITICAL_STRIKE_BASE_RATE = -8,
    SOLAR_CRITICAL_STRIKE_BASE_RATE = -8,
    NEUTRAL_CRITICAL_STRIKE_BASE_RATE = -8,
    POISON_CRITICAL_STRIKE_BASE_RATE = -8,
    MAGIC_CRITICAL_STRIKE_BASE_RATE = -8,

    PHYSICS_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE = -9,
    LUNAR_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE = -10,
    SOLAR_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE = -10,
    NEUTRAL_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE = -10,
    POISON_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE = -10,
    MAGIC_CRITICAL_DAMAGE_POWER_BASE_KILONUM_RATE = -10,

    PHYSICS_SHIELD_PERCENT = -11,
    LUNAR_MAGIC_SHIELD_PERCENT = -12,
    SOLAR_MAGIC_SHIELD_PERCENT = -12,
    NEUTRAL_MAGIC_SHIELD_PERCENT = -12,
    POISON_MAGIC_SHIELD_PERCENT = -12,

    GLOBAL_DAMGAGE_FACTOR = -13,
    DST_NPC_DAMAGE_COEFFICIENT = -14,
    ALL_DAMAGE_ADD_PERCENT = -15,

    CALL_PHYSICS_DAMAGE = 1,
    CALL_LUNAR_DAMAGE = 2,
    CALL_SOLAR_DAMAGE = 2,
    CALL_NEUTRAL_DAMAGE = 2,
    CALL_POISON_DAMAGE = 2,
    
    CALL_ADAPTIVE_DAMAGE = 3,
    
    CALL_SURPLUS_PHYSICS_DAMAGE = 4,
    CALL_SURPLUS_LUNAR_DAMAGE = 5,
    CALL_SURPLUS_SOLAR_DAMAGE = 5,
    CALL_SURPLUS_NEUTRAL_DAMAGE = 5,
    CALL_SURPLUS_POISON_DAMAGE = 5,
};
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
            if skill_id in skills or skill_id in dots:
                continue
            if isinstance(skill, Dot):
                dots.append(skill_id)
            else:
                skills.append(skill_id)

        for buff_id, buff in school.buffs.items():
            if buff_id in buffs:
                continue
            if isinstance(buff, CustomBuff):
                continue
            if buff_id < 0:
                buff_id = -buff_id
            buffs.append(buff_id)

    return skills, dots, buffs


SKILLS, DOTS, BUFFS = prepare_data()
