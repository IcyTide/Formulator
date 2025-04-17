from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (2761,): Gain(),
    (1942,): Gain(),
    (2430,): Gain(),
    **{(16984, level + 1): Gain() for level in range(8)},
    **EQUIPMENT_GAINS,
}
