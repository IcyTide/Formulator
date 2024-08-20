from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.tai_xu_jian_yi.buffs import BUFFS

GAINS = {
    (1915,): CriticalSet(BUFFS[1438]),
    (2419,): Gain(),
    (1932,): Gain(),
    **EQUIPMENT_GAINS,
}
