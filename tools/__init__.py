import os.path
import re

import lupa.lua54 as lupa

BASE_DIR = "../../jx3_hd_src"

LUA = lupa.LuaRuntime()

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
    -13: "global_damage_factor",
    -14: "pve_addition"
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

    CALL_PHYSICS_DAMAGE = 1,
    CALL_LUNAR_DAMAGE = 2,
    CALL_SOLAR_DAMAGE = 2,
    CALL_NEUTRAL_DAMAGE = 2,
    CALL_POISON_DAMAGE = 2,

    CALL_SURPLUS_PHYSICS_DAMAGE = 3,
    CALL_SURPLUS_LUNAR_DAMAGE = 3,
    CALL_SURPLUS_SOLAR_DAMAGE = 3,
    CALL_SURPLUS_NEUTRAL_DAMAGE = 3,
    CALL_SURPLUS_POISON_DAMAGE = 3,

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
};
"""

LUA.execute(INCLUDE_LUA)

pattern = re.compile(r'Include\("([^"]+)"\)')


def remove_include(s):
    new_s = pattern.sub('', s)
    return new_s


with open(os.path.join(BASE_DIR, "scripts/include/Skill.lh"), encoding="gbk") as f:
    lua_code = remove_include(f.read())
LUA.execute(lua_code)
