from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1924,): CriticalSet(GENERAL_BUFFS[9586]),
    (2718,): Gain(),
    (1941,): Gain(),
    (2415,): Gain(),
    **{(15183, level + 1): Gain() for level in range(8)},
    **EQUIPMENT_GAINS,
}
