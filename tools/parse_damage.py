import pandas as pd

from tools import *
from tqdm import tqdm

SCRIPTS_PATH = "scripts/skill"


class Damage(Skill):
    physical_damage_base = 0
    magical_damage_base = 0
    physical_damage_rand = 0
    magical_damage_rand = 0

    prepare_frame = 0
    weapon_damage_cof = 0
    global_damage_factor = 0

    physical_attack_power_gain = 0
    physical_critical_strike_rate = 0
    physical_critical_power_rate = 0
    physical_shield_gain = 0
    magical_attack_power_gain = 0
    magical_critical_strike_rate = 0
    magical_critical_power_rate = 0
    magical_shield_gain = 0
    pve_addition = 0

    physical_call = 0
    magical_call = 0
    surplus_call = 0

    def __init__(self, skill_id, skill_level, skill_name, kind_type, weapon_request):
        super().__init__(skill_id, skill_level, skill_name, kind_type)
        self.weapon_request = weapon_request
        if weapon_request:
            self.weapon_damage_cof = 1024
        self.channel_interval = 16

    @property
    def nPrepareFrames(self):
        return self.prepare_frame

    @nPrepareFrames.setter
    def nPrepareFrames(self, nPrepareFrames):
        self.prepare_frame = nPrepareFrames

    @property
    def nWeaponDamagePercent(self):
        return self.weapon_damage_cof

    @nWeaponDamagePercent.setter
    def nWeaponDamagePercent(self, nWeaponDamagePercent):
        if self.weapon_request:
            self.weapon_damage_cof = nWeaponDamagePercent

    def AddAttribute(self, effect_mode, attr_type, param_1, param_2):
        if param_1 is None:
            return

        if attr := ATTRIBUTE_TYPE.get(attr_type):
            setattr(self, attr, param_1)
        elif attr_type == 1:
            self.physical_call += 1
        elif attr_type == 2:
            self.magical_call += 1
        elif attr_type == 3:
            self.surplus_call += 1


def parse_lua(skill_id):
    skill_row = SKILL_TAB[SKILL_TAB.SkillID == skill_id].iloc[0]
    max_level = int(skill_row.MaxLevel)
    kind_type = skill_row.KindType
    weapon_request = int(skill_row.WeaponRequest)
    with open(os.path.join(BASE_DIR, SCRIPTS_PATH, skill_row.ScriptFile), encoding="gbk") as f:
        lua_code = remove_include(f.read())
    return max_level, kind_type, weapon_request, lua_code


def collect_result():
    result = []
    for skill_id in tqdm(DAMAGES):
        max_level, kind_type, weapon_request, lua_code = parse_lua(skill_id)
        filter_skill_txt = SKILL_TXT[SKILL_TXT.SkillID == skill_id]
        LUA.execute(lua_code)
        for skill_level in range(max_level):
            skill_level += 1
            if skill_level in filter_skill_txt.Level.tolist():
                skill_name = filter_skill_txt[filter_skill_txt.Level == skill_level].iloc[0].Name
            else:
                skill_name = filter_skill_txt.iloc[-1].Name

            skill = Damage(skill_id, skill_level, skill_name, kind_type, weapon_request)
            LUA.globals()['GetSkillLevelData'](skill)
            result.append(skill.__dict__)
    return result


if __name__ == '__main__':
    results = collect_result()
    df = pd.DataFrame(results)
    df.to_csv("damages.csv")
    print(df)
