from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.fen_shan_jing.buffs import BUFFS

GAINS = {
    (1923,): CriticalSet(BUFFS[1428]),
    (2408,): Gain(),
    (1940,): Gain(),
    17447: Gain(),
    17448: Gain(),
    **EQUIPMENT_GAINS,
}
