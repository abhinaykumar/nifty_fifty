import requests
import redis
import time

r = redis.StrictRedis(host='localhost', port=6379)

def nifty_list():
    response = requests.get('https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json')
    r.set('nifty', response.text)
    print response.text
    return None

if __name__ == "__main__":
    while True:
        nifty_list()
        time.sleep(300)
