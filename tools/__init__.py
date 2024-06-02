import os.path
import re

import lupa.lua54 as lupa
import pandas as pd

from base.skill import DotDamage, Damage
from schools import SUPPORT_SCHOOLS

BASE_DIR = "../../jx3_hd_src"
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

PATTERN = re.compile(r'Include\("([^"]+)"\)')


def remove_include(code):
    new_code = PATTERN.sub('', code)
    return new_code


def prepare_lua_runtime(lua):
    lua.execute(INCLUDE_LUA)
    with open(os.path.join(BASE_DIR, "scripts/include/Skill.lh"), encoding="gbk") as f:
        lua_code = remove_include(f.read())
    lua.execute(lua_code)


LUA = lupa.LuaRuntime()
prepare_lua_runtime(LUA)


class Skill:
    skill_id = 0
    skill_level = 0
    skill_name = ""

    kind_type = None

    channel_interval = 0

    @staticmethod
    def empty_function(*args):
        return

    def __init__(self, skill_id, skill_level, skill_name, kind_type):
        self.skill_id = skill_id
        self.skill_level = skill_level
        self.skill_name = skill_name
        self.kind_type = kind_type

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
        self.channel_interval = nChannelInterval

    def __getitem__(self, key):
        if key in dir(self):
            return getattr(self, key)
        else:
            return self.empty_function

    def __setitem__(self, key, value):
        if key in dir(self):
            setattr(self, key, value)


def prepare_skills():
    damages, dot_damages = {}, {}
    for school in SUPPORT_SCHOOLS.values():
        for skill_id, skill in school.skills.items():
            if isinstance(skill, DotDamage):
                dot_damages[skill_id] = skill
            elif isinstance(skill, Damage):
                damages[skill_id] = skill
    return damages, dot_damages


DAMAGES, DOT_DAMAGES = prepare_skills()
