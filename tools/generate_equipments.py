import json
import os
from functools import cache

import pandas as pd
import requests
from tqdm import tqdm

from assets.constant import MAX_BASE_ATTR, MAX_MAGIC_ATTR, MAX_EMBED_ATTR, MAX_ENCHANT_ATTR, STONES_DIR
from assets.constant import ATTR_TYPE_MAP, ATTR_TYPE_TRANSLATE
from assets.constant import MAX_STONE_ATTR, MAX_STONE_LEVEL
from assets.constant import EQUIPMENTS_DIR, ENCHANTS_DIR
from schools import SUPPORT_SCHOOLS
from tools import *

KINDS = set(sum([[school.kind, school.major] for school in SUPPORT_SCHOOLS.values()], []))
SCHOOLS = set(["精简", "通用"] + [school.school for school in SUPPORT_SCHOOLS.values()])

EQUIP_ATTR_MAP = {
    "Overcome": "破防",
    "Critical": "会心",
    "CriticalDamage": "会效",
    "Haste": "加速",
    "Surplus": "破招",
    "Strain": "无双"
}

POSITION_MAP = {
    "hat": 3,
    "jacket": 2,
    "belt": 6,
    "wrist": 10,
    "bottoms": 8,
    "shoes": 9,
    "necklace": 4,
    "pendant": 7,
    "ring": 5,
    "tertiary_weapon": 1
}

SUFFIX_MAP = {
    3: 'armor',
    2: 'armor',
    6: 'armor',
    10: 'armor',
    8: 'armor',
    9: 'armor',
    4: 'trinket',
    7: 'trinket',
    5: 'trinket',
    1: 'weapon',
    0: 'weapon'
}
SPECIAL_ENCHANT_MAP = {
    3: {
        14350: [15436, 12],
        12800: [15436, 11],
        11500: [15436, 10],
        10600: [15436, 9]
    },
    2: {
        14350: [22151, 12],
        12800: [22151, 11],
        11500: [22151, 10],
        10600: [22151, 9]
    },
    6: {
        0: 22169
    },
    10: {
        0: 22166
    },
    9: {
        0: 33247
    }
}

equip_min_level = 12000
equip_params = {
    "client": "std",
    "pv_type": 1,
    "pz": 1,
    "page": 1,
    "per": 300,
    "min_level": 9000,
    "max_level": 17000
}

enchant_params = {
    "client": "std",
    "subtype": 1,
    "latest_enhance": 1
}


def filter_equips(result):
    result = {k: v for k, v in result.items() if v['level'] >= equip_min_level or v['max_strength'] == 8}
    result = {k: v for k, v in result.items() if v['kind'] in KINDS and v['school'] in SCHOOLS}
    return result


def get_equips_list(position):
    position_id = POSITION_MAP[position]
    url = f"https://node.jx3box.com/equip/{SUFFIX_MAP[position_id]}"
    params = equip_params.copy()
    params['position'] = position_id
    equips = []
    res = requests.get(url, params=params).json()
    equips.extend(res['list'])
    while res['pages'] > params['page']:
        params['page'] += 1
        res = requests.get(url, params=params).json()
        equips.extend(res['list'])

    result = {get_equip_name(row): get_equip_detail(row) for row in reversed(equips)}
    result = filter_equips(result)
    return result


def get_weapon_equips():
    params = equip_params.copy()
    params['position'] = 0

    url = f"https://node.jx3box.com/equip/weapon"
    equips = []
    res = requests.get(url, params=params).json()
    equips.extend(res['list'])
    while res['pages'] > params['page']:
        params['page'] += 1
        res = requests.get(url, params=params).json()
        equips.extend(res['list'])
    primary_weapon_result, secondary_weapon_result = {}, {}
    for row in reversed(equips):
        if row['DetailType'] == 9:
            secondary_weapon_result[get_equip_name(row)] = get_equip_detail(row)
        else:
            primary_weapon_result[get_equip_name(row)] = get_equip_detail(row)
    primary_weapon_result = filter_equips(primary_weapon_result)
    secondary_weapon_result = filter_equips(secondary_weapon_result)
    return primary_weapon_result, secondary_weapon_result


def get_equip_name(row):
    name = row['Name']
    attrs = " ".join([EQUIP_ATTR_MAP[attr] for attr in EQUIP_ATTR_MAP if attr in row['_Attrs']])
    level = row['Level']
    return f"{name}#{row['ID']}({attrs}) {level}"


