from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.hua_jian_you.buffs import BUFFS

GAINS = {
    (1912,): CriticalSet(BUFFS[1440]),
    (2417,): Gain(),
    (1929,): Gain(),
    **EQUIPMENT_GAINS,
}
