from collections import defaultdict

import pandas as pd
from tqdm import tqdm

from assets.constant import ATTR_TYPE_MAP, MIN_EQUIP_LEVEL, SPECIAL_ENCHANT_MAP, TARGET_ATTR_TYPE_MAP
from assets.constant import MAX_BASE_ATTR, MAX_MAGIC_ATTR, MAX_EMBED_ATTR, MAX_SET_COUNT, MAX_SET_ATTR
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

WEAPON_TAB = read_tab("settings/item/Custom_Weapon.tab").fillna(0)
ARMOR_TAB = read_tab("settings/item/Custom_Armor.tab").fillna(0)
TRINKET_TAB = read_tab("settings/item/Custom_Trinket.tab").fillna(0)
ATTRIB_TAB = read_tab("settings/item/Attrib.tab")
SET_TAB = read_tab("settings/item/Set.tab").fillna(0)
ARMOR_TAB['Score'] = ARMOR_TAB.apply(
    lambda x: round(x['Level'] * QUALITY_COF.get(x['Quality'], 0) * POSITION_COF.get(x['SubType'], 0)), axis=1
)
WEAPON_TAB['Score'] = WEAPON_TAB.apply(
    lambda x: round(x['Level'] * QUALITY_COF.get(x['Quality'], 0) * POSITION_COF.get(x['SubType'], 0)), axis=1
)
TRINKET_TAB['Score'] = TRINKET_TAB.apply(
    lambda x: round(x['Level'] * QUALITY_COF.get(x['Quality'], 0) * POSITION_COF.get(x['SubType'], 0)), axis=1
)

MIN_EQUIP_SCORE = {
    k: round(MIN_EQUIP_LEVEL * QUALITY_COF[4] * v) for k, v in POSITION_COF.items()
}
ATTR_ABBR = {
    "overcome_base": "破防",
    "critical_strike_base": "会心",
    "critical_power_base": "会效",
    "haste_base": "加速",
    "surplus_base": "破招",
    "strain_base": "无双",
    "pvx_round": "全能"
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
    if detail['school'] == "精简":
        abbrs = ["精简"]
    elif detail["gains"]:
        abbrs = ["特效"]
    else:
        abbrs = []
    for attr in detail['magic']:
        for k, v in ATTR_ABBR.items():
            if k in attr:
                abbrs.append(v)
                break
    return f"{detail['name']}#{detail['id']} ({detail['level']} {' '.join(abbrs)})"


def get_equip_detail(row):
    detail = {
        "id": row.ID, "name": row.Name, "school": row.BelongSchool, "kind": row.MagicKind, "level": int(row.Level),
        "max_strength": int(row.MaxStrengthLevel), "special_enchant": 0, "set_id": 0,
    }
    detail['base'] = base_attrs = {}
    detail['magic'] = magic_attrs = {}
    detail['embed'] = embed_attrs = {}
    detail['gains'] = gains = []
    detail['recipes'] = recipes = {}
    detail['set_attr'] = set_attr = defaultdict(dict)
    detail['set_gain'] = set_gain = defaultdict(list)
    detail['set_recipe'] = set_recipe = defaultdict(dict)
    for i in range(MAX_BASE_ATTR):
        if not (attr_type := getattr(row, f'Base{i + 1}Type')):
            break
        if attr_type not in ATTR_TYPE_MAP or attr_type in TARGET_ATTR_TYPE_MAP:
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
            recipes[value] = int(attr_row.Param2Max)
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
                    set_recipe[i + 1][value] = int(attr_row.Param2Max)
                elif attr == "atSkillEventHandler":
                    set_gain[i + 1].append([value])
                else:
                    continue
    return detail


def get_equip_list(equip_tab):
    equip_tab = equip_tab[
        equip_tab.apply(lambda x: x['Score'] >= MIN_EQUIP_SCORE.get(x['SubType'], float("inf")), axis=1)]
    equip_tab = equip_tab[(equip_tab.MagicKind.isin(KINDS)) & (equip_tab.BelongSchool.isin(SCHOOLS))]
    # equip_tab = equip_tab[(~equip_tab.MagicType.str.contains("PVP")) & (~equip_tab.MagicType.str.contains("PVX"))]
    equip_tab = equip_tab[~equip_tab.MagicType.str.contains("PVP")]
    equip_tab = equip_tab.sort_values(["Score", "ID"], ascending=False)

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


def generate():
    save_code("equipments", {
        **get_equip_list(ARMOR_TAB),
        **get_equip_list(TRINKET_TAB),
        **get_weapon_list()
    })


if __name__ == '__main__':
    generate()
