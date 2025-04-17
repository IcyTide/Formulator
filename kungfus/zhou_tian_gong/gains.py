from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (2724,): Gain(),
    (2725,): Gain(),
    (2723,): Gain(),
    **{(39078, level + 1): Gain() for level in range(6)},
    **EQUIPMENT_GAINS,
}
