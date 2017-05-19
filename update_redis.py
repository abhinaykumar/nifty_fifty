import requests
import redis
import time
import cherrypy

r = redis.StrictRedis(host='localhost', port=6379)
class NiftyFifty(object):
    def nifty_list():
        response = requests.get('https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json')
        r.set('nifty', response.text)
        return None

if __name__ == "__main__":
    cherrypy.quickstart(NiftyFifty())
    nifty_list()
        time.sleep(300)
