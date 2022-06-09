import requests

URL = "https://otx.alienvault.com/api/v1/pulses/subscribed"
API_KEY = "d5c58f3278d36b93f2d35139a2a10638a3da4e707ebbfa8cb088ba5a289cac4e"

# curl -H "X-OTX-API-KEY: f59fa77f38fbc5c56e36aafc5cf72aa6d9852e6fe2ea125753f2718de3fe8930" https://otx.alienvault.com/api/v1/pulses/subscribed


def getdata():
     f = open("data.txt", "r")
     data = f.readline()
     return data



def run():
    print("requsting for getting data...!")
    r = requests.get(URL, headers={"OTX-API-KEY": API_KEY})
    print(r.status_code)
    print(r.json())

