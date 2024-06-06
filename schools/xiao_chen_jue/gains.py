from base.recipe import DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from base.gain import Gain
from schools.xiao_chen_jue.buffs import BUFFS

GAINS = {
    (22035, 1): Gain(),
    1921: CriticalSet(1438, BUFFS[1438]),
    1548: DamageAdditionRecipe(102, 5638, 5638),
    1540: DamageAdditionRecipe(51, 5258, 5258),
    1541: DamageAdditionRecipe(51, 5638, 5638),
    1980: CriticalStrikeRecipe(500, 5367, 5367),
    1981: CriticalStrikeRecipe(500, 5368, 5368),
    1982: CriticalStrikeRecipe(500, 5369, 5369),
    1983: CriticalStrikeRecipe(500, 5370, 5370),
    2431: Gain(),
    1939: Gain(),
    17441: Gain(),
    17444: Gain(),
    17442: Gain(),
    **EQUIPMENT_GAINS,
}
