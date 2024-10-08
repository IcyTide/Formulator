from assets.constant import ATTR_TYPE_TRANSLATE
from assets.enchants import ENCHANTS
from general.buffs import GENERAL_BUFFS


def consumable_name(name, attributes):
    return f"{name}({'/'.join(f'{v}{ATTR_TYPE_TRANSLATE[k]}' for k, v in attributes.items())})"


def create_consumable_gain(buff_id, scope: range = None):
    buff = GENERAL_BUFFS[-buff_id]
    if not scope:
        scope = range(1, buff.max_level + 1)
    result = {}
    for i in scope:
        buff.buff_level = i
        if not buff.attributes:
            continue
        result[consumable_name(buff.buff_name, buff.attributes)] = buff.attributes
    return result


MAJOR_FOODS = create_consumable_gain(29274)
MINOR_FOODS = create_consumable_gain(29276)
MAJOR_POTIONS = create_consumable_gain(29288)
MINOR_POTIONS = create_consumable_gain(29289)
SPREADS = {
    **create_consumable_gain(29284),
    **create_consumable_gain(29285)
}
SNACKS = {
    **create_consumable_gain(17365, range(56, 60 + 1)),
    **{k: v for gain_id in range(27784, 27792 + 1) for k, v in create_consumable_gain(gain_id).items()}
}
WINES = {
    k: v for gain_id in range(17347 + 2, 17364 + 1, 3) for k, v in create_consumable_gain(gain_id).items()
}
BOILED_FISH = create_consumable_gain(10100)
GUILD_FOOD = create_consumable_gain(2563)
GUILD_SPREAD = create_consumable_gain(18428)

WEAPON_ENCHANTS = {
    consumable_name(k, v): v for k, v in ENCHANTS.get("consumable", {}).items()
}
CONSUMABLES = {
    **MAJOR_FOODS,
    **MINOR_FOODS,
    **MAJOR_POTIONS,
    **MINOR_POTIONS,
    **SPREADS,
    **SNACKS,
    **WINES,
    **BOILED_FISH,
    **GUILD_FOOD,
    **GUILD_SPREAD,
    **WEAPON_ENCHANTS
}
