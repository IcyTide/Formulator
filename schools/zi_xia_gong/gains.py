from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.zi_xia_gong.buffs import BUFFS

GAINS = {
    (1914,): CriticalSet(BUFFS[1439]),
    (2418,): Gain(),
    (1931,): Gain(),
    **EQUIPMENT_GAINS,
}
