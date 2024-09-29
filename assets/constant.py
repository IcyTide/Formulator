import os

""" Directory """
ASSETS_DIR = "assets"
EQUIPMENTS_DIR = os.path.join(ASSETS_DIR, "equipments.json")
ENCHANTS_DIR = os.path.join(ASSETS_DIR, "enchants.json")
STONES_DIR = os.path.join(ASSETS_DIR, "stones.json")


""" Season Constant """

SPECIAL_ENCHANT_MAP = {
    3: {
        26600: [15436, 14],
        23500: [15436, 13]
    },
    2: {
        26600: [22151, 14],
        23500: [22151, 13]
    },
    6: {
        26600: [2672],
        23500: [2662]
    },
    10: {
        26600: [2673],
        23500: [2663]
    },
    9: {
        26600: [2674],
        23500: [2664]
    }
}
MIN_EQUIP_LEVEL = 16500
LAST_SEASON_DIVINE_LEVEL = 12500, 11650
ENCHANT_START_ID = 12207

BUFF_MAX_ATTRIB = 15

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
ATTR_TYPE_MAP = {
    "atVitalityBase": "vitality_base",
    "atMaxLifeAdditional": "max_life_add",
    "atMeleeWeaponDamageBase": "weapon_damage_base",
    "atMeleeWeaponDamageRand": "weapon_damage_rand",
    "atMeleeWeaponDamagePercent": "weapon_damage_gain",
    "atBasePotentialAdd": "all_major_base",

    "atAgilityBase": "agility_base",
    "atStrengthBase": "strength_base",
    "atSpiritBase": "spirit_base",
    "atSpunkBase": "spunk_base",
    "atAgilityBasePercentAdd": "agility_gain",
    "atStrengthBasePercentAdd": "strength_gain",
    "atSpiritBasePercentAdd": "spirit_gain",
    "atSpunkBasePercentAdd": "spunk_gain",

    "atPhysicsAttackPowerBase": "physical_attack_power_base",
    "atMagicAttackPowerBase": "magical_attack_power_base",
    "atSolarAndLunarAttackPowerBase": "solar_and_lunar_attack_power_base",
    "atSolarAttackPowerBase": "solar_attack_power_base",
    "atLunarAttackPowerBase": "lunar_attack_power_base",
    "atNeutralAttackPowerBase": "neutral_attack_power_base",
    "atPoisonAttackPowerBase": "poison_attack_power_base",

    "atPhysicsAttackPowerPercent": "physical_attack_power_gain",
    "atMagicAttackPowerPercent": "magical_attack_power_gain",
    "atSolarAttackPowerPercent": "solar_attack_power_gain",
    "atLunarAttackPowerPercent": "lunar_attack_power_gain",
    "atNeutralAttackPowerPercent": "neutral_attack_power_gain",
    "atPoisonAttackPowerPercent": "poison_attack_power_gain",

    "atPhysicsOvercomeBase": "physical_overcome_base",
    "atMagicOvercome": "magical_overcome_base",
    "atSolarAndLunarOvercomeBase": "solar_and_lunar_overcome_base",
    "atSolarOvercomeBase": "solar_overcome_base",
    "atLunarOvercomeBase": "lunar_overcome_base",
    "atNeutralOvercomeBase": "neutral_overcome_base",
    "atPoisonOvercomeBase": "poison_overcome_base",

    "atPhysicsOvercomePercent": "physical_overcome_gain",
    "atSolarOvercomePercent": "solar_overcome_gain",
    "atLunarOvercomePercent": "lunar_overcome_gain",
    "atNeutralOvercomePercent": "neutral_overcome_gain",
    "atPoisonOvercomePercent": "poison_overcome_gain",

    "atAllTypeCriticalStrike": "all_critical_strike_base",
    "atPhysicsCriticalStrike": "physical_critical_strike_base",
    "atMagicCriticalStrike": "magical_critical_strike_base",
    "atSolarAndLunarCriticalStrike": "solar_and_lunar_critical_strike_base",
    "atSolarCriticalStrike": "solar_critical_strike_base",
    "atLunarCriticalStrike": "lunar_critical_strike_base",
    "atNeutralCriticalStrike": "neutral_critical_strike_base",
    "atPoisonCriticalStrike": "poison_critical_strike_base",

    "atPhysicsCriticalStrikeBaseRate": "physical_critical_strike_rate",
    "atSolarCriticalStrikeBaseRate": "solar_critical_strike_rate",
    "atLunarCriticalStrikeBaseRate": "lunar_critical_strike_rate",
    "atNeutralCriticalStrikeBaseRate": "neutral_critical_strike_rate",
    "atPoisonCriticalStrikeBaseRate": "poison_critical_strike_rate",

    "atAllTypeCriticalDamagePowerBase": "all_critical_power_base",
    "atPhysicsCriticalDamagePowerBase": "physical_critical_power_base",
    "atMagicCriticalDamagePowerBase": "magical_critical_power_base",
    "atSolarAndLunarCriticalDamagePowerBase": "solar_and_lunar_critical_power_base",
    "atSolarCriticalDamagePowerBase": "solar_critical_power_base",
    "atLunarCriticalDamagePowerBase": "lunar_critical_power_base",
    "atNeutralCriticalDamagePowerBase": "neutral_critical_power_base",
    "atPoisonCriticalDamagePowerBase": "poison_critical_power_base",

    "atPhysicsCriticalDamagePowerBaseKiloNumRate": "physical_critical_power_rate",
    "atMagicCriticalDamagePowerBaseKiloNumRate": "magical_critical_power_rate",
    "atSolarCriticalDamagePowerBaseKiloNumRate": "solar_critical_power_rate",
    "atLunarCriticalDamagePowerBaseKiloNumRate": "lunar_critical_power_rate",
    "atNeutralCriticalDamagePowerBaseKiloNumRate": "neutral_critical_power_rate",
    "atPoisonCriticalDamagePowerBaseKiloNumRate": "poison_critical_power_rate",

    "atSurplusValueBase": "surplus_base",
    "atSurplusValueAddPercent": "surplus_gain",

    "atStrainBase": "strain_base",
    "atStrainPercent": "strain_gain",
    "atStrainRate": "strain_rate",
    "atPVXAllRound": "pvx_round",

    "atHasteBase": "haste_base",

    "atAllShieldIgnorePercent": "all_shield_ignore",
    "atAllDamageAddPercent": "all_damage_addition",
    "atAllPhysicsDamageAddPercent": "physical_damage_addition",
    "atAllMagicDamageAddPercent": "magical_damage_addition",
    "atDstNpcDamageCoefficient": "pve_addition_base",
}
TARGET_ATTR_TYPE_MAP = {
    "atResistCriticalStrikeRate": "resist_critical_strike_rate",

    "atPhysicsShieldBase": "physical_shield_base",
    "atPhysicsShieldPercent": "physical_shield_gain",
    "atMagicShield": "magical_shield_base",
    "atSolarMagicShieldPercent": "solar_shield_gain",
    "atLunarMagicShieldPercent": "lunar_shield_gain",
    "atNeutralMagicShieldPercent": "neutral_shield_gain",
    "atPoisonMagicShieldPercent": "poison_shield_gain",

    "atPhysicsDamageCoefficient": "physical_damage_cof",
    "atSolarDamageCoefficient": "solar_damage_cof",
    "atLunarDamageCoefficient": "lunar_damage_cof",
    "atNeutralDamageCoefficient": "neutral_damage_cof",
    "atPoisonDamageCoefficient": "poison_damage_cof",
}
ATTR_TYPE_MAP = {
    **ATTR_TYPE_MAP,
    **TARGET_ATTR_TYPE_MAP
}
ATTR_TYPE_TRANSLATE = {
    "vitality_base": "体质",
    "max_life_add": "额外气血上限",
    "weapon_damage_base": "基础武器伤害",
    "weapon_damage_rand": "浮动武器伤害",
    "all_major_base": "全属性",
    "agility_base": "身法",
    "strength_base": "力道",
    "spirit_base": "根骨",
    "spunk_base": "元气",
    "physical_attack_power_base": "外功攻击",
    "magical_attack_power_base": "内功攻击",
    "lunar_attack_power_base": "阴性攻击",
    "solar_attack_power_base": "阳性攻击",
    "neutral_attack_power_base": "混元攻击",
    "solar_and_lunar_attack_power_base": "阴阳攻击",
    "poison_attack_power_base": "毒性攻击",
    "physical_critical_strike_base": "外功会心等级",
    "magical_critical_strike_base": "内功会心等级",
    "lunar_critical_strike_base": "阴性会心等级",
    "solar_critical_strike_base": "阳性会心等级",
    "neutral_critical_strike_base": "混元会心等级",
    "solar_and_lunar_critical_strike_base": "阴阳会心等级",
    "poison_critical_strike_base": "毒性会心等级",
    "all_critical_strike_base": "全会心等级",
    "physical_critical_power_base": "外功会心效果等级",
    "magical_critical_power_base": "内功会心效果等级",
    "lunar_critical_power_base": "阴性会心效果等级",
    "solar_critical_power_base": "阳性会心效果等级",
    "neutral_critical_power_base": "混元会心效果等级",
    "solar_and_lunar_critical_power_base": "阴阳会心效果等级",
    "poison_critical_power_base": "毒性会心效果等级",
    "all_critical_power_base": "全会心效果等级",
    "physical_overcome_base": "外功破防等级",
    "magical_overcome_base": "内功破防等级",
    "lunar_overcome_base": "阴性破防等级",
    "solar_overcome_base": "阳性破防等级",
    "neutral_overcome_base": "混元破防等级",
    "solar_and_lunar_overcome_base": "阴阳破防等级",
    "poison_overcome_base": "毒性破防等级",
    "surplus_base": "破招值",
    "strain_base": "无双等级",
    "pvx_round": "全能",
    "haste_base": "加速",
}
ATTR_TYPE_TRANSLATE_REVERSE = {v: k for k, v in ATTR_TYPE_TRANSLATE.items()}
ATTR_TYPE_TRANSLATE = {
    **ATTR_TYPE_TRANSLATE,
    "base_weapon_damage": "基础武器伤害",
    "strain": "无双",
    "surplus": "破招",
    "agility": "身法",
    "strength": "力道",
    "spirit": "根骨",
    "spunk": "元气",

    "base_physical_attack_power": "外功基础攻击",
    "base_magical_attack_power": "内功基础攻击",
    "base_solar_attack_power": "阳功基础攻击",
    "base_lunar_attack_power": "阴功基础攻击",
    "base_neutral_attack_power": "混元基础攻击",
    "base_poison_attack_power": "毒性基础攻击",

    "physical_attack_power": "外功攻击",
    "magical_attack_power": "内功攻击",
    "lunar_attack_power": "阴性攻击",
    "solar_attack_power": "阳性攻击",
    "neutral_attack_power": "混元攻击",
    "poison_attack_power": "毒性攻击",

    "final_physical_critical_strike": "外功会心等级",
    "final_magical_critical_strike": "内功会心等级",
    "final_lunar_critical_strike": "阴性会心等级",
    "final_solar_critical_strike": "阳性会心等级",
    "final_neutral_critical_strike": "混元会心等级",
    "final_poison_critical_strike": "毒性会心等级",

    "physical_critical_strike": "外功会心",
    "magical_critical_strike": "内功会心",
    "lunar_critical_strike": "阴性会心",
    "solar_critical_strike": "阳性会心",
    "neutral_critical_strike": "混元会心",
    "poison_critical_strike": "毒性会心",

    "physical_critical_power": "外功会心效果",
    "magical_critical_power": "内功会心效果",
    "lunar_critical_power": "阴性会心效果",
    "solar_critical_power": "阳性会心效果",
    "neutral_critical_power": "混元会心效果",
    "poison_critical_power": "毒性会心效果",

    "base_physical_overcome": "外功基础破防",
    "base_magical_overcome": "内功基础破防",
    "base_lunar_overcome": "阴性基础破防",
    "base_solar_overcome": "阳性基础破防",
    "base_neutral_overcome": "混元基础破防",
    "base_poison_overcome": "毒性基础破防",

    "final_physical_overcome": "外功最终破防",
    "final_magical_overcome": "内功最终破防",
    "final_lunar_overcome": "阴性最终破防",
    "final_solar_overcome": "阳性最终破防",
    "final_neutral_overcome": "混元最终破防",
    "final_poison_overcome": "毒性最终破防",

    "physical_overcome": "外功破防",
    "magical_overcome": "内功破防",
    "lunar_overcome": "阴性破防",
    "solar_overcome": "阳性破防",
    "neutral_overcome": "混元破防",
    "poison_overcome": "毒性破防",
}
""" Equip """

MAX_BASE_ATTR = 6
MAX_ENCHANT_ATTR = 4

MAX_MAGIC_ATTR = 12
MAX_STRENGTH_LEVEL = 8

MAX_SET_COUNT = 4
MAX_SET_ATTR = 4

MAX_EMBED_ATTR = 3
MAX_EMBED_LEVEL = 8

MAX_STONE_ATTR = 3
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
