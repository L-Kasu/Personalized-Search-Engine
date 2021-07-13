import json


def write_config(config, path="./config/config.json"):
    with open(path, 'w') as file:
        json.dump(config, file)
        file.close()


def edit_config(key, value, path="./config/config.json"):
    with open(path, 'r') as file:
        config = json.load(file)
        config[key] = value
        file.close()
    with open(path, 'w') as file:
        json.dump(config, file)
        file.close()


def get_config(key, path="./config/config.json"):
    with open(path, 'r') as file:
        config = json.load(file)
        value = config[key]
        file.close()
    return value
