from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (2726,): CriticalSet(GENERAL_BUFFS[29597]),
    (2724,): Gain(),
    (2725,): Gain(),
    (2723,): Gain(),
    **{(39078, level + 1): Gain() for level in range(6)},
    **EQUIPMENT_GAINS,
}
