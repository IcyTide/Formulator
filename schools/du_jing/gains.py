from base.recipe import attack_power_recipe, damage_addition_recipe, critical_strike_recipe, double_addition_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.du_jing.buffs import BUFFS

GAINS = {
    1917: CriticalSet(2557, BUFFS[2557].gain_attributes),
    818: double_addition_recipe([6218], [], 1.2, 204),
    4678: attack_power_recipe([25917], 1.1),
    1528: double_addition_recipe([6218], [], 1.05, 51),
    1529: damage_addition_recipe([13472], 51),
    1143: critical_strike_recipe([6218], 500),
    2420: Gain(),
    1934: Gain(),
    17316: Gain(),
    17322: Gain(),
    **EQUIPMENT_GAINS,
}
