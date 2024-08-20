from base.gain import Gain
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet
from schools.tian_luo_gui_dao.buffs import BUFFS

GAINS = {
    (1918,): CriticalSet(BUFFS[3401]),
    (2412,): Gain(),
    (1935,): Gain(),
    **EQUIPMENT_GAINS,
}
