from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1911,): CriticalSet(GENERAL_BUFFS[1436]),
    (2758,): Gain(),
    (1928,): Gain(),
    (2410,): Gain(),
    **EQUIPMENT_GAINS,
}
