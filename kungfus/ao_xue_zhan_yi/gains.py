from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (2741,): Gain(),
    (1933,): Gain(),
    (2424,): Gain(),
    **{(1850, level + 1): Gain() for level in range(8)},
    **EQUIPMENT_GAINS,
}
