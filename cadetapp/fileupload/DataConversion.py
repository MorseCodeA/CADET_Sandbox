import csv
import json
import os

#----------------------------------------------------------------------

class CSVfiletoJSONobj:
	
	def _init_(self):
		self.inputpath = 'string'
		self.outputpath = 'string'
		self.fieldnames = ("anon_id","program","modality","course_num_sect_id","instructor_last_name", "instructor_first__name", "course_comments","instructor_comments","additional_comments")

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


