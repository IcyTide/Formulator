from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain


GAINS = {
    1919: CriticalSet(3401),
    946: damage_addition_recipe([3095, 37504], 102),
    1969: damage_addition_recipe([3227], 102),
    1534: damage_addition_recipe([3095, 37504], 51),
    1535: damage_addition_recipe([3227], 51),
    1145: critical_strike_recipe([3095, 37504], 500),
    1978: critical_strike_recipe([3227], 500),
    2411: Gain(),
    1936: Gain(),
    17435: Gain(),
    17436: Gain(),
    **EQUIPMENT_GAINS,
}
