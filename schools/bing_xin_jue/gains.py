from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.bing_xin_jue.buffs import BUFFS

GAINS = {
    (1916,): CriticalSet(BUFFS[1437]),
    (2416,): Gain(),
    (1930,): Gain(),
    **EQUIPMENT_GAINS,
}
