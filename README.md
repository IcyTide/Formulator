# Comprehensive Damage Formulator with JCL Parser

## User Guide
### In Progress

## Architecture
### Kungfu Components
- **\_\_init__.py**: this file will import all detail a kungfu needed 
- **attribute.py**: define the kungfu attribute, like extra attribute from kungfu
- **buffs.py**: define the buffs of your kungfu
- **gains.py**: define the gains from equipment, like divine and tier set activate
- **recipes.py**: define the recipes for kungfu
- **skills.py**: define the skills, include all damage skill and dot skill
- **talents.py**: define the talents

### Generate Code Automatically
All the code under **assets** are generated by scripts under **tools**
- assets/skills.py : From tools/generate_skills.py
- assets/dots.py: From tools/generate_dots.py
- assets/buffs.py : From tools/generate_buffs.py
- assets/equipments.py : From tools/generate_equipments.py
- assets/enchants.py : From tools/generate_enchants.py
- assets/stones.py : From tools/generate_enchants.py


Feel free to contribute to this exciting project! Your collaboration will make our tool more comprehensive and valuable to all users.