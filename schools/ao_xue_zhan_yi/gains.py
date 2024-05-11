from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain

GAINS = {
    1913: CriticalSet(1428),
    817: damage_addition_recipe([18773, 15002], 102),
    1508: damage_addition_recipe([18207], 51),
    1509: damage_addition_recipe([18603], 51),
    1133: critical_strike_recipe([18773, 15002], 500),
    2424: Gain(),
    1933: Gain(),
    1942: Gain(),
    17362: Gain(),
    17367: Gain(),
    **EQUIPMENT_GAINS,
}
