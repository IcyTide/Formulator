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
                if num == "true":
                    result[index] = True
                elif num == "false":
                    result[index] = False
                else:
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
        if num == "true":
            result[index] = True
        elif num == "false":
            result[index] = False
        else:
            result[index] = int(num)
    elif string:
        result[index] = string
    return result


def parse_lua(lua_data):
    return parse(lua_data.strip()[1:-1])


if __name__ == '__main__':
    r = parse_lua('{117,1073742562,0,1,3404,1,false,3,{[14]=0,[13]=250532,[4]=250532}}')
    print(r)