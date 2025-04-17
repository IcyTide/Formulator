from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (2746,): Gain(),
    (2571,): Gain(),
    (2572,): Gain(),
    **{(36578, level + 1): Gain() for level in range(6)},
    **EQUIPMENT_GAINS,
}
