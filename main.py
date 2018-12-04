import ast, json
from ml_feature import Feature


def load_log():
    str = ""
    file = open("log_file.txt", "r")
    file.readline()
    logs = file.readlines()
    for line in logs:
        str += line + ","
    # str += file.readline() + ","
    # str += file.readline() + ","
    file.close()

    return str.replace('\n', '').replace('\r', '')


def make_new_log(log):
    file = open("new_log.txt", "w")
    file.write(log)
    file.close()


def str_list_indentation(str_list):
    indent = 0
    prefix = ['[', ']', '{', '}', ',']
    res = ""
    str_list = str(str_list).replace("\'", "\"").replace("\"{", "{").replace("}\"", "}").replace(" ", "")
    for char in str_list:
        if char in prefix:
            if char == ']' or char == '}':
                indent -= 1
                res += "\n" + ("\t" * indent) + char
            else:
                if char == '[' or char == '{':
                    indent += 1
                res += char + "\n" + ("\t" * indent)
        else:
            res += char

    return res


if __name__ == "__main__":

    res = []
    log = load_log()
    dicts = ast.literal_eval(log)
    feature = Feature()
    for dict in dicts:
        feature.update_feature(dict)
        res.append(str(feature.__dict__))
    new = str_list_indentation(res)
    make_new_log(new)


