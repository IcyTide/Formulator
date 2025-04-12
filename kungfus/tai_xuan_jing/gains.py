from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1956,): CriticalSet(GENERAL_BUFFS[18555]),
    (2756,): Gain(),
    (1962,): Gain(),
    (2413,): Gain(),
    **{(25831, level + 1): Gain() for level in range(20)},
    **EQUIPMENT_GAINS,
}
