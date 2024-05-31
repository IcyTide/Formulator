from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.zi_xia_gong.buffs import BUFFS

GAINS = {
    1914: CriticalSet(1439, BUFFS[1439].gain_attributes),
    818: damage_addition_recipe([18649, 18650, 18651, 18652, 18653, 22014], 102),
    4602: Gain(),
    1520: damage_addition_recipe([896], 51),
    1521: Gain(),
    1136: critical_strike_recipe([896], 500),
    2418: Gain(),
    1931: Gain(),
    17300: Gain(),
    17312: Gain(),
    **EQUIPMENT_GAINS,
}
