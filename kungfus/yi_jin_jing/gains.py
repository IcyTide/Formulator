from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1911,): CriticalSet(GENERAL_BUFFS[1436]),
    (2758,): Gain(),
    (1928,): Gain(),
    (2410,): Gain(),
    **{(1854, level + 1): Gain() for level in range(8)},
    **EQUIPMENT_GAINS,
}
