from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1927,): CriticalSet(GENERAL_BUFFS[16025]),
    (2428,): Gain(),
    (1944,): Gain(),
    **EQUIPMENT_GAINS,
}
