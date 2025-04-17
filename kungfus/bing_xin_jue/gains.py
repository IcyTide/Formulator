from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (2719,): Gain(),
    (1930,): Gain(),
    (2416,): Gain(),
    **{(1858, level + 1): Gain() for level in range(8)},
    **EQUIPMENT_GAINS,
}
