from ast import literal_eval
import re

DAMAGE_RESULT_PATTERN = re.compile(r"\[[0-4]\]=(\d+)")


def parse_player(lua_data):
    try:
        python_data = lua_data.strip().replace("{", "[").replace("}", "]")
        return literal_eval(python_data)
    except:
        return None


def parse_damage(lua_data):
    return sum(int(damage) for damage in DAMAGE_RESULT_PATTERN.findall(lua_data))
