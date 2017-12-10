import csv
import json
import os

#----------------------------------------------------------------------

class CSVfiletoJSONobj:
	#("anon id","Program","Modality","Course Number/ Section ID","Instructor Last Name", "Instructor First Name", "Course comments","Instructor comments","[Additional comments, if available]")
	
	def _init_(self):
		self.inputpath = 'string'
		self.outputpath = 'string'
		self.fieldnames = ("anon id","Program","Modality","Course Number/ Section ID","Instructor Last Name", "Instructor First Name", "Course comments","Instructor comments","[Additional comments, if available]")

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
		json_list = {}
		totalrows = 0
		for row in reader:
			json_list[totalrows] = row
			totalrows += 1
		json.dump(json_list, jsonfile)


