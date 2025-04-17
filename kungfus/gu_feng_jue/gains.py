from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (2757,): Gain(),
    (2392,): Gain(),
    (2391,): Gain(),
    **{(33238, level + 1): Gain() for level in range(20)},
    **EQUIPMENT_GAINS,
}
