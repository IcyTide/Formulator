from base.recipe import damage_addition_recipe, critical_strike_recipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.xiao_chen_jue.buffs import BUFFS

GAINS = {
    (22035, 1): Gain(),
    1921: CriticalSet(1438, BUFFS[1438].gain_attributes),
    1548: damage_addition_recipe([6369, 6370, 6371, 6372, 6373, 6374], 102),
    1541: damage_addition_recipe([6369, 6370, 6371, 6372, 6373, 6374], 51),
    1980: critical_strike_recipe([6358, 6359, 13526], 500),
    1981: critical_strike_recipe([13527], 500),
    1982: critical_strike_recipe([6362, 6363, 13528], 500),
    1983: critical_strike_recipe([13529], 500),
    2431: Gain(),
    1939: Gain(),
    17441: Gain(),
    17444: Gain(),
    17442: Gain(),
    **EQUIPMENT_GAINS,
}
