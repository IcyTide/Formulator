from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (2717,): Gain(),
    (1934,): Gain(),
    (2420,): Gain(),
    **{(3065, level + 1): Gain() for level in range(8)},
    **EQUIPMENT_GAINS,
}
