from tools import generate_skills, generate_dots, generate_buffs, generate_recipes
from tools import generate_equipments, generate_enchants

if __name__ == '__main__':
    generate_buffs.generate()
    generate_dots.generate()
    generate_skills.generate()
    generate_recipes.generate()

    generate_equipments.generate()
    generate_enchants.generate()
