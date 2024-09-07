from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1911,): CriticalSet(GENERAL_BUFFS[1436]),
    (2410,): Gain(),
    (1928,): Gain(),
    **EQUIPMENT_GAINS,
}
