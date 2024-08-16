from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.ling_hai_jue.buffs import BUFFS

GAINS = {
    (1926,): CriticalSet(BUFFS[14353]),
    (2423,): Gain(),
    (1943,): Gain(),
    **EQUIPMENT_GAINS,
}
