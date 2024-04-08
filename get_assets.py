import json
import os
from functools import cache

import requests
from tqdm import tqdm

from qt.constant import MAX_BASE_ATTR, MAX_MAGIC_ATTR, MAX_EMBED_ATTR, MAX_ENCHANT_ATTR, MAX_STONE_ATTR, \
    MAX_STONE_LEVEL, ATTR_TYPE_MAP, ATTR_TYPE_TRANSLATE, STONE_ATTR
from qt.constant import EQUIPMENTS_DIR, ENCHANTS_DIR, STONES_DIR

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
    "tertiary_weapon": 1,
    "primary_weapon": 0
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
    "3": {
        12800: "15436-11",
        11500: "15436-10",
        10600: "15436-9"
    },
    "2": {
        12800: "22151-11",
        11500: "22151-10",
        10600: "22151-9"
    },
    "6": {
        0: "22169"
    },
    "10": {
        0: "22166"
    },
    "9": {
        0: "33247"
    },
}

equip_min_level = 11000
equip_params = {
    "client": "std",
    "pv_type": 1,
    "pz": 1,
    "page": 1,
    "per": 300,
    "min_level": 9000,
    "max_level": 15000
}

enchant_params = {
    "client": "std",
    "subtype": 1,
    "latest_enhance": 1
}


# @cache
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
    return equips


@cache
def get_enchants_list(position):
    position_id = POSITION_MAP[position]
    url = f"https://node.jx3box.com/enchant/primary"
    params = enchant_params.copy()
    params['position'] = position_id
    res = requests.get(url, params=params)
    enchants = [e for e in sorted(res.json(), key=lambda x: x['Score'], reverse=True) if
                e['Attribute1ID'] in ATTR_TYPE_MAP]
    return enchants


def get_stones_list():
    url = "https://node.jx3box.com/enchant/stone"

    result = {}
    for level in tqdm(range(MAX_STONE_LEVEL)):
        level = level + 1
        stones = []
        params = {
            "client": "std",
            "level": level,
            "page": 1,
            "per": 100
        }
        res = requests.get(url, params=params).json()
        stones.extend(res['list'])
        while res['pages'] > params['page']:
            params['page'] += 1
            res = requests.get(url, params=params).json()
            stones.extend(res['list'])

    return result


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

    json.dump(get_stones_list(), open(STONES_DIR, "w", encoding="utf-8"), ensure_ascii=False)
