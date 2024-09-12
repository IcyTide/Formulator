from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1926,): CriticalSet(GENERAL_BUFFS[14353]),
    (2423,): Gain(),
    (1943,): Gain(),
    **EQUIPMENT_GAINS,
}