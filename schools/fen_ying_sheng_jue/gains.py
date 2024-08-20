from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.fen_ying_sheng_jue.buffs import BUFFS

GAINS = {
    (1922,): CriticalSet(BUFFS[4671]),
    (2421,): Gain(),
    (1938,): Gain(),
    **EQUIPMENT_GAINS,
}
