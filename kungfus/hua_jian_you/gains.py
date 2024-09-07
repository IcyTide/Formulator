from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1912,): CriticalSet(GENERAL_BUFFS[1440]),
    (2417,): Gain(),
    (1929,): Gain(),
    **EQUIPMENT_GAINS,
}
