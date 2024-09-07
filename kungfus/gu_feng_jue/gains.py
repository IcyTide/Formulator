from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1925,): CriticalSet(GENERAL_BUFFS[11378]),
    (2391,): Gain(),
    (2392,): Gain(),
    **EQUIPMENT_GAINS,
}
