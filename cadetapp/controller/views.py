import json

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from dashboard.models import Comment, Instructor, Course, Topic

# The purpose of this file is to take Josh's query from the data layer and 
# organize the information woth the structure from /dashboard/models.py. 
# This will then be called by Anh's code to display.
#def organizeResults(result):
    # parse json
#    parsed_json = json.loads(result.GET)
    
    #### Iterate through topics stats ####
#    for topic in parsed_json[results][topics_stats]:
#       topic_record = Topic(topic_id = topic.topic_id)
#        topic_record.save()
#        for pos_comm in topic[comments][postive]:
#            pos_comment_record = Comment(tone = 'pos', text = pos_comm)
#            pos_comment_record.save()
#        for neu_comm in topic[comments][neutral]:
#            neu_comment_record = Comment(tone = 'neu', text = neu_comm)
#            neu_comment_record.save()
#        for neg_comm in topic[comments][negative]:
#            neg_comment_record = Comment(tone = 'neg', text = neg_comm)
#            neg_comment_record.save()
	
#    for instructor in parsed_json[results][instructor_stats]:
#        instructor_record = Instructor(courses = instructor.course_num_sect_id, 
#				first_name = instructor_first_name,
#				last_name = instructor_last_name)
#        instructor_record.save()
#        for pos_comm in instructor[comments][postive]:
#            pos_comment_record = Comment(tone = 'pos', text = pos_comm)
#            pos_comment_record.save()
#        for neu_comm in instructor[comments][neutral]:
#            neu_comment_record = Comment(tone = 'neu', text = neu_comm)
#            neu_comment_record.save()
#        for neg_comm in instructor[comments][negative]:
#            neg_comment_record = Comment(tone = 'neg', text = neg_comm)
#            neg_comment_record.save()

#    return HttpResponse("results for the graph")