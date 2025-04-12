from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1923,): CriticalSet(GENERAL_BUFFS[1428]),
    (2754,): Gain(),
    (1940,): Gain(),
    (2408,): Gain(),
    **{(13410, level + 1): Gain() for level in range(20)},
    **EQUIPMENT_GAINS,
}
