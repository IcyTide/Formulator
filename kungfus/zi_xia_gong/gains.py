from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1914,): CriticalSet(GENERAL_BUFFS[1439]),
    (2739,): Gain(),
    (1931,): Gain(),
    (2418,): Gain(),
    **{(1853, level + 1): Gain() for level in range(20)},
    **EQUIPMENT_GAINS,
}
