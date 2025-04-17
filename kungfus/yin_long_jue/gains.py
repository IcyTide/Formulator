from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (2745,): Gain(),
    (1944,): Gain(),
    (2428,): Gain(),
    **{(23396, level + 1): Gain() for level in range(8)},
    **EQUIPMENT_GAINS,
}
