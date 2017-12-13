import json
from django.shortcuts import render, redirect
import requests
from pprint import pprint

class DataPush:
	def _init_(self):
		self.url = 'http://localhost:5000/api/AddDataset'

	def set_url(self, StringEnter):
		self.url = StringEnter

	def get_url(self, StringEnter):
		return self.url

	def ReadParamsObject(self, Comments, Topics, Iterations):
		params = {}
		params['document_id_number']=1
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
		strfinalJSON = str(finalJSON)
		strfinalJSON = strfinalJSON.replace("\'", "\"")
		finalJSON = json.loads(strfinalJSON)
		self.PushObject(strfinalJSON)

	def PushObject(self, data_json):
		response = requests.post(self.url, data_json)
		print('THIS IS THE NUBER JOSH NEEDS!   = ', response.json)
		return redirect('views.retrieve', result_id=response)
