import json

from tools import *
from tqdm import tqdm

SCRIPTS_PATH = "scripts/skill"


class SkillLua:
    skill_id = 0
    skill_level = 0
    skill_name = ""

    kind_type = None
    recipe_type = None
    event_mask_1 = 0
    event_mask_2 = 0

    physical_damage_base = 0
    magical_damage_base = 0
    physical_damage_rand = 0
    magical_damage_rand = 0

    prepare_frame = 0
    channel_interval = 0
    weapon_damage_cof = 0
    global_damage_cof = 0

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

    @staticmethod
    def empty_function(*args):
        return

    def __init__(
            self, skill_id, skill_level, skill_name, kind_type, recipe_type, event_mask_1, event_mask_2, weapon_request
    ):
        self.skill_id = skill_id
        self.skill_level = skill_level
        if skill_name:
            self.skill_name = skill_name
        self.kind_type = kind_type
        self.recipe_type = recipe_type
        self.event_mask_1 = event_mask_1
        self.event_mask_2 = event_mask_2
        self.weapon_request = weapon_request
        if weapon_request:
            self.weapon_damage_cof = 1024
        self.channel_interval = 16

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
        self.channel_interval = nChannelInterval

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

    def AddAttribute(self, effect_mode, attr_type, *params):
        if not params:
            return

        param = params[0]
        if attr_type == 1:
            self.physical_call += 1
        elif attr_type == 2:
            self.magical_call += 1
        elif attr_type == 3:
            self.surplus_call += 1

        if attr := ATTRIBUTE_TYPE.get(attr_type):
            setattr(self, attr, param)

    def __call__(self, *args, **kwargs):
        pass


def parse_lua(skill_id):
    skill_row = SKILL_TAB[SKILL_TAB.SkillID == skill_id].iloc[0]
    max_level = int(skill_row.MaxLevel)
    kind_type = skill_row.KindType if pd.notna(skill_row.KindType) else ""
    recipe_type = skill_row.RecipeType if pd.notna(skill_row.RecipeType) else 0
    event_mask_1 = int(skill_row.SkillEventMask1) if pd.notna(skill_row.SkillEventMask1) else 0
    event_mask_2 = int(skill_row.SkillEventMask2) if pd.notna(skill_row.SkillEventMask2) else 0
    weapon_request = int(skill_row.WeaponRequest)
    with open(os.path.join(BASE_DIR, SCRIPTS_PATH, skill_row.ScriptFile), encoding="gbk") as f:
        lua_code = remove_include(f.read())
    return max_level, kind_type, recipe_type, event_mask_1, event_mask_2, weapon_request, lua_code


def collect_result():
    result = []
    for skill_id in tqdm(SKILLS):
        max_level, kind_type, recipe_type, event_mask_1, event_mask_2, weapon_request, lua_code = parse_lua(skill_id)
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

            skill = SkillLua(
                skill_id, skill_level, skill_name, kind_type, recipe_type, event_mask_1, event_mask_2, weapon_request
            )
            LUA.globals()['GetSkillLevelData'](skill)
            result.append(skill.__dict__.copy())
    return pd.DataFrame(result)


def convert_json(result):
    exclude_columns = [
        "skill_id", "skill_level", "kind_type", "recipe_type", "event_mask_1", "event_mask_2", "weapon_request"
    ]
    int_columns = ["physical_attack_power_gain", "physical_critical_strike_rate", "physical_critical_power_rate",
                   "magical_attack_power_gain", "magical_critical_strike_rate", "magical_critical_power_rate",
                   "physical_shield_gain", "magical_shield_gain", "all_shield_ignore", "pve_addition",
                   "damage_addition", "physical_call", "magical_call", "surplus_call"]
    result_json = {}
    for skill_id in result.skill_id.unique().tolist():
        filter_result = result[result.skill_id == skill_id]
        first_row = filter_result.iloc[0]
        result_json[skill_id] = dict(
            kind_type=first_row.kind_type, recipe_type=int(first_row.recipe_type),
            event_mask_1=int(first_row.event_mask_1), event_mask_2=int(first_row.event_mask_2),
        )
        for column in result.columns:
            if column in exclude_columns:
                continue
            if filter_result[column].isna().all():
                continue
            if column == "global_damage_cof":
                filter_column = filter_result[column].fillna(-1024 * 1024)
            else:
                filter_column = filter_result[column].fillna(0)
            if column in int_columns:
                filter_column = filter_column.astype(int)
            if filter_column.nunique() == 1:
                result_json[skill_id][column] = filter_column.tolist()[0]
            else:
                result_json[skill_id][column] = filter_column.tolist()

    with open(os.path.join(SAVE_DIR, "skills.py"), "w", encoding="utf-8") as f:
        f.write(f"SKILLS = {json.dumps(result_json, indent=4, ensure_ascii=False)}")


if __name__ == '__main__':
    convert_json(collect_result())
