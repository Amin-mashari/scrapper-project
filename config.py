import yaml

# Read YAML file


def read_conf_data():
    with open('config.yml', 'r') as f:
        conf_data = yaml.load(f, Loader=yaml.SafeLoader)

    return conf_data
