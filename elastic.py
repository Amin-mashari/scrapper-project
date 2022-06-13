from config import read_conf_data
from time import sleep
import traceback
import elasticsearch
import json

path = "config.yml"


def load_elastic(conf):
    # print("CONF:::")
    # print(conf)

    LINK = "http://{}:{}".format(conf["elastic"]
                                 ["HOST"], conf["elastic"]["PORT"])
    return elasticsearch.Elasticsearch(LINK)


def check_connection():
    es = load_elastic(read_conf_data(path))

    if es.ping():
        return True
    return False


def save_in_elstic(d):

    es = load_elastic(read_conf_data(path))
    resp = es.index(index="test-index", document=d)
    # print(resp['result'])


def savedata(data):
    print("wait for connection...")
    sleep(8)

    if not check_connection():
        print("ping:{}".format(check_connection()))
        print("connection Error")
        print(traceback.format_exc())
        exit(1)

    print("ELASTIC CONNECTED...!")
    for d in data["results"]:
        # print(d)
        save_in_elstic(d)

    print("data puting has done..")


