from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1917,): CriticalSet(GENERAL_BUFFS[2557]),
    (2420,): Gain(),
    (1934,): Gain(),
    **EQUIPMENT_GAINS,
}
