from base.gain import Gain
from base.recipe import ChannelIntervalRecipe, DamageAdditionRecipe, CriticalStrikeRecipe
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.du_jing.buffs import BUFFS
from schools.du_jing.recipes import 蝎心伤害提高

GAINS = {
    (1917,): CriticalSet(2557, BUFFS[2557]),
    818: 蝎心伤害提高((1.2, 204), 2209, 2209),
    4678: ChannelIntervalRecipe(1.1, 2211, 2211),
    1528: 蝎心伤害提高((1.05, 51), 2209, 2209),
    1529: DamageAdditionRecipe(51, 2212, 2212),
    1143: CriticalStrikeRecipe(500, 2209, 2209),
    (2420,): Gain(),
    (1934,): Gain(),
    17316: Gain(),
    17322: Gain(),
    **EQUIPMENT_GAINS,
}
