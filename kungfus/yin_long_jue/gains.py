from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1927,): CriticalSet(GENERAL_BUFFS[16025]),
    (2745,): Gain(),
    (1944,): Gain(),
    (2428,): Gain(),
    **{(23396, level + 1): Gain() for level in range(8)},
    **EQUIPMENT_GAINS,
}
