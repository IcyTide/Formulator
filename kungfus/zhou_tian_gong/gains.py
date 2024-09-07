from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1956,): CriticalSet(GENERAL_BUFFS[18555]),
    **EQUIPMENT_GAINS,
}
