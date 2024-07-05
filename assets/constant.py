import os

""" Directory """
ASSETS_DIR = "assets"
EQUIPMENTS_DIR = os.path.join(ASSETS_DIR, "equipments")
ENCHANTS_DIR = os.path.join(ASSETS_DIR, "enchants")
STONES_DIR = os.path.join(ASSETS_DIR, "stones.json")

""" Equipments """
POSITION_MAP = {
    '帽子': 'hat',
    '上衣': 'jacket',
    '腰带': 'belt',
    '护腕': 'wrist',
    '下装': 'bottoms',
    '鞋子': 'shoes',
    '项链': 'necklace',
    '腰坠': 'pendant',
    '戒指1': 'ring',
    '戒指2': 'ring',
    '远程武器': 'tertiary_weapon',
    '近战武器': 'primary_weapon',
    '额外武器': 'secondary_weapon'
}
STONES_POSITIONS = ["primary_weapon", 'secondary_weapon']
EMBED_POSITIONS = {
    "hat": 2,
    "jacket": 2,
    "belt": 2,
    "wrist": 2,
    "bottoms": 2,
    "shoes": 2,
    "necklace": 1,
    "pendant": 1,
    "ring": 0,
    "tertiary_weapon": 1,
    "primary_weapon": 3,
    "secondary_weapon": 3
}
SPECIAL_ENCHANT_POSITIONS = ["hat", "jacket", "belt", "wrist", "shoes"]
""" Attrs """
ATTR_TYPE_MAP = dict(
    atMeleeWeaponDamageBase="weapon_damage_base",
    atMeleeWeaponDamageRand="weapon_damage_rand",
    atMeleeWeaponDamagePercent="weapon_damage_gain",
    atBasePotentialAdd="all_major_base",

    atAgilityBase="agility_base",
    atStrengthBase="strength_base",
    atSpiritBase="spirit_base",
    atSpunkBase="spunk_base",
    atAgilityBasePercentAdd="agility_gain",
    atStrengthBasePercentAdd="strength_gain",
    atSpiritBasePercentAdd="spirit_gain",
    atSpunkBasePercentAdd="spunk_gain",

    atPhysicsAttackPowerBase="physical_attack_power_base",
    atMagicAttackPowerBase="magical_attack_power_base",
    atSolarAttackPowerBase="magical_attack_power_base",
    atLunarAttackPowerBase="magical_attack_power_base",
    atNeutralAttackPowerBase="magical_attack_power_base",
    atSolarAndLunarAttackPowerBase="magical_attack_power_base",
    atPoisonAttackPowerBase="magical_attack_power_base",

    atPhysicsAttackPowerPercent="physical_attack_power_gain",
    atMagicAttackPowerPercent="magical_attack_power_gain",
    atSolarAttackPowerPercent="magical_attack_power_gain",
    atLunarAttackPowerPercent="magical_attack_power_gain",
    atNeutralAttackPowerPercent="magical_attack_power_gain",
    atSolarAndLunarAttackPowerPercent="magical_attack_power_gain",
    atPoisonAttackPowerPercent="magical_attack_power_gain",

    atPhysicsOvercomeBase="physical_overcome_base",
    atMagicOvercome="magical_overcome_base",
    atSolarOvercomeBase="magical_overcome_base",
    atLunarOvercomeBase="magical_overcome_base",
    atNeutralOvercomeBase="magical_overcome_base",
    atSolarAndLunarOvercomeBase="magical_overcome_base",
    atPoisonOvercomeBase="magical_overcome_base",

    atPhysicsOvercomePercent="physical_overcome_gain",
    atMagicOvercomePercent="magical_overcome_gain",
    atSolarOvercomePercent="magical_overcome_gain",
    atLunarOvercomePercent="magical_overcome_gain",
    atNeutralOvercomePercent="magical_overcome_gain",
    atSolarAndLunarOvercomePercent="magical_overcome_gain",
    atPoisonOvercomePercent="magical_overcome_gain",

    atAllTypeCriticalStrike="all_critical_strike_base",
    atPhysicsCriticalStrike="physical_critical_strike_base",
    atMagicCriticalStrike="magical_critical_strike_base",
    atSolarCriticalStrike="magical_critical_strike_base",
    atLunarCriticalStrike="magical_critical_strike_base",
    atNeutralCriticalStrike="magical_critical_strike_base",
    atSolarAndLunarCriticalStrike="magical_critical_strike_base",
    atPoisonCriticalStrike="magical_critical_strike_base",

    atAllTypeCriticalStrikeBaseRate="all_critical_strike_rate",
    atPhysicsCriticalStrikeBaseRate="physical_critical_strike_rate",
    atSolarCriticalStrikeBaseRate="magical_critical_strike_rate",
    atLunarCriticalStrikeBaseRate="magical_critical_strike_rate",
    atNeutralCriticalStrikeBaseRate="magical_critical_strike_rate",
    atSolarAndLunarCriticalStrikeBaseRate="magical_critical_strike_rate",
    atPoisonCriticalStrikeBaseRate="magical_critical_strike_rate",

    atAllTypeCriticalDamagePowerBase="all_critical_power_base",
    atPhysicsCriticalDamagePowerBase="physical_critical_power_base",
    atMagicCriticalDamagePowerBase="magical_critical_power_base",
    atSolarCriticalDamagePowerBase="magical_critical_power_base",
    atLunarCriticalDamagePowerBase="magical_critical_power_base",
    atNeutralCriticalDamagePowerBase="magical_critical_power_base",
    atSolarAndLunarCriticalDamagePowerBase="magical_critical_power_base",
    atPoisonCriticalDamagePowerBase="magical_critical_power_base",

    atPhysicsCriticalDamagePowerBaseKiloNumRate="physical_critical_power_rate",
    atMagicCriticalDamagePowerBaseKiloNumRate="magical_critical_power_rate",
    atSolarCriticalDamagePowerBaseKiloNumRate="magical_critical_power_rate",
    atLunarCriticalDamagePowerBaseKiloNumRate="magical_critical_power_rate",
    atNeutralCriticalDamagePowerBaseKiloNumRate="magical_critical_power_rate",
    atSolarAndLunarCriticalDamagePowerBaseKiloNumRate="magical_critical_power_rate",
    atPoisonCriticalDamagePowerBaseKiloNumRate="magical_critical_power_rate",

    atSurplusValueBase="surplus_base",
    atSurplusValueAddPercent="surplus_gain",

    atStrainBase="strain_base",
    atStrainPercent="strain_gain",
    atStrainRate="strain_rate",
    atHasteBase="haste_base",

    atAllShieldIgnorePercent="all_shield_ignore",
    atAllDamageAddPercent="all_damage_addition",
    atAllPhysicsDamageAddPercent="physical_damage_addition",
    atAllMagicDamageAddPercent="magical_damage_addition",
    atDstNpcDamageCoefficient="pve_addition",

    atPhysicsShieldBase="physical_shield_base",
    atPhysicsShieldPercent="physical_shield_gain",
    atMagicShield="magical_shield_base",
    atSolarMagicShieldPercent="magical_shield_gain",
    atLunarMagicShieldPercent="magical_shield_gain",
    atNeutralMagicShieldPercent="magical_shield_gain",
    atPoisonMagicShieldPercent="magical_shield_gain",

    atPhysicsDamageCoefficient="physical_damage_cof",
    atSolarDamageCoefficient="magical_damage_cof",
    atLunarDamageCoefficient="magical_damage_cof",
    atNeutralDamageCoefficient="magical_damage_cof",
    atPoisonDamageCoefficient="magical_damage_cof",
)

