from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.yi_jin_jing.buffs import BUFFS

GAINS = {
    (1911,): CriticalSet(BUFFS[1436]),
    (2410,): Gain(),
    (1928,): Gain(),
    **EQUIPMENT_GAINS,
}
