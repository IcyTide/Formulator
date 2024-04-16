from base.buff import Buff

GENERAL_BUFFS = {
    15455: {
        "buff_name": "输出伤害波动",
        "gain_attributes": {
            "all_damage_addition": [10, 51]
        }
    },
    # 4761: {
    #     "buff_name": "水特效",
    #     "gain_attributes": {
    #         "physical_attack_power_base": 0,
    #         "magical_attack_power_base": 0,
    #     }
    # },
    # 6360: {
    #     "buff_name": "风特效",
    #     "gain_attributes": {
    #         "physical_overcome_base": 0,
    #         "magical_overcome_base": 0
    #     }
    # }
}

for buff_id, detail in GENERAL_BUFFS.items():
    GENERAL_BUFFS[buff_id] = Buff(buff_id, detail.pop("buff_name"))
    for attr, value in detail.items():
        setattr(GENERAL_BUFFS[buff_id], attr, value)
