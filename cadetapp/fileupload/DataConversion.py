import os
import csv
import json

# Added Class DataConversion.py and function through which the program
# receives a CSV file (without regard for delimiter) and converts it to
# a JSON object. The JSON object format has been adjusted and is agreed
# on by both the data layer team and display team and is codified in the
# AnalysisRequest.json file.


class CSVfiletoJSONobj:
	#Initialized to expected JHU comment format input
	def _init_(self):
		self.inputpath = 'string'
		self.outputpath = 'string'
		self.fieldnames = ("anon_id","program","modality",
						   "course_num_sect_id","instructor_last_name",
						   "instructor_first__name", "course_comments",
						   "instructor_comments","additional_comments")

	#Getters and Setters.
	def get_input_path(self):
		return self.inputpath

	def get_output_path(self):
		return self.outputpath

	def get_fieldnames(self):
		return self.fieldnames

	def set_input_path(self, StringEnter):
		self.inputpath = StringEnter

	def set_output_path(self, StringEnter):
		self.outputpath = StringEnter

	def set_fieldnames(self, fields):
		self.fieldnames.append(fields)
		
	# CSV to JSON Method formats the information deliberately based on Back-
	# End expectations.
	def CSVtoJSON_Obj(self):
		csvfile = open(self.inputpath, 'r')
		jsonfile = open(self.outputpath, 'w')
		reader = csv.DictReader(csvfile, self.fieldnames)
		next(reader)
		next(reader)
		json_list = []
		for row in reader:
			json_list.append(row)
		json.dump(json_list, jsonfile)


