from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1913,): CriticalSet(GENERAL_BUFFS[1428]),
    (2741,): Gain(),
    (1933,): Gain(),
    (2424,): Gain(),
    **{(1851, level + 1): Gain() for level in range(8)},
    **EQUIPMENT_GAINS,
}
