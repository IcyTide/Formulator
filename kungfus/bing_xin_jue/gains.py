from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1916,): CriticalSet(GENERAL_BUFFS[1437]),
    (2719,): Gain(),
    (1930,): Gain(),
    (2416,): Gain(),
    **EQUIPMENT_GAINS,
}
