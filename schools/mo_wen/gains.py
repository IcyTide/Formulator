from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.mo_wen.buffs import BUFFS

GAINS = {
    (1924,): CriticalSet(BUFFS[9586]),
    (2415,): Gain(),
    (1941,): Gain(),
    **EQUIPMENT_GAINS,
}
