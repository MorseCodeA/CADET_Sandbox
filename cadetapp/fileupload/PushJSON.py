import json
import requests
from pprint import pprint

class DataPush:
	def _init_(self):
		self.url = 'https://requestb.in/rx85inrx'

	def set_url(self, StringEnter):
		self.url = StringEnter

	def get_url(self, StringEnter):
		return self.url

	def ReadParamsObject(self, Comments, Topics, Iterations):
		params = {}
		params['user_selected_words_per_topic'] = Comments
		params['user_selected_number_topics'] = Topics
		params['user_selected_number_iterations'] = Iterations
		return params

	def ReadJSONObject(self, StringEnter):
		with open(StringEnter) as json_data:
		    data_json = json.load(json_data)
		return data_json

	def PushJSONObject(self, Comments, Topics, Iterations, StringEnter):
		finalJSON={}
		finalJSON['meta_file_info'] = self.ReadParamsObject(Comments, Topics, Iterations)
		finalJSON['raw_file_stats'] = self.ReadJSONObject(StringEnter)
		print(finalJSON)
		self.PushObject(finalJSON)


	def PushObject(self, data_json):
		headers =  data_json.keys()
		response = requests.post(self.url, data_json, headers)
		print(response.content)
		return response.content