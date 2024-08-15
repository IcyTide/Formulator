from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.bei_ao_jue.buffs import BUFFS

GAINS = {
    (1925,): CriticalSet(BUFFS[11378]),
    (2430,): Gain(),
    (1942,): Gain(),
    **EQUIPMENT_GAINS,
}
