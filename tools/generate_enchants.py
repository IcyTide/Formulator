from tqdm import tqdm

from assets.constant import SELF_ATTR_TYPE_MAP, ENCHANT_START_ID
from tools import *
from tools.generate_equipments import POSITION_MAP

ENCHANT_TAB = read_tab("settings/item/Enchant.tab").fillna(0)


def get_enchants_list():
    enchant_tab = ENCHANT_TAB[(ENCHANT_TAB.ID >= ENCHANT_START_ID) & (ENCHANT_TAB.DiamondType1 == 0)]
    enchant_tab = enchant_tab.sort_values(["Score", "ID"], ascending=False)
    results = {"consumable": {}}
    for row in tqdm(enchant_tab.itertuples()):
        if row.Attribute1ID not in SELF_ATTR_TYPE_MAP:
            continue
        name = f"{row.Name} {row.AttriName}"
        position = POSITION_MAP[row.DestItemSubType]
        attr = {SELF_ATTR_TYPE_MAP[row.Attribute1ID]: int(row.Attribute1Value1)}
        if row.Time:
            results["consumable"][name] = attr
        else:
            if position not in results:
                results[position] = {}
            results[position][name] = dict(id=row.ID, score=int(row.Score), attr=attr)
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
        if any(attr and attr not in SELF_ATTR_TYPE_MAP for attr in attrs):
            continue
        values = row.Attribute1Value1, row.Attribute2Value1, row.Attribute3Value1
        node = result
        attributes = {}
        for attr, value in zip(attrs, values):
            if not attr:
                break
            attr = SELF_ATTR_TYPE_MAP[attr]
            if attr not in node:
                node[attr] = {}
            node = node[attr]
            attributes[attr] = int(value)
        if row.TabIndex:
            stone_id = int(row.TabIndex) - 1
        else:
            stone_id = int(stone_tab.loc[row.Index - 1].TabIndex)
        if level in node:
            node[level]['id'].append(stone_id)
        else:
            node[level] = dict(id=[stone_id], name=row.Name, level=int(level), attr=attributes)
    return result


def generate():
    save_code("enchants", get_enchants_list())
    save_code("stones", get_stones_list())


if __name__ == '__main__':
    generate()
