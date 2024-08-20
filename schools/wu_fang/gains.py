from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.wu_fang.buffs import BUFFS

GAINS = {
    (2125,): CriticalSet(BUFFS[21758]),
    (2414,): Gain(),
    (2138,): Gain(),
    **EQUIPMENT_GAINS,
}
