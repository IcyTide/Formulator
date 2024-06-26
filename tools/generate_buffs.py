from tqdm import tqdm

from assets.constant import ATTR_TYPE_MAP
from tools import *

MAX_ATTRIB = 15


def parse_buff(row, result):
    for i in range(MAX_ATTRIB):
        attr, param_1 = row[f"BeginAttrib{i + 1}"], row[f"BeginValue{i + 1}A"]

        if attr in ATTR_TYPE_MAP:
            result[ATTR_TYPE_MAP[attr]] = int(param_1)


def collect_result():
    results = []
    for buff_id in tqdm(BUFFS):
        filter_buffs = BUFF_TAB[BUFF_TAB.ID == buff_id]
        filter_buff_txt = BUFF_TXT[BUFF_TXT.BuffID == buff_id]
        for _, buff_row in filter_buffs.iterrows():
            result = dict(buff_id=buff_id)
            buff_level = buff_row["Level"]
            max_stack = buff_row["MaxStackNum"]
            if filter_buff_txt.empty:
                pass
            elif buff_level in filter_buff_txt.Level.tolist():
                result['buff_name'] = filter_buff_txt[filter_buff_txt.Level == buff_level].iloc[0].Name
            else:
                result['buff_name'] = filter_buff_txt.iloc[-1].Name
            result["max_stack"] = max_stack
            parse_buff(buff_row, result)
            results.append(result)

    return pd.DataFrame(results)


def convert_json(result):
    exclude_columns = ["buff_id"]
    result_json = {}
    for buff_id in result.buff_id.unique().tolist():
        filter_result = result[result.buff_id == buff_id]
        result_json[buff_id] = {"attributes": {}}
        for column in result.columns:
            if column in exclude_columns:
                continue
            if filter_result[column].isna().all():
                continue

            if filter_result[column].dtype == float:
                filter_column = filter_result[column].fillna(0).astype(int)
                result_dict = result_json[buff_id]["attributes"]
            else:
                filter_column = filter_result[column]
                result_dict = result_json[buff_id]
            if filter_column.nunique() == 1:
                result_dict[column] = filter_column.tolist()[0]
            else:
                result_dict[column] = filter_column.tolist()

    save_code("buffs", result_json)


def generate():
    convert_json(collect_result())


if __name__ == '__main__':
    generate()
