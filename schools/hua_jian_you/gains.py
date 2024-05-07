from base.recipe import attack_power_recipe, damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain

GAINS = {
    1912: CriticalSet(1440),
    817: attack_power_recipe([714], 1.15),
    1546: damage_addition_recipe([33222], 102),
    1516: damage_addition_recipe([14941], 51),
    1517: damage_addition_recipe([33222], 51),
    1131: critical_strike_recipe([14941], 500),
    1979: critical_strike_recipe([33222], 500),
    2417: Gain(),
    1929: Gain(),
    17399: Gain(),
    17400: Gain(),
    **EQUIPMENT_GAINS,
}
