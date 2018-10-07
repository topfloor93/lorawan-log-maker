import ast
from ml_feature import Feature


def load_log():
    str = ""
    file = open("log_file.txt", "r")
    file.readline()
    logs = file.readlines()
    for line in logs:
        str += line + ","
    #str += file.readline() + ","
    #str += file.readline() + ","
    file.close()

    return str.replace('\n', ' ').replace('\r', '')


def make_new_log(log):
    file = open("new_log.txt", "w")
    file.write(log)
    file.close()


if __name__ == "__main__":

    res = ""
    log = load_log()
    dicts = ast.literal_eval(log)
    feature = Feature()
    for dict in dicts:
        feature.update_feature(dict)
        res += str(feature.__dict__) + ", "
    res = res[:len(res)-2]
    make_new_log(res)


