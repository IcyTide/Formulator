from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1919,): CriticalSet(GENERAL_BUFFS[3401]),
    (2737,): Gain(),
    (1936,): Gain(),
    (2411,): Gain(),
    **EQUIPMENT_GAINS,
}
