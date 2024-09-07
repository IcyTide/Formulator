from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1923,): CriticalSet(GENERAL_BUFFS[1428]),
    (2408,): Gain(),
    (1940,): Gain(),
    **EQUIPMENT_GAINS,
}
