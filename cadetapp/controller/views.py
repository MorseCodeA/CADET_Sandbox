import json

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from results.models import Results_Set

# The purpose of this file is to take Results_Set that stores information 
# from the data layer in results/views.py and compute the information to 
# display in the topic and instructor chart in distribution_chart/views.py.

# Parse JSON result for instrctor chart
def computeTopicResults():
    # retrieve JSON
	last_result = Results_Set.objects.all().order_by('-id')[0]
	result_JSON = last_result.jsonObjs
	
	topic_JSON = result_JSON[0]['results']['topics_stats']
	num_of_topics = len(topic_JSON)
	
	topic_word_list = []
	pos_list = []
	neu_list = []
	neg_list = []
	
	for x in range(num_of_topics):
	    topic_word_list.append(topic_JSON[x]['words'])
	    pos_list.append(len(topic_JSON[x]['comments']['positive']))
	    neu_list.append(len(topic_JSON[x]['comments']['neutral']))
	    neg_list.append(len(topic_JSON[x]['comments']['negative']))
	    
	result = [topic_word_list, pos_list, neu_list, neg_list]
	return result
# END function computeTopicResults

# Parse JSON result for instructor chart	
def computeInstructorResults():
    # retrieve JSON
    last_result = Results_Set.objects.all().order_by('-id')[0]
    result_JSON = last_result.jsonObjs
    
    inst_JSON = result_JSON[0]['results']['instructor_stats']
    num_of_inst = len(inst_JSON)
	
    inst_name_list = []
    pos_list = []
    neu_list = []
    neg_list = []
	
    for x in range(num_of_inst):
	    inst_name_list.append(inst_JSON[x]['instructor_first_name'] + " " +\
	    inst_JSON[x]['instructor_last_name'])
	    pos_list.append(len(inst_JSON[x]['comments']['positive']))
	    neu_list.append(len(inst_JSON[x]['comments']['neutral']))
	    neg_list.append(len(inst_JSON[x]['comments']['negative']))
	    
    result = [inst_name_list, pos_list, neu_list, neg_list]
    return result
# END function computeInstructorResults
