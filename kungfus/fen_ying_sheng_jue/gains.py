from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1922,): CriticalSet(GENERAL_BUFFS[4671]),
    (2421,): Gain(),
    (1938,): Gain(),
    **EQUIPMENT_GAINS,
}
