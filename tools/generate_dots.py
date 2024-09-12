from tqdm import tqdm

from kungfus import SUPPORT_KUNGFU
from tools import *
from tools.generate_buffs import BUFF_TAB, BUFF_TXT


def prepare_dots():
    dots = []
    for kungfu in SUPPORT_KUNGFU.values():
        for dot_id in kungfu.dots:
            if dot_id in dots:
                continue
            dots.append(dot_id)
    return dots


MAX_ATTRIB = 2


def parse_dot(row):
    result = dict(
        interval=row.Interval, tick=row.Count, max_stack=row.MaxStackNum, platform=row.Platform
    )
    for i in range(MAX_ATTRIB):
        attr, param_1 = row[f"ActiveAttrib{i + 1}"], row[f"ActiveValue{i + 1}A"]

        if attr == "atCallPhysicsDamage":
            result["damage_base"] = int(param_1)
            result["physical_damage_call"] = 1
        elif attr == "atCallSolarDamage":
            result["damage_base"] = int(param_1)
            result["solar_damage_call"] = 1
        elif attr == "atCallLunarDamage":
            result["damage_base"] = int(param_1)
            result["lunar_damage_call"] = 1
        elif attr == "atCallNeutralDamage":
            result["damage_base"] = int(param_1)
            result["neutral_damage_call"] = 1
        elif attr == "atCallPoisonDamage":
            result["damage_base"] = int(param_1)
            result["poison_damage_call"] = 1
        # elif attr in ATTR_TYPE_MAP:
        #     if "attributes" not in result:
        #         result["attributes"] = {}
        #     result["attributes"][ATTR_TYPE_MAP[attr]] = int(param_1)
        # elif attr == "atSetTalentRecipe":
        #     if "gains" not in result:
        #         result["gains"] = {}
        #     result["gains"][int(param_1)] = int(param_2)

    return result


def collect_result():
    result = []
    for buff_id in tqdm(prepare_dots()):
        filter_dots = BUFF_TAB[BUFF_TAB.ID == buff_id]
        filter_dot_txt = BUFF_TXT[BUFF_TXT.BuffID == buff_id]
        for _, buff_row in filter_dots.iterrows():
            alias_name = buff_row["Name"]
            buff_level = buff_row["Level"]
            if filter_dot_txt.empty:
                buff_name = ""
            elif buff_level in filter_dot_txt.Level.tolist():
                buff_name = filter_dot_txt[filter_dot_txt.Level == buff_level].iloc[0].Name
            else:
                buff_name = filter_dot_txt.iloc[-1].Name
            buff_name += "(DOT)"

            result.append(dict(buff_id=buff_id, buff_name=buff_name, alias_name=alias_name, **parse_dot(buff_row)))

    return pd.DataFrame(result)


def convert_json(result):
    exclude_columns = ["buff_id"]
    result_json = {}
    for buff_id in result.buff_id.unique().tolist():
        filter_result = result[result.buff_id == buff_id]
        result_json[buff_id] = {}
        for column in result.columns:
            if column in exclude_columns:
                continue
            if filter_result[column].isna().all():
                continue
            if filter_result[column].dtype == float:
                filter_column = filter_result[column].fillna(0).astype(int)
            else:
                filter_column = filter_result[column]
            if filter_column.nunique() == 1:
                result_json[buff_id][column] = filter_column.tolist()[0]
            else:
                result_json[buff_id][column] = filter_column.tolist()

    save_code("dots", result_json)


def generate():
    convert_json(collect_result())


if __name__ == '__main__':
    generate()
