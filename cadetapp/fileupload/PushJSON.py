import json
import requests

from pprint import pprint
from django.shortcuts import render, redirect

# Added Modile  PushJSON.py  and method which takes the formatted JSON object
# so that it can be sent to a specified IP for the data layer team to be able
# to access. The REST API request POST method is used in the order to achieve
# this functionality.

class DataPush:
	# Initialize connection to specified database. 
	def _init_(self):
		self.url = 'http://localhost:5000/api/AddDataset'

	# Getters and Setters.
	def set_url(self, StringEnter):
		self.url = StringEnter

	def get_url(self, StringEnter):
		return self.url

	# Add Analysis Parameters applied to selected JSON files. 
	def ReadParamsObject(self, Comments, Topics, Iterations):
		params = {}
		params['document_id_number']=1
		params['user_selected_words_per_topic'] = Comments
		params['user_selected_number_topics'] = Topics
		params['user_selected_number_iterations'] = Iterations
		return params

	# Read in JSON files. 
	def ReadJSONObject(self, StringEnter):
		with open(StringEnter) as json_data:
		    data_json = json.load(json_data)
		return data_json

	# Take Final JSON and POST to Back End server. 	
	def SendObject(self, data_json):
		response = requests.post(self.url, data_json).json()
		return redirect('views.retrieve', result_id=response)

	# Construct JSON with Analysis Parameters and Comments and call SendObject 
	# method.
	def PushJSONObject(self, Comments, Topics, Iterations, StringEnter):
		finalJSON={}
		finalJSON['meta_file_info'] = self.ReadParamsObject(Comments,Topics, 
																Iterations)
		finalJSON['raw_file_stats'] = self.ReadJSONObject(StringEnter)
		strfinalJSON = str(finalJSON)
		strfinalJSON = strfinalJSON.replace("\'", "\"")
		finalJSON = json.loads(strfinalJSON)
		self.SendObject(strfinalJSON)

