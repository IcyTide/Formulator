from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1925,): CriticalSet(GENERAL_BUFFS[11378]),
    (2430,): Gain(),
    (1942,): Gain(),
    **EQUIPMENT_GAINS,
}
