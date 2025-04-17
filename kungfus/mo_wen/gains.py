from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (2718,): Gain(),
    (1941,): Gain(),
    (2415,): Gain(),
    **{(15183, level + 1): Gain() for level in range(8)},
    **EQUIPMENT_GAINS,
}
