from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain


GAINS = {
    1918: CriticalSet(3401),
    947: damage_addition_recipe([36502, 30894, 30727], 205),
    4120: damage_addition_recipe([3228], 102),
    1532: damage_addition_recipe([3105], 51),
    1533: damage_addition_recipe([36502, 30894, 30727], 51),
    1146: critical_strike_recipe([3105], 500),
    1978: critical_strike_recipe([3228], 500),
    2412: Gain(),
    1935: Gain(),
    17429: Gain(),
    17430: Gain(),
    **EQUIPMENT_GAINS,
}
