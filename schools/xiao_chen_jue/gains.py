from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.xiao_chen_jue.buffs import BUFFS

GAINS = {
    (22035, 1): Gain(),
    (1921,): CriticalSet(BUFFS[1438]),
    (2431,): Gain(),
    (1939,): Gain(),
    **EQUIPMENT_GAINS,
}
