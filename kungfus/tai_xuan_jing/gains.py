from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (2756,): Gain(),
    (1962,): Gain(),
    (2413,): Gain(),
    **{(25831, level + 1): Gain() for level in range(20)},
    **EQUIPMENT_GAINS,
}
