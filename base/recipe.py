

def damage_addition_recipe(skill_ids, value, name="伤害增加"):
    return {
        "buff_name": name,
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": value
            } for skill_id in skill_ids
        }
    }


def critical_strike_recipe(skill_ids, value, name="会心增加"):
    return {
        "buff_name": name,
        "gain_skills": {
            skill_id: {
                "skill_critical_strike": value
            } for skill_id in skill_ids
        }
    }
