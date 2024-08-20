from base.gain import Gain

from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.tai_xuan_jing.buffs import BUFFS

GAINS = {
    (1956,): CriticalSet(BUFFS[18555]),
    (2413,): Gain(),
    (1962,): Gain(),
    **EQUIPMENT_GAINS,
}
