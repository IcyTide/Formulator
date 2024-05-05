from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain

GAINS = {
    1916: CriticalSet(1437),
    1547: damage_addition_recipe([6234, 6554], 102),
    1524: damage_addition_recipe([6234, 6554], 51),
    1525: damage_addition_recipe([6559], 51),
    1137: critical_strike_recipe([30524], 500),
    1977: critical_strike_recipe([], 500),  # 剑破
    2416: Gain(),
    1930: Gain(),
    17380: Gain(),
    17381: Gain(),
    **EQUIPMENT_GAINS,
}
