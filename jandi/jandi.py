import urllib3
import json


class Jandi:
	class Colors:
		RED = "#CD0000"
		BLUE = "#0000CD"
		GREEN = "#00C957"
		YELLOW = "#FFFF00"
		PURPLE = "#836FFF"
		SILVER = "#C0C0C0"
		SALMON = "#FA8072"
		BLACK = "#292421"
		WHITE = "#F5F5F5"
		ORANGE = "#FF8000"
		ORANGERED = "#FF4500"
		EMERALD = "#00997B"

	__infos = []

	def __init__(self, url):
		self.__url = url
		self.__headers = {
			'Accept': 'application/vnd.tosslab.jandi-v2+json',
			'Content-Type': 'application/json'
		}
		self.__session = urllib3.PoolManager()

	def push_info(self, title: str, description: str):
		self.__infos.append({"title": title, "description": description})

	def send(self, headline: str, infos: list = None, color: str = Colors.SILVER) -> urllib3.response.HTTPResponse:
		_content = dict()
		_content['body'] = headline
		if infos is None:
			_content["connectInfo"] = self.__infos
		else:
			_content["connectInfo"] = infos

		_content["connectColor"] = color

		res = self.__session.request("POST", self.__url, headers=self.__headers, body=json.dumps(_content))
		if infos is None:
			self.__infos.clear()
		return res

