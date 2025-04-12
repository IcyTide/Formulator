from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1912,): CriticalSet(GENERAL_BUFFS[1440]),
    (2740,): Gain(),
    (2417,): Gain(),
    (1929,): Gain(),
    **{(1856, level + 1): Gain() for level in range(8)},
    **EQUIPMENT_GAINS,
}
