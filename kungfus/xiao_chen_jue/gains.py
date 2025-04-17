from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (2738,): Gain(),
    (1939,): Gain(),
    (2431,): Gain(),
    **{(6950, level + 1): Gain() for level in range(20)},
    **EQUIPMENT_GAINS,
}
