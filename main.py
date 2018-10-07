import ast
from ml_feature import Feature


def load_log():
    str = ""
    file = open("log_file.txt", "r")
    file.readline()
    #logs = file.readlines()
    #for line in logs:
    #    str += line + ","
    str += file.readline() + ","
    str += file.readline() + ","
    file.close()

    return str.replace('\n', ' ').replace('\r', '')


if __name__ == "__main__":

    log = load_log()
    dicts = ast.literal_eval(log)
    feature = Feature()
    for dict in dicts:
        feature.update_feature(dict)
        print(feature.__dict__)