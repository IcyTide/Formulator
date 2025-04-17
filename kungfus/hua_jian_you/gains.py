from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (2740,): Gain(),
    (2417,): Gain(),
    (1929,): Gain(),
    **{(1856, level + 1): Gain() for level in range(8)},
    **EQUIPMENT_GAINS,
}
