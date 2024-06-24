from tqdm import tqdm

from tools import *

MAX_ATTRIB = 2


def parse_dot(row):
    result = dict(
        interval=row["Interval"], tick=row["Count"], max_stack=row["MaxStackNum"]
    )
    for i in range(MAX_ATTRIB):
        attr, param_1 = row[f"ActiveAttrib{i + 1}"], row[f"ActiveValue{i + 1}A"]

        if attr == "atCallPhysicsDamage":
            result["damage_base"] = int(param_1)
            result["physical_damage_call"] = 1
        elif attr in ["atCallSolarDamage", "atCallLunarDamage", "atCallNeutralDamage", "atCallPoisonDamage"]:
            result["damage_base"] = int(param_1)
            result["magical_damage_call"] = 1
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
    for skill_id in tqdm(DOTS):
        filter_skills = BUFF_TAB[BUFF_TAB.ID == skill_id]
        filter_skill_txt = BUFF_TXT[BUFF_TXT.BuffID == skill_id]
        for _, skill_row in filter_skills.iterrows():
            skill_level = skill_row["Level"]
            if filter_skill_txt.empty:
                skill_name = ""
            elif skill_level in filter_skill_txt.Level.tolist():
                skill_name = filter_skill_txt[filter_skill_txt.Level == skill_level].iloc[0].Name
            else:
                skill_name = filter_skill_txt.iloc[-1].Name
            skill_name += "(DOT)"

            result.append(dict(skill_id=skill_id, skill_name=skill_name, **parse_dot(skill_row)))

    return pd.DataFrame(result)


def convert_json(result):
    exclude_columns = ["skill_id"]
    result_json = {}
    for skill_id in result.skill_id.unique().tolist():
        filter_result = result[result.skill_id == skill_id]
        result_json[skill_id] = {}
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
                result_json[skill_id][column] = filter_column.tolist()[0]
            else:
                result_json[skill_id][column] = filter_column.tolist()

    save_code("dots", result_json)


def generate():
    convert_json(collect_result())


if __name__ == '__main__':
    generate()
