from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1918,): CriticalSet(GENERAL_BUFFS[3401]),
    (2412,): Gain(),
    (1935,): Gain(),
    **EQUIPMENT_GAINS,
}
