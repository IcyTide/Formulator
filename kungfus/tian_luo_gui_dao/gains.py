from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (2736,): Gain(),
    (1935,): Gain(),
    (2412,): Gain(),
    **{(3477, level + 1): Gain() for level in range(20)},
    **EQUIPMENT_GAINS,
}
