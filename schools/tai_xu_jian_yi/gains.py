from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain

GAINS = {
    1915: CriticalSet(1438),
    818: damage_addition_recipe([386, 387, 388, 389, 390, 391, 392, 393, 394], 102),
    1522: damage_addition_recipe([386, 387, 388, 389, 390, 391, 392, 393, 394], 51),
    1523: damage_addition_recipe([13853, 4954], 51),
    1135: critical_strike_recipe([386, 387, 388, 389, 390, 391, 392, 393, 394], 500),
    2419: Gain(),
    1932: Gain(),
    17301: Gain(),
    17313: Gain(),
    **EQUIPMENT_GAINS,
}
