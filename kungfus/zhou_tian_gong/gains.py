from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (2726,): CriticalSet(GENERAL_BUFFS[1438]),
    (2724,): Gain(),
    (2725,): Gain(),
    **EQUIPMENT_GAINS,
}
