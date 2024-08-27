from functools import cache

from base.constant import BINARY_SCALE, BASE_CRITICAL_POWER


@cache
def defense_result(shield, shield_ignore, shield_constant):
    shield = int(shield * (1 - shield_ignore / BINARY_SCALE))
    shield = max(shield, 0)
    return shield / (shield + shield_constant)


@cache
def base_result(damage_base, damage_rand, damage_gain):
    damage = damage_base * (1 + damage_gain / BINARY_SCALE) + damage_rand / 2
    return damage


@cache
def attack_power_result(attack_power_cof, attack_power):
    return attack_power * attack_power_cof


@cache
def weapon_damage_result(weapon_damage_cof, weapon_damage):
    return weapon_damage * weapon_damage_cof


@cache
def surplus_result(surplus_cof, surplus):
    return surplus * surplus_cof


@cache
def init_result(
        damage_base=0, damage_rand=0, damage_gain=0, attack_power_cof=0, attack_power=0,
        weapon_damage_cof=0, weapon_damage=0, surplus_cof=0, surplus=0, multi_stack=1
):
    damage = int(base_result(damage_base, damage_rand, damage_gain))
    damage += int(attack_power_result(attack_power_cof, attack_power))
    damage += int(weapon_damage_result(weapon_damage_cof, weapon_damage))
    damage += int(surplus_result(surplus_cof, surplus))
    return int(damage) * multi_stack


@cache
def damage_addition_result(damage, damage_addition, move_state_damage_addition):
    damage = int(damage * (1 + damage_addition / BINARY_SCALE))
    damage = int(damage * (1 + move_state_damage_addition / BINARY_SCALE))
    return damage


@cache
def overcome_result(damage, overcome, shield_ignore, shield, shield_constant):
    overcome = int(overcome * BINARY_SCALE + BINARY_SCALE)
    defense = defense_result(shield, shield_ignore, shield_constant)
    defense = int(defense * BINARY_SCALE)
    rate = (overcome - int(overcome * defense / BINARY_SCALE)) / BINARY_SCALE
    return int(damage * rate)


@cache
def critical_result(damage, critical_power):
    rate = int((critical_power - BASE_CRITICAL_POWER) * BINARY_SCALE) / BINARY_SCALE
    return int(damage * BASE_CRITICAL_POWER) + int(damage * rate)


@cache
def level_reduction_result(damage, level_reduction):
    return int(damage * (1 - level_reduction))


@cache
def strain_result(damage, strain):
    rate = int(strain * BINARY_SCALE) / BINARY_SCALE
    return int(damage * (1 + rate))


@cache
def pve_addition_result(damage, pve_addition):
    return int(damage * (1 + pve_addition / BINARY_SCALE))


@cache
def damage_cof_result(damage, damage_cof):
    return int(damage * (1 + damage_cof / BINARY_SCALE))


@cache
def vulnerable_result(damage, vulnerable):
    return int(damage * (1 + vulnerable / BINARY_SCALE))
