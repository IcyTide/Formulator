from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain


GAINS = {
    2568: CriticalSet(16025),
    5438: damage_addition_recipe([35987], 102),
    17250: Gain(),
    5461: damage_addition_recipe([36157], 51),
    5462: damage_addition_recipe([35987], 51),
    5463: critical_strike_recipe([36157], 500),
    2572: Gain(),
    2571: Gain(),
    17470: Gain(),
    17239: Gain(),
    17471: Gain(),
    **EQUIPMENT_GAINS,
}
