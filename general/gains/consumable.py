from assets.constant import ATTR_TYPE_TRANSLATE
from general.gains import GENERAL_GAINS


def consumable_attribute(gain):
    attributes = {}
    for attr, value in gain.attributes.items():
        if value := gain.attribute_value(values):
            attributes[attr] = value
    return attributes


def consumable_name(name, attributes):
    return f"{name}({''.join(f'{v}{ATTR_TYPE_TRANSLATE[k]}' for k, v in attributes.items())})"


def create_consumable_gain(gain_id, scope: range = None):
    gain = GENERAL_GAINS[gain_id]
    if not scope:
        scope = range(1, gain.max_level + 1)
    result = {}
    for i in scope:
        gain.buff_level = i
        if not gain.attributes:
            continue
        result[consumable_name(gain.buff_name, gain.attributes)] = gain.attributes
    return result


MAJOR_FOODS = create_consumable_gain(24731)
MINOR_FOODS = create_consumable_gain(24732)
MAJOR_POTIONS = create_consumable_gain(24735)
MINOR_POTIONS = create_consumable_gain(24736)
SPREADS = {
    **create_consumable_gain(24733),
    **create_consumable_gain(24734)
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
    "瀑沙熔锭": {"physical_attack_power_base": 658},
    "瀑沙磨石": {"physical_attack_power_base": 439},
    "坠宵熔锭": {"magical_attack_power_base": 786},
    "坠宵磨石": {"magical_attack_power_base": 524}
}
WEAPON_ENCHANTS = {
    consumable_name(k, v): v for k, v in WEAPON_ENCHANTS.items()
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
