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
		nifty_list = r.get('nifty')
		json_response = json.dumps(nifty_list)
		return json_response

	@cherrypy.expose
	def new(self, _):
		r = redis.StrictRedis(host='localhost', port=6379)
		response = requests.get('https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json')
		r.set('nifty', response.text)
		return None

	@cherrypy.expose
	def logo(self, _, symbol):
		company_details = requests.get("https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/companySnapshot/getContactDetails"+symbol+".json")
		dict_reponse = ast.literal_eval(company_details.text)
		web_address = dict_reponse["rows"][0]["webAddress"]
		return web_address

cherrypy.config.update({'server.socket_host': '0.0.0.0',
                        'server.socket_port': 8280,
                       })
cherrypy.quickstart(NiftyFifty(), "/", { "/views": {
                        "tools.staticdir.on": True,
                        "tools.staticdir.dir" : path.join(path.abspath(curdir), "views")}})
