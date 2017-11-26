import json

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from dashboard.models import Comment, Instructor, Course, Topic

# The purpose of this file is to take Josh's query from the data layer and 
# organize the information woth the structure from /dashboard/models.py. 
# This will then be called by Anh's code to display.

# I am assuming that I am recieving an array of topic objects and an 
# array of comment objects. A topic object has the word and topic_ID, and
# a comment object will have the tone, which I can use to count the pos,
# neu, and neg values.
def organizeTopicCommentResults(comment_list):
	topic_id_list = []
	# find out how many topic_ids there are
	for comment in comment_list:
		topic_id_list.append(comment.topic_id)
	
	# this list has sorted unique values of topic ids (ex: [1,2,3,4,5])
	topic_id_list = sorted(list(set(topic_id_list)))
	num_topics = len(topic_id_list)

	# create the tone lists and initlaize it to zero
	pos_list = [0] * num_topics
	neu_list = [0] * num_topics
	neg_list = [0] * num_topics	

	for topic_id in topic_id_list:
		for comment in comment_list:
			if (comment.topic_id == topic_id):
				if (comment.tone == 'pos'):
					++pos_list[topic_id];
				elif (comment.tone == 'neu'):
					++neu_list[topic_id]
				elif (comment.tone == 'neg'):
					++neg_list[topic_id]

	result = [topic_id_list, pos_list, neu_list, neg_list]
	return result

def organizeTopicWordResults(topic_list):
	topic_id_list = []
	# find out how many topic_ids there are
	for topic in topic_list:
		topic_id_list.append(topic.topic_id)
	
	# this list has sorted unique values of topic ids (ex: [1,2,3,4,5])
	topic_id_list = sorted(list(set(topic_id_list)))
	num_topics = len(topic_id_list)

	# create a list of lists that map to the topic_id
	topic_word_list = [] * num_topics
	
	for topic_id in topic_id_list:
		for topic in topic_list:
			if (topic.topic_id == topic_id):
				topic_word_list[topic_id].append(topic.text)

	result = [topic_id_list, topic_word_list]
	return result


def organizeInstructorCommentResults(comment_list):
	inst_name_list = []
	# find out how many instructors there are
	for comment in comment_list:
		name = Instructor.first_name + " " + Instructor.last_name
		inst_name_list.append(name)
	
	# this list has unique values of instructors (ex: [1,2,3,4,5])
	inst_name_list = list(set(topic_id_list))
	num_topics = len(topic_id_list)

	# create the tone lists and initlaize it to zero
	pos_list = [0] * num_topics
	neu_list = [0] * num_topics
	neg_list = [0] * num_topics	

	for instructor in inst_name_list:
		for comment in comment_list:
			name_model = Instructor.first_name + " " + Instructor.last_name
			if (name_model == instructor):
				if (comment.tone == 'pos'):
					++pos_list[topic_id];
				elif (comment.tone == 'neu'):
					++neu_list[topic_id]
				elif (comment.tone == 'neg'):
					++neg_list[topic_id]

	result = [topic_id_list, pos_list, neu_list, neg_list]
	return result 		

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
