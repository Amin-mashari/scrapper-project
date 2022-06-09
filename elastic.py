import elasticsearch
import json

es = elasticsearch.Elasticsearch("http://elasticsearch:9200")


def check_connection():
    if es.ping():
        return True
    return False


def savedata(data):

    if not check_connection():
        raise ValueError("Connection failed")
    else:
        print("connected to elastic .!")

    js = json.loads(data)
    for d in js["results"]:
        resp = es.index(index="index", document=d)
    #     print(resp['result'])

    # resp = es.get(index="index")
    # print(resp['_source'])
