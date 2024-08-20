from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.jing_yu_jue.buffs import BUFFS

GAINS = {
    (1919,): CriticalSet(BUFFS[3401]),
    (2411,): Gain(),
    (1936,): Gain(),
    **EQUIPMENT_GAINS,
}
