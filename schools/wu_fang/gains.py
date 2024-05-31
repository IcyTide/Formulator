from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.wu_fang.buffs import BUFFS

GAINS = {
    2125: CriticalSet(21758, BUFFS[21758].gain_attributes),
    2839: damage_addition_recipe([27557], 102),
    2840: damage_addition_recipe([27552], 102),
    2842: damage_addition_recipe([27557], 51),
    2843: damage_addition_recipe([27555], 51),
    2841: critical_strike_recipe([27557], 500),
    2414: Gain(),
    2138: Gain(),
    17458: Gain(),
    17459: Gain(),
    **EQUIPMENT_GAINS,
}
