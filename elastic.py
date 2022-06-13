from distutils.command.config import config
from time import sleep
import traceback
import elasticsearch
import json

CONF = config.read_conf_data()


def load_elastic(conf):
    LINK = "http://{}:{}".format(CONF["elastic"]
                                 ["LINK"], CONF["elastic"]["PORT"])
    return elasticsearch.Elasticsearch(LINK)


def check_connection():
    es = load_elastic()

    if es.ping():
        return True
    return False


def save_in_elstic(d):

    es = load_elastic()
    es.index(index="test-index", document=d)

def savedata(data):
    print("aa")
    sleep(8)

    if not check_connection():
        print("ping:{}".format(check_connection()))
        print("connection Error")
        print(traceback.format_exc())
        exit(1)

    print("ELASTIC CONNECTED...!")
    js = json.loads(data)
    for d in js["results"]:
        # print(d)
        # print(type(doc))
        save_in_elstic(d)
        # print(resp['result'])

    # resp = es.get(index="test-index")
    # print(resp['_source'])
