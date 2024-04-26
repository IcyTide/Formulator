from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain


GAINS = {
    1926: CriticalSet(14353),
    4816: damage_addition_recipe([31250], 102),
    4817: damage_addition_recipe([20684, 20685], 102),
    4818: damage_addition_recipe([19819], 51),
    4819: damage_addition_recipe([20016], 51),
    4820: critical_strike_recipe([19819], 500),
    4821: critical_strike_recipe([20684, 20685], 500),
    2423: Gain(),
    1943: Gain(),
    17409: Gain(),
    17239: Gain(),
    17410: Gain(),
    **EQUIPMENT_GAINS,
}
