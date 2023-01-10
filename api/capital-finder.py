from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		"""
		This function sends a request to REST api and returns requested info"
		"""
		s = self.path
		url_bits = parse.urlsplit(s)
		parsed_list = parse.parse_qsl(url_bits.query)
		new_dic = dict(parsed_list)

		if 'country' in new_dic:
			country = new_dic['country']
			url = "https://restcountries.com/v3.1/name/"
			r = requests.get(url + country.lower())
			data = r.json()
			capital = str(data[0]['capital'][0])
			message = f"The capital of {new_dic['country'].capitalize()} is {capital.capitalize()}"

		# change back elif when working
		elif 'capital' in new_dic:
			capital = new_dic['capital']
			url = "https://restcountries.com/v3.1/capital/"
			r = requests.get(url + capital.lower())
			data = r.json()
			country = str(data[0]['name']['common'])
			message = f"{new_dic['capital'].capitalize()} is the capital of {country.capitalize()}"
		else:
			message = "Enter a valid country or capital name"

		self.send_response(200)
		self.send_header('Content-type', 'text/plain')
		self.end_headers()
		self.wfile.write(message.encode())

		return
