from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.gu_feng_jue.buffs import BUFFS

GAINS = {
    (1925,): CriticalSet(BUFFS[11378]),
    (2391,): Gain(),
    (2392,): Gain(),
    **EQUIPMENT_GAINS,
}
