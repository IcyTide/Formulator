from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1921,): CriticalSet(GENERAL_BUFFS[1438]),
    (2738,): Gain(),
    (1939,): Gain(),
    (2431,): Gain(),
    **EQUIPMENT_GAINS,
}
