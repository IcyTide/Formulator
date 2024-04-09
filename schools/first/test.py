from base.calculator import analyze_details
from qt.scripts.top import Parser
from schools.first.attribute import BeiAoJue


if __name__ == '__main__':
    attribute = BeiAoJue()
    attribute.strength_base += 6665
    attribute.weapon_damage_base += 3291
    attribute.weapon_damage_rand += 2194
    attribute.surplus += 29401
    attribute.strain_base += 15598
    attribute.physical_attack_power_base += 28964
    attribute.physical_critical_strike_base += 30507
    attribute.physical_overcome_base += 24303
    attribute.physical_critical_power_base += 7905

    parser = Parser()
    parser("logs.jcl")
    analyze_details(parser, attribute)
    print(parser.records)
