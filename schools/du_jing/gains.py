from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.du_jing.buffs import BUFFS

GAINS = {
    (1917,): CriticalSet(BUFFS[2557]),
    (2420,): Gain(),
    (1934,): Gain(),
    **EQUIPMENT_GAINS,
}
