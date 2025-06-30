from tools import generate_equipments, generate_enchants
from tools import generate_attributes, generate_skills, generate_dots, generate_buffs, generate_recipes
from tools_extra import generate_mobile_skills

if __name__ == '__main__':
    # generate_attributes.generate()
    generate_buffs.generate()
    generate_dots.generate()
    generate_skills.generate()
    generate_recipes.generate()

    generate_equipments.generate()
    generate_enchants.generate()

    generate_mobile_skills.generate()
