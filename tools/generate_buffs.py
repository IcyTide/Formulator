import pandas as pd
from tqdm import tqdm

from assets.constant import ATTR_TYPE_MAP
from base.buff import CustomBuff
from general.gains import GENERAL_GAINS
from schools import SUPPORT_SCHOOLS
from tools import *


def prepare_buffs():
    buffs = []
    for school in SUPPORT_SCHOOLS.values():
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
    return buffs


BUFFS = prepare_buffs()

BUFF_TAB = pd.read_csv(os.path.join(BASE_DIR, "settings/skill/buff.tab"), sep="\t", low_memory=False, encoding="gbk")
BUFF_TAB['Platform'] = 0
MOBILE_BUFF_TAB = pd.read_csv(os.path.join(BASE_DIR, "settings/skill_mobile/buff.tab"), sep="\t", low_memory=False,
                              encoding="gbk")
MOBILE_BUFF_TAB['Platform'] = 1
BUFF_TAB = pd.concat([BUFF_TAB, MOBILE_BUFF_TAB], axis=0)
BUFF_TXT = pd.read_csv(os.path.join(BASE_DIR, "ui/Scheme/Case/buff.txt"), sep="\t", low_memory=False, encoding="gbk")
MOBILE_BUFF_TXT = pd.read_csv(os.path.join(BASE_DIR, "ui/Scheme/case_mobile/buff.txt"), sep="\t", low_memory=False,
                              encoding="gbk")
BUFF_TXT = pd.concat([BUFF_TXT, MOBILE_BUFF_TXT], axis=0)

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
            result["buff_level"] = buff_level
            parse_buff(buff_row, result)
            results.append(result)

    return pd.DataFrame(results)


def convert_json(result):
    exclude_columns = ["buff_id", "buff_level"]
    result_json = {}
    for buff_id in result.buff_id.unique().tolist():
        filter_result = result[result.buff_id == buff_id]
        result_json[buff_id] = dict(attributes={}, max_level=int(filter_result.buff_level.max()))
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
