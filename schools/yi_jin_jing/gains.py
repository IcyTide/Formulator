from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain

GAINS = {
    1911: CriticalSet(1436),
    818: damage_addition_recipe([3848, 3849, 3850, 271], 102),
    1147: damage_addition_recipe([13685], 102),
    1512: damage_addition_recipe([17641], 51),
    1513: damage_addition_recipe([3814, 3816], 51),
    1139: critical_strike_recipe([3848, 3849, 3850, 271], 500),
    2410: Gain(),
    1928: Gain(),
    17351: Gain(),
    17352: Gain(),
    **EQUIPMENT_GAINS,
}
