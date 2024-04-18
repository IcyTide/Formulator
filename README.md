# Comprehensive Damage Formulator with JCL Parser

## User Guide
### In Progress

## Contributing to This Project
### Add Your School
To add your school to the application, follow the steps below:
Under the schools directory, create a new python directory name it after your school (Please use snake_case for the name).
and add the following files to your directory:

- **\_\_init__.py**: this file will import all detail a school needed 
- **attribute.py**: define your school attribute, like extra attribute from school
- **buffs.py**: define the buffs of your school
- **gains.py**: define the gains from your school equipment, like divine and tier set activate
- **recipes.py**: define the recipes for skill of your school
- **skills.py**: define the skills of your school, include all damage skill and dot trigger skill
- **talents.py**: define the talents of your school

### Integrate Your School into UI
Once the school framework is ready, make your school data available on our QT-UI:

Open the **parser.py** under **utils** dir, and add your school into **SUPPORT_SCHOOL** dictionary like below:

- key: the school id you can find in LUA or ask me
- value: a School instance set by the details import from **schools/<YOUR_SCHOOL>**

Feel free to contribute to this exciting project! Your collaboration will make our tool more comprehensive and valuable to all users.