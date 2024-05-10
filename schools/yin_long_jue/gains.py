from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain

GAINS = {
    1927: CriticalSet(16025),
    5037: damage_addition_recipe([22604, 22605, 36267, 36268], 102),
    5038: damage_addition_recipe([22621, 22620], 102),
    5091: damage_addition_recipe([22170, 22550, 22551, 22298], 51),
    5092: damage_addition_recipe([22604, 22605, 36267, 36268], 51),
    5093: critical_strike_recipe([22604, 22605, 36267, 36268], 500),
    (36726, 1): Gain(),
    17348: Gain(),
    2428: Gain(),
    1944: Gain(),
    17324: Gain(),
    17330: Gain(),
    **EQUIPMENT_GAINS,
}