ATTR_TYPE_TRANSLATE = {
    "weapon_damage_base": "基础武器伤害",
    "weapon_damage_rand": "浮动武器伤害",
    "all_major_base": "全属性",
    "agility_base": "身法",
    "strength_base": "力道",
    "spirit_base": "根骨",
    "spunk_base": "元气",
    "physical_attack_power_base": "外功攻击",
    "magical_attack_power_base": "内功攻击",
    "physical_critical_strike_base": "外功会心",
    "magical_critical_strike_base": "内功会心",
    "all_critical_strike_base": "全会心",
    "physical_critical_power_base": "外功会效",
    "magical_critical_power_base": "内功会效",
    "all_critical_power_base": "全会效",
    "physical_overcome_base": "外功破防",
    "magical_overcome_base": "内功破防",
    "surplus_base": "破招",
    "strain_base": "无双",
    "haste_base": "加速",
}
ATTR_TYPE_TRANSLATE_REVERSE = {v: k for k, v in ATTR_TYPE_TRANSLATE.items()}

""" Equip """

MAX_EMBED_ATTR = 3
MAX_BASE_ATTR = 6
MAX_MAGIC_ATTR = 12
MAX_ENCHANT_ATTR = 4
MAX_STONE_ATTR = 3

MAX_EMBED_LEVEL = 8
MAX_STRENGTH_LEVEL = 8
MAX_STONE_LEVEL = 6


def EMBED_COF(level):
    if level > 6:
        return (level * 0.65 - 3.2) * 1.3
    else:
        return level * 0.195


def STRENGTH_COF(level):
    return level * (0.7 + 0.3 * level) / 200


""" Talent """
MAX_TALENTS = 12
MOBILE_MAX_TALENTS = 4

""" Recipes """
MAX_RECIPE_SKILLS = 12
MAX_RECIPES = 4

""" Consumables """
