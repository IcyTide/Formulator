from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.yin_long_jue.buffs import BUFFS

GAINS = {
    (36726, 1): Gain(),
    (1927,): CriticalSet(BUFFS[16025]),
    (2428,): Gain(),
    (1944,): Gain(),
    **EQUIPMENT_GAINS,
}
