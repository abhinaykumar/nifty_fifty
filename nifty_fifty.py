import cherrypy
import requests
from os import path, curdir
import redis
import json

class NiftyFifty(object):
	@cherrypy.expose
	def index(self):
		return file("views/nifty/index.html")

	@cherrypy.expose
	def new
		response = requests.get('https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json')
		j = response.text.encode('utf-8')
		js = json.dumps(j)
		print type(js)
		r = redis.StrictRedis(host='localhost', port=6379)
		json_response = json.dumps(response.text)
		r.set('nifty', json_response)
		get_redis= json.loads(r.get('nifty'))

# cherrypy.config.update({'server.socket_host': '0.0.0.0',
#                         'server.socket_port': 8080,
#                        })
cherrypy.quickstart(NiftyFifty(), "/", { "/views": {
                        "tools.staticdir.on": True,
                        "tools.staticdir.dir" : path.join(path.abspath(curdir), "views")}})
