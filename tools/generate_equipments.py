from collections import defaultdict

import pandas as pd
from tqdm import tqdm

from assets.constant import ATTR_TYPE_MAP, MAX_SET_COUNT, MAX_SET_ATTR, SPECIAL_ENCHANT_MAP
from assets.constant import MAX_BASE_ATTR, MAX_MAGIC_ATTR, MAX_EMBED_ATTR
from schools import SUPPORT_SCHOOLS
from tools import *

KINDS = set(sum([[school.kind, school.major] for school in SUPPORT_SCHOOLS.values()], []))
SCHOOLS = set(["精简", "通用"] + [school.school for school in SUPPORT_SCHOOLS.values()])

QUALITY_COF = {
    4: 1.8,
    5: 2.5
}
POSITION_COF = {
    0: 1.2,
    1: 0.6,
    2: 1,
    3: 0.9,
    4: 0.5,
    5: 0.5,
    6: 0.7,
    7: 0.5,
    8: 1,
    9: 0.7,
    10: 0.7,
}

ENCHANT_TAB = pd.read_csv(os.path.join(BASE_DIR, "settings/item/Enchant.tab"), sep="\t", low_memory=False,
                          encoding="gbk").fillna(0)
WEAPON_TAB = pd.read_csv(os.path.join(BASE_DIR, "settings/item/Custom_Weapon.tab"), sep="\t", low_memory=False,
                         encoding="gbk").fillna(0)
ARMOR_TAB = pd.read_csv(os.path.join(BASE_DIR, "settings/item/Custom_Armor.tab"), sep="\t", low_memory=False,
                        encoding="gbk").fillna(0)
TRINKET_TAB = pd.read_csv(os.path.join(BASE_DIR, "settings/item/Custom_Trinket.tab"), sep="\t", low_memory=False,
                          encoding="gbk").fillna(0)
ATTRIB_TAB = pd.read_csv(os.path.join(BASE_DIR, "settings/item/Attrib.tab"), sep="\t", low_memory=False, encoding="gbk")
SET_TAB = pd.read_csv(os.path.join(BASE_DIR, "settings/item/Set.tab"), sep="\t", low_memory=False,
                      encoding="gbk").fillna(0)
ARMOR_TAB['Score'] = ARMOR_TAB.apply(
    lambda x: round(x['Level'] * QUALITY_COF.get(x['Quality'], 0) * POSITION_COF.get(x['SubType'], 0)), axis=1
)
WEAPON_TAB['Score'] = WEAPON_TAB.apply(
    lambda x: round(x['Level'] * QUALITY_COF.get(x['Quality'], 0) * POSITION_COF.get(x['SubType'], 0)), axis=1
)
TRINKET_TAB['Score'] = TRINKET_TAB.apply(
    lambda x: round(x['Level'] * QUALITY_COF.get(x['Quality'], 0) * POSITION_COF.get(x['SubType'], 0)), axis=1
)

MIN_EQUIP_LEVEL = 12100
ENCHANT_START_ID = 11869
MIN_EQUIP_SCORE = {
    k: round(MIN_EQUIP_LEVEL * QUALITY_COF[4] * v) for k, v in POSITION_COF.items()
}
ATTR_ABBR = {
    "overcome_base": "破防",
    "critical_strike_base": "会心",
    "critical_power_base": "会效",
    "haste_base": "加速",
    "surplus_base": "破招",
    "strain_base": "无双"
}

POSITION_MAP = {
    0: "primary_weapon",
    1: "tertiary_weapon",
    2: "jacket",
    3: "hat",
    4: "necklace",
    5: "ring",
    6: "belt",
    7: "pendant",
    8: "bottoms",
    9: "shoes",
    10: "wrist",
}
SECONDARY_WEAPON_DETAIL_TYPE = 9


def get_equip_name(detail):
    abbrs = []
    for attr in detail['magic']:
        for k, v in ATTR_ABBR.items():
            if k in attr:
                abbrs.append(v)
                break
    return f"{detail['name']}#{detail['id']}({' '.join(abbrs)}) {detail['level']}"


def get_equip_detail(row):
    detail = {
        "id": row.ID, "name": row.Name, "school": row.BelongSchool, "kind": row.MagicKind, "level": int(row.Level),
        "max_strength": int(row.MaxStrengthLevel), "special_enchant": 0, "set_id": 0,
    }
    detail['base'] = base_attrs = {}
    detail['magic'] = magic_attrs = {}
    detail['embed'] = embed_attrs = {}
    detail['gains'] = gains = []
    detail['set_attr'] = set_attr = defaultdict(dict)
    detail['set_gain'] = set_gain = defaultdict(list)
    for i in range(MAX_BASE_ATTR):
        if not (attr_type := getattr(row, f'Base{i + 1}Type')):
            break
        if attr_type not in ATTR_TYPE_MAP:
            continue
        base_attrs[ATTR_TYPE_MAP[attr_type]] = int(getattr(row, f'Base{i + 1}Max'))
    for i in range(MAX_MAGIC_ATTR):
        if not (attr_id := getattr(row, f'Magic{i + 1}Type')):
            break
        attr_row = ATTRIB_TAB[ATTRIB_TAB.ID == attr_id].iloc[0]
        attr, value = attr_row.ModifyType, int(attr_row.Param1Max)
        if attr in ATTR_TYPE_MAP:
            magic_attrs[ATTR_TYPE_MAP[attr]] = value
        elif attr == "atSetEquipmentRecipe":
            gains.append(value)
        elif attr == "atSkillEventHandler":
            gains.append([value])
        else:
            continue
    for i in range(MAX_EMBED_ATTR):
        if not (attr_id := getattr(row, f'DiamondAttributeID{i + 1}')):
            break
        attr_row = ATTRIB_TAB[ATTRIB_TAB.ID == attr_id].iloc[0]
        attr, value = attr_row.ModifyType, int(attr_row.Param1Max)
        if attr not in ATTR_TYPE_MAP:
            continue
        embed_attrs[ATTR_TYPE_MAP[attr]] = value

    for k, v in SPECIAL_ENCHANT_MAP.get(row.SubType, {}).items():
        if detail['level'] > k:
            detail['special_enchant'] = v
            break

    if row.SkillID:
        gains.append([int(row.SkillID), int(row.SkillLevel)])

    if not row.SetID:
        return detail
    detail['set_id'] = int(row.SetID)
    set_row = SET_TAB[SET_TAB.ID == row.SetID].iloc[0]
    for i in range(1, MAX_SET_COUNT):
        for j in range(MAX_SET_ATTR):
            if attr_id := getattr(set_row, f"{i + 1}_{j + 1}"):
                attr_row = ATTRIB_TAB[ATTRIB_TAB.ID == attr_id].iloc[0]
                attr, value = attr_row.ModifyType, int(attr_row.Param1Max)
                if attr in ATTR_TYPE_MAP:
                    set_attr[i + 1][ATTR_TYPE_MAP[attr]] = value
                elif attr == "atSetEquipmentRecipe":
                    set_gain[i + 1].append(value)
                elif attr == "atSkillEventHandler":
                    set_gain[i + 1].append([value])
                else:
                    continue
    return detail


def get_equip_list(equip_tab):
    equip_tab = equip_tab[
        equip_tab.apply(lambda x: x['Score'] >= MIN_EQUIP_SCORE.get(x['SubType'], float("inf")), axis=1)]
    equip_tab = equip_tab[(equip_tab.MagicKind.isin(KINDS)) & (equip_tab.BelongSchool.isin(SCHOOLS))]
    equip_tab = equip_tab[(~equip_tab.MagicType.str.contains("PVP")) & (~equip_tab.MagicType.str.contains("PVX"))]
    equip_tab = equip_tab.sort_values("Score", ascending=False)

    results = defaultdict(dict)
    for row in tqdm(equip_tab.itertuples()):
        detail = get_equip_detail(row)
        name = get_equip_name(detail)
        position = POSITION_MAP[row.SubType]
        results[position][name] = detail
    return results


def get_weapon_list():
    return {
        **get_equip_list(WEAPON_TAB[WEAPON_TAB.DetailType != SECONDARY_WEAPON_DETAIL_TYPE]),
        "secondary_weapon": get_equip_list(
            WEAPON_TAB[WEAPON_TAB.DetailType == SECONDARY_WEAPON_DETAIL_TYPE]
        )['primary_weapon']
    }


def get_enchants_list():
    enchant_tab = ENCHANT_TAB[ENCHANT_TAB.ID >= ENCHANT_START_ID].sort_values("Score", ascending=False)
    results = defaultdict(dict)
    for row in tqdm(enchant_tab.itertuples()):
        if row.Time or row.Attribute1ID not in ATTR_TYPE_MAP:
            continue
        name = f"{row.Name} {row.AttriName}"
        position = POSITION_MAP[row.DestItemSubType]
        results[position][name] = dict(id=row.ID, score=int(row.Score), attr={
            ATTR_TYPE_MAP[row.Attribute1ID]: int(row.Attribute1Value1)
        })

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
    save_code("equipments", {
        **get_equip_list(ARMOR_TAB),
        **get_equip_list(TRINKET_TAB),
        **get_weapon_list()
    })
    save_code("enchants", get_enchants_list())
    save_code("stones", get_stones_list())


if __name__ == '__main__':
    generate()
