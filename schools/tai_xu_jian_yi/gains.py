from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain

GAINS = {
    1915: CriticalSet(16025),
    818: damage_addition_recipe([35987], 102),  # 无我无剑
    17250: Gain(),
    1522: damage_addition_recipe([35987], 51),  # 无我无剑
    1523: damage_addition_recipe([35987], 51),  # 八荒归元
    1135: critical_strike_recipe([36157], 500),  # 无我无剑
    2419: Gain(),
    1932: Gain(),
    17301: Gain(),
    17239: Gain(),
    17313: Gain(),
    **EQUIPMENT_GAINS,
}