def get_equip_detail(row):
    base_attrs, magic_attrs, embed_attrs = {}, {}, {}
    set_id, set_attr, set_gain = "", {}, {}
    level = int(row['Level'])
    special_enchant = []
    gains = []
    for i in range(MAX_BASE_ATTR):
        if not (attr_type := row[f'Base{i + 1}Type']):
            break
        if attr_type not in ATTR_TYPE_MAP:
            continue
        base_attrs[ATTR_TYPE_MAP[attr_type]] = int(row[f'Base{i + 1}Max'])
    for i in range(MAX_MAGIC_ATTR):
        if not (attr := row[f'_Magic{i + 1}Type']):
            break
        attr = attr['attr']
        if attr[0] in ATTR_TYPE_MAP:
            magic_attrs[ATTR_TYPE_MAP[attr[0]]] = int(attr[1])
        elif attr[0] in ["atSetEquipmentRecipe", "atSkillEventHandler"]:
            gains.append(int(attr[1]))
        else:
            continue
    for i in range(MAX_EMBED_ATTR):
        if not (attr := row[f'_DiamondAttributeID{i + 1}']):
            break
        if attr[0] not in ATTR_TYPE_MAP:
            continue
        embed_attrs[ATTR_TYPE_MAP[attr[0]]] = int(attr[1])

    for k, v in SPECIAL_ENCHANT_MAP.get(row['SubType'], {}).items():
        if level > k:
            special_enchant = v
            break

    if row["SkillID"]:
        gains.append((int(row['SkillID']), int(row['SkillLevel'])))

    if set_id := row['_SetAttrbs']:
        set_id = set_id['UiID']
        for k, v in row['_SetData'].items():
            if not v:
                continue
            count = k.split("_")[0]
            attr = v['attr']
            if attr[0] in ATTR_TYPE_MAP:
                if count not in set_attr:
                    set_attr[count] = {}
                set_attr[count][ATTR_TYPE_MAP[attr[0]]] = int(attr[1])
            elif attr[0] in ["atSetEquipmentRecipe", "atSkillEventHandler"]:
                if count not in set_gain:
                    set_gain[count] = []
                set_gain[count].append(int(attr[1]))
    return {
        "id": row["ID"],
        "school": row['BelongSchool'],
        "kind": row['MagicKind'],
        "level": level,
        "max_strength": int(row['MaxStrengthLevel']),
        "base": base_attrs,
        "magic": magic_attrs,
        "embed": embed_attrs,
        "gains": gains,
        "special_enchant": special_enchant,
        "set_id": set_id,
        "set_attr": set_attr,
        "set_gain": set_gain
    }


@cache
def get_enchants_list(position):
    position_id = POSITION_MAP[position]
    url = f"https://node.jx3box.com/enchant/primary"
    params = enchant_params.copy()
    params['position'] = position_id
    res = requests.get(url, params=params)
    enchants = [e for e in sorted(res.json(), key=lambda x: x['Score'], reverse=True) if
                e['Attribute1ID'] in ATTR_TYPE_MAP]

    result = {get_enchant_name(row): get_enchant_detail(row) for row in enchants}

    return result


def get_weapon_enchants():
    position_id = 0
    url = f"https://node.jx3box.com/enchant/primary"
    params = enchant_params.copy()
    params['position'] = position_id
    res = requests.get(url, params=params)
    enchants = [e for e in sorted(res.json(), key=lambda x: x['Score'], reverse=True) if
                e['Attribute1ID'] in ATTR_TYPE_MAP]

    weapon_enchants = {get_enchant_name(row): get_enchant_detail(row) for row in enchants}
    return weapon_enchants, weapon_enchants


def get_enchant_name(row):
    if not row:
        return ""
    name = row['Name']
    attr = row['AttriName']
    return f"{name} {attr}"


def get_enchant_detail(row):
    attrs = {}
    for i in range(MAX_ENCHANT_ATTR):
        if not (attr_type := row[f'Attribute{i + 1}ID']):
            break
        if attr_type not in ATTR_TYPE_MAP:
            continue
        attrs[ATTR_TYPE_MAP[attr_type]] = int(row[f'Attribute{i + 1}Value1'])
    return {
        "id": row['ID'],
        "score": row['Score'],
        "attr": attrs
    }


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
    stone_tab = ENCHANT_TAB[pd.notna(ENCHANT_TAB.DiamondType1)].fillna("")

    for row in stone_tab.itertuples():
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
            if attr not in node:
                node[attr] = {}
            node = node[attr]
            attributes[attr] = int(value)
        node[level] = dict(level=int(level), attr=attributes)
    return result


def generate():
    equipments = {}
    enchants = {}
    for pos in tqdm(POSITION_MAP):
        equipments[pos] = get_equips_list(pos)
        enchants[pos] = get_enchants_list(pos)
    equipments["primary_weapon"], equipments["secondary_weapon"] = get_weapon_equips()
    enchants["primary_weapon"], enchants["secondary_weapon"] = get_weapon_enchants()



if __name__ == '__main__':
    if not os.path.exists(EQUIPMENTS_DIR):
        os.makedirs(EQUIPMENTS_DIR)
    if not os.path.exists(ENCHANTS_DIR):
        os.makedirs(ENCHANTS_DIR)

    for pos in tqdm(POSITION_MAP):
        json.dump(
            get_equips_list(pos),
            open(os.path.join(EQUIPMENTS_DIR, pos), "w", encoding="utf-8"), ensure_ascii=False
        )
        json.dump(
            get_enchants_list(pos),
            open(os.path.join(ENCHANTS_DIR, pos), "w", encoding="utf-8"), ensure_ascii=False
        )
    get_weapon_equips()
    get_weapon_enchants()

    json.dump(get_stones_list(), open(STONES_DIR, "w", encoding="utf-8"), ensure_ascii=False)
