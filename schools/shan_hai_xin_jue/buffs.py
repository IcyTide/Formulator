from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS = {
    16025: {
        "buff_name": "雷引",
        "gain_attributes": {
            "physical_critical_strike_gain": 400,
            "physical_critical_power_gain": 41
        }
    },
    26857: {
        "buff_name": "承契",
        "gain_attributes": {
            "all_damage_addition": 62
        }
    }
}

for buff_id, detail in BUFFS.items():
    BUFFS[buff_id] = Buff(buff_id, detail.pop("buff_name"))
    for attr, value in detail.items():
        setattr(BUFFS[buff_id], attr, value)

for buff_id, buff in GENERAL_BUFFS.items():
    BUFFS[buff_id] = buff
