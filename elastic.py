from time import sleep
import traceback
import elasticsearch
import json

es = elasticsearch.Elasticsearch("http://elasticsearch:9200")


def check_connection():
    if es.ping():
        return True
    return False


def savedata(data):
    print("aa")
    sleep(8)

    if not es.ping():
        print("ping:{}".format(es.ping()))
        print("connection Error")
        print(traceback.format_exc())
        exit(1)
  
    print("ELASTIC CONNECTED...!")
    js = json.loads(data)
    for d in js["results"]:
        # print(d)
        # print(type(doc))
        resp = es.index(index="test-index",document=d)
        # print(resp['result'])

    # resp = es.get(index="test-index")
    # print(resp['_source'])
