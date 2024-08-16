from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.shan_hai_xin_jue.buffs import BUFFS

GAINS = {
    (2568,): CriticalSet(BUFFS[16025]),
    (2572,): Gain(),
    (2571,): Gain(),
    **EQUIPMENT_GAINS,
}
