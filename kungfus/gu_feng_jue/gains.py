from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1925,): CriticalSet(GENERAL_BUFFS[11378]),
    (2757,): Gain(),
    (2392,): Gain(),
    (2391,): Gain(),
    **EQUIPMENT_GAINS,
}
