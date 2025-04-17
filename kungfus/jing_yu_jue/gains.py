from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (2737,): Gain(),
    (1936,): Gain(),
    (2411,): Gain(),
    **{(3476, level + 1): Gain() for level in range(20)},
    **EQUIPMENT_GAINS,
}
