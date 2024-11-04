from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1924,): CriticalSet(GENERAL_BUFFS[9586]),
    (2718,): Gain(),
    (1941,): Gain(),
    (2415,): Gain(),
    **EQUIPMENT_GAINS,
}
