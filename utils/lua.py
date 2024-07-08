import re

DAMAGE_RESULT_PATTERN = re.compile(r"\[[0-4]\]=(\d+)")


def parse(content):
    index = 0
    result = {}
    key_flag = False
    code_flags = []
    str_flag = False
    key = ""
    string = ""
    ret = {}
    num = ""
    i = 0
    while i < len(content):
        c = content[i]

        if c == "{":
            code_flags.append(i + 1)
        elif c == "}" and code_flags:
            start = code_flags.pop()
            if not code_flags:
                ret = parse(content[start: i])
        elif code_flags:
            pass
        elif c == '"':
            str_flag = not str_flag
        elif str_flag:
            string += c
        elif c == "]":
            key_flag = False
        elif key_flag:
            key += c
        elif c == "[":
            key_flag = True
        elif c == "=":
            index = int(key) - 1
            key = ""
        elif c == "," and not str_flag:
            if ret:
                result[index] = ret
                ret = {}
            elif num:
                result[index] = int(num)
                num = ""
            else:
                result[index] = string
                string = ""
            index += 1
        else:
            num += c
        i += 1
    if ret:
        result[index] = ret
    elif num:
        result[index] = int(num)
    else:
        result[index] = string
    return result


def parse_player(lua_data):
    return parse(lua_data.strip().strip("{}"))


def parse_damage(lua_data):
    return sum(int(damage) for damage in DAMAGE_RESULT_PATTERN.findall(lua_data))
