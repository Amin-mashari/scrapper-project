import elasticsearch

es = elasticsearch.Elasticsearch("http://elasticsearch:9200")

def check_connection():
    if es.ping():
        return True
    return False


def savedata(data):

    print("before connection...")
    if not check_connection():
        raise ValueError("Connection failed")

    print("after connection..")
    
    for d in data["results"]:
        resp = es.index(index="index", document=d)
        print(resp['result'])
   

    resp = es.get(index="index")
    print(resp['_source'])
