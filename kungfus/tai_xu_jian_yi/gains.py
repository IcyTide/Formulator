from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1915,): CriticalSet(GENERAL_BUFFS[1438]),
    (2753,): Gain(),
    (1932,): Gain(),
    (2419,): Gain(),
    **EQUIPMENT_GAINS,
}
