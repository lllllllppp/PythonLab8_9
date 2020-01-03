import glob
import json


def get_files(path):
    return glob.glob(path + '*')


def read_file(file):
    with open(file, 'r', encoding="utf-8") as f:
        return f.read()


def print_json(dictionary):
    print(json.dumps(dictionary, indent=2))
