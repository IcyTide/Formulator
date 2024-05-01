from utils.lua import parse
lua = """

"""
result = parse(lua)
damage_base = [row['nDamageBase'] for row in result]
print(f'"damage_base": {damage_base},')
damage_rand = [row['nDamageRand'] for row in result]
print(f'"damage_rand": {damage_rand},')
