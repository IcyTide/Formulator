from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (2568,): CriticalSet(GENERAL_BUFFS[16025]),
    (2746,): Gain(),
    (2571,): Gain(),
    (2572,): Gain(),
    **EQUIPMENT_GAINS,
}
