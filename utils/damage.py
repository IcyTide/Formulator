from functools import cache

from base.constant import BINARY_SCALE, BASE_CRITICAL_POWER


@cache
def defense_result(shield_base, shield_gain, shield_ignore, shield_constant):
    shield = shield_base
    shield += int(shield * shield_gain / BINARY_SCALE)
    shield -= int(shield * shield_ignore / BINARY_SCALE)
    shield = max(shield, 0)
    return int(shield * BINARY_SCALE / (shield + shield_constant))


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
        damage_base, damage_rand, damage_gain, attack_power_cof, attack_power,
        weapon_damage_cof, weapon_damage, surplus_cof, surplus, global_damage_factor
):
    damage = base_result(damage_base, damage_rand, damage_gain)
    damage += attack_power_result(attack_power_cof, attack_power)
    damage += weapon_damage_result(weapon_damage_cof, weapon_damage)
    damage += surplus_result(surplus_cof, surplus)
    return int(damage * global_damage_factor)


@cache
def damage_addition_result(damage, damage_addition, damage_addition_extra):
    damage = int(damage * (1 + damage_addition / BINARY_SCALE))
    damage = int(damage * (1 + damage_addition_extra / BINARY_SCALE))
    return damage


@cache
def overcome_result(damage, overcome, shield_base, shield_gain, shield_ignore, shield_constant):
    overcome = int(overcome * BINARY_SCALE + BINARY_SCALE)
    defense = defense_result(shield_base, shield_gain, shield_ignore, shield_constant)
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
