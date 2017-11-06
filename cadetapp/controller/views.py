import json

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Comment, Instructor, Course, Topic, Result, Stopword

# The purpose of this file is to take Josh's query from the data layer and 
# organize the information woth the structure from /dashboard/models.py. 
# This will then be called by Anh's code to display.

def organizeResults(result):
    #parse json
    parsed_json = json.loads(result.GET)
    #fit the json into the models.py
    for result in parsed_json[results]:
        if result == "topic_stats":
	    for topic in result.iterItems():
		# get topic id
		Topic.topic_id = topic["topic_id"]
		# iterate through comments and track the tone
		
		    
	elif result == "instructor_stats":
	    for instructor in result.iterItems():
		# get the course, last, first name
		# get the comments and track the tone
    #return HttpResponse("results for the graph")

