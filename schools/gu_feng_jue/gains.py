from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain


GAINS = {
    1925: CriticalSet(11378),
    3188: damage_addition_recipe([32235, 32236, 32237, 32238, 32239, 32891, 32892], 102),
    3186: damage_addition_recipe([32602, 32603, 32604], 51),
    3187: damage_addition_recipe([32235, 32236, 32237, 32238, 32239, 32891, 32892], 51),
    3185: critical_strike_recipe([32602, 32603, 32604], 500),
    2391: Gain(),
    2392: Gain(),
    17358: Gain(),
    17359: Gain(),
    **EQUIPMENT_GAINS,
}
