import yaml

# Read YAML file


def read_conf_data(path):
    with open(path, 'r') as f:
        conf_data = yaml.load(f, Loader=yaml.SafeLoader)

    return conf_data


def isYml(path):
    if path.endswith(".yaml") or path.endswith(".yml"):
        return True
    else:
        return False


def load_config(config_data):

    # [schedule]
    if not config_data.get("schedule"):
        return "schedule not found in config.yml !"
    # [schedule][sch_format]
    if not isinstance(config_data["schedule"], dict):
        return "schedule data format is not dictionary !"

     # [elastic]
    if not config_data.get("elastic"):
        return "elastic not found in config.yml !"

    # elastic: {}
    if not isinstance(config_data["elastic"], dict):
        return "elastic data format is not dictionary !"

    # elastic[HOST]

    if not isinstance(config_data["elastic"]["HOST"], str):
        return "elastic data format is not string !"
    
    if not config_data["elastic"].get("HOST"):
        return "elastic host is missing in config.yml .."

    if not config_data["elastic"].get("PORT"):
        return "elastic port is missing in config.yml .."

    if not str(config_data["elastic"]["PORT"]).isdigit():
        return "elastic data format is not string !"

    return None
