from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (2726,): Gain(),
    **EQUIPMENT_GAINS,
}
