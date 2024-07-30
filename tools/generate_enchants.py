from collections import defaultdict

import pandas as pd
from tqdm import tqdm

from assets.constant import ATTR_TYPE_MAP, TARGET_ATTR_TYPE_MAP
from tools import *
from tools.generate_equipments import POSITION_MAP

ENCHANT_TAB = pd.read_csv(os.path.join(BASE_DIR, "settings/item/Enchant.tab"), sep="\t", low_memory=False,
                          encoding="gbk").fillna(0)

ENCHANT_START_ID = 11869


def get_enchants_list():
    enchant_tab = ENCHANT_TAB[ENCHANT_TAB.ID >= ENCHANT_START_ID].sort_values("Score", ascending=False)
    results = defaultdict(dict)
    for row in tqdm(enchant_tab.itertuples()):
        if row.Time or row.Attribute1ID not in ATTR_TYPE_MAP or row.Attribute1ID in TARGET_ATTR_TYPE_MAP:
            continue
        name = f"{row.Name} {row.AttriName}"
        position = POSITION_MAP[row.DestItemSubType]
        results[position][name] = dict(id=row.ID, score=int(row.Score), attr={
            ATTR_TYPE_MAP[row.Attribute1ID]: int(row.Attribute1Value1)
        })
    results["secondary_weapon"] = results["primary_weapon"]
    return results


def get_stones_list():
    stone_level_mapping = {
        "(壹)": "1",
        "(贰)": "2",
        "(叁)": "3",
        "(肆)": "4",
        "(伍)": "5",
        "(陆)": "6"
    }
    result = {}
    stone_tab = ENCHANT_TAB[ENCHANT_TAB.DiamondType1 > 0]

    for row in tqdm(stone_tab.itertuples()):
        name = row.Name
        level = ""
        for key in stone_level_mapping:
            if key in name:
                level = stone_level_mapping[key]
                break
        attrs = row.Attribute1ID, row.Attribute2ID, row.Attribute3ID
        if any(attr and attr not in ATTR_TYPE_MAP for attr in attrs):
            continue
        values = row.Attribute1Value1, row.Attribute2Value1, row.Attribute3Value1
        node = result
        attributes = {}
        for attr, value in zip(attrs, values):
            if not attr:
                break
            attr = ATTR_TYPE_MAP[attr]
            if attr not in node:
                node[attr] = {}
            node = node[attr]
            attributes[attr] = int(value)
        node[level] = dict(level=int(level), attr=attributes)
    return result


def generate():
    save_code("enchants", get_enchants_list())
    save_code("stones", get_stones_list())


if __name__ == '__main__':
    generate()
