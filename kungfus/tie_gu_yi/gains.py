from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (1222,): Gain(),
    **EQUIPMENT_GAINS,
}
