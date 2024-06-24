from tqdm import tqdm

from tools import *

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

    physical_damage_call = 0
    magical_damage_call = 0
    adaptive_damage_call = 0
    physical_surplus_call = 0
    magical_surplus_call = 0

    @staticmethod
    def empty_function(*args):
        return

    def __init__(
            self, skill_id, skill_level, skill_name, kind_type, recipe_type, weapon_request, use_skill_cof
    ):
        self.skill_id = skill_id
        self.skill_level = skill_level
        if skill_name:
            self.skill_name = skill_name
        self.kind_type = kind_type
        self.recipe_type = recipe_type
        self.weapon_request = weapon_request
        if weapon_request:
            self.weapon_damage_cof = 1024
        self.use_skill_cof = use_skill_cof
        if use_skill_cof:
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
        if self.use_skill_cof:
            self.channel_interval = nChannelInterval

    @property
    def nPrepareFrames(self):
        return self.prepare_frame

    @nPrepareFrames.setter
    def nPrepareFrames(self, nPrepareFrames):
        if self.use_skill_cof:
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
        if attr_type == 1:
            self.physical_damage_call += 1
        elif attr_type == 2:
            self.magical_damage_call += 1
        elif attr_type == 3:
            self.adaptive_damage_call += 1
        elif attr_type == 4:
            self.physical_surplus_call += 1
        elif attr_type == 5:
            self.magical_surplus_call += 1

        if attr := ATTRIBUTE_TYPE.get(attr_type):
            setattr(self, attr, param)

    def __call__(self, *args, **kwargs):
        pass


def parse_lua(skill_id):
    skill_row = SKILL_TAB[SKILL_TAB.SkillID == skill_id].iloc[0]
    max_level = int(skill_row.MaxLevel)
    kind_type = skill_row.KindType if pd.notna(skill_row.KindType) else ""
    recipe_type = skill_row.RecipeType if pd.notna(skill_row.RecipeType) else 0
    # event_mask_1 = int(skill_row.SkillEventMask1) if pd.notna(skill_row.SkillEventMask1) else 0
    # event_mask_2 = int(skill_row.SkillEventMask2) if pd.notna(skill_row.SkillEventMask2) else 0
    weapon_request = int(skill_row.WeaponRequest)
    use_skill_cof = int(skill_row.UseSkillCoefficient)
    with open(os.path.join(BASE_DIR, SCRIPTS_PATH, skill_row.ScriptFile), encoding="gbk") as f:
        lua_code = remove_include(f.read())
    return max_level, kind_type, recipe_type, weapon_request, use_skill_cof, lua_code


def collect_result():
    result = []
    for skill_id in tqdm(SKILLS):
        max_level, kind_type, recipe_type, weapon_request, use_skill_cof, lua_code = parse_lua(skill_id)
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
                skill_id, skill_level, skill_name, kind_type, recipe_type, weapon_request, use_skill_cof
            )
            LUA.globals()['GetSkillLevelData'](skill)
            if not skill.physical_damage_call and skill.weapon_damage_cof:
                del skill.weapon_damage_cof
            result.append(skill.__dict__.copy())
    return pd.DataFrame(result)


def convert_json(result):
    exclude_columns = [
        "skill_id", "skill_level", "kind_type", "recipe_type", "weapon_request", "use_skill_cof"
    ]
    int_columns = [
        "physical_damage_base", "magical_damage_base", "physical_damage_rand", "magical_damage_rand",
        "physical_attack_power_gain", "physical_critical_strike_rate", "physical_critical_power_rate",
        "magical_attack_power_gain", "magical_critical_strike_rate", "magical_critical_power_rate",
        "physical_shield_gain", "magical_shield_gain", "all_shield_ignore", "pve_addition", "damage_addition",
        "physical_damage_call", "magical_damage_call", "adaptive_damage_call",
        "physical_surplus_call", "magical_surplus_call",
        "physical_attack_power_base", "magical_attack_power_base"
    ]
    result_json = {}
    for skill_id in result.skill_id.unique().tolist():
        filter_result = result[result.skill_id == skill_id]
        first_row = filter_result.iloc[0]
        result_json[skill_id] = dict(
            kind_type=first_row.kind_type, recipe_type=int(first_row.recipe_type)
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

    save_code("skills", result_json)


def generate():
    convert_json(collect_result())


if __name__ == '__main__':
    generate()
