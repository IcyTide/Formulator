from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (2125,): CriticalSet(GENERAL_BUFFS[21758]),
    (2414,): Gain(),
    (2138,): Gain(),
    **EQUIPMENT_GAINS,
}
