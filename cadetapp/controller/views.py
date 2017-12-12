import json

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from results.models import Results_Set

# The purpose of this file is to take Results_Set that stores information 
# from the data layer in results/views.py and compute the information to 
# display in the topic and instructor chart in distribution_chart/views.py.

# Parse JSON result for instructor chart
def computeTopicResults():
    """
    Purpose: Parse JSON result to populate topic chart.

    Return: a list with 4 values: a list of a list of words that correspond to 
    each topic, a list of the number of postive comments per topic, a list of 
    the number of neutal comments per topic, and a list of the negative 
    comments per topic.

    How: Retrieve the latest result JSON, parse it, then obtain the list of 
    words, and number of postive, netural, and negative comments per each 
    topic.
    """
    # retrieve the most recent JSON, which is determined by its result id
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

# Parse JSON result for instructor chart	
def computeInstructorResults():
    """
    Purpose: Parse JSON result to populate instructor chart.

    Return: a list with 4 values: a list of a the instructor's first and last 
    name per instruictor, a list of the number of postive comments per 
    inctructor, a list of the number of neutal comments per instructor, and a 
    list of the negative comments per instructor.

    How: Retrieve the latest result JSON, parse it, then obtain the 
    instructor's first and last name, and number of postive, netural, and 
    negative comments per each instructor.
    """
    # retrieve the most recent JSON, which is determined by its result id
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
