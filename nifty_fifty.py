import cherrypy
import requests
from os import path, curdir
import redis
import json
import ast

class NiftyFifty(object):
	@cherrypy.expose
	def index(self):
		return file("views/nifty/index.html")

	@cherrypy.expose
	def show(self, _):
		r = redis.StrictRedis(host='localhost', port=6379)
		nifty_list = json.dumps(r.get('nifty'))
		return nifty_list

	@cherrypy.expose
	def logo(self, _, symbol):
		r = redis.StrictRedis(host='localhost', port=6379)
		web_address = r.get(symbol)
		print web_address
		return web_address

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8280,
                       })
cherrypy.quickstart(NiftyFifty(), "/", { "/views": {
                        "tools.staticdir.on": True,
                        "tools.staticdir.dir" : path.join(path.abspath(curdir), "views")}})
