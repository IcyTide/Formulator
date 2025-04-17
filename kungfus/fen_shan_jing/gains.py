from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS

GAINS = {
    (2754,): Gain(),
    (1940,): Gain(),
    (2408,): Gain(),
    **EQUIPMENT_GAINS,
}
