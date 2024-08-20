from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.ao_xue_zhan_yi.buffs import BUFFS

GAINS = {
    (1913,): CriticalSet(BUFFS[1428]),
    (2424,): Gain(),
    (1933,): Gain(),
    **EQUIPMENT_GAINS,
}
