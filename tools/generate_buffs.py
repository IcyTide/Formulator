from tqdm import tqdm

from assets.constant import ATTR_TYPE_MAP, BUFF_MAX_ATTRIB
from base.buff import CustomBuff
from kungfus import SUPPORT_KUNGFU
from tools import *


def prepare_buffs():
    buffs = []
    for kungfu in SUPPORT_KUNGFU.values():
        for buff_id, buff in kungfu.buffs.items():
            if isinstance(buff, CustomBuff):
                continue
            buff_id = abs(buff_id)
            if buff_id in buffs:
                continue
            buffs.append(buff_id)
    return buffs


BUFF_TAB = read_tab("settings/skill/buff.tab")
BUFF_TAB['Platform'] = 0
MOBILE_BUFF_TAB = read_tab("settings/skill_mobile/buff.tab")
MOBILE_BUFF_TAB['Platform'] = 1
BUFF_TAB = pd.concat([BUFF_TAB, MOBILE_BUFF_TAB], axis=0)
BUFF_TXT = read_tab("ui/Scheme/Case/buff.txt")
MOBILE_BUFF_TXT = read_tab("ui/Scheme/case_mobile/buff.txt")
BUFF_TXT = pd.concat([BUFF_TXT, MOBILE_BUFF_TXT], axis=0)


class HashDict(dict):
    def __hash__(self):
        return hash(tuple((k, v) for k, v in self.items()))


def parse_buff(row, result):
    result["attributes"] = HashDict()
    result["recipes"] = HashDict()
    for i in range(BUFF_MAX_ATTRIB):
        attr, param_1, param_2 = row[f"BeginAttrib{i + 1}"], row[f"BeginValue{i + 1}A"], row[f"BeginValue{i + 1}B"]

        if attr in ATTR_TYPE_MAP:
            result["attributes"][ATTR_TYPE_MAP[attr]] = int(param_1)
        elif attr == "atSetTalentRecipe":
            result["recipes"][int(param_1)] = int(param_2)


def collect_result():
    results = []
    for buff_id in tqdm(prepare_buffs()):
        filter_buffs = BUFF_TAB[BUFF_TAB.ID == buff_id]
        filter_buff_txt = BUFF_TXT[BUFF_TXT.BuffID == buff_id]
        for _, buff_row in filter_buffs.iterrows():
            result = dict(buff_id=buff_id)
            alias_name = buff_row["Name"]
            buff_level = buff_row["Level"]
            max_stack = buff_row["MaxStackNum"]
            if filter_buff_txt.empty:
                pass
            elif buff_level in filter_buff_txt.Level.tolist():
                result['buff_name'] = filter_buff_txt[filter_buff_txt.Level == buff_level].iloc[0].Name
            else:
                result['buff_name'] = filter_buff_txt.iloc[-1].Name
            result['alias_name'] = alias_name
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
