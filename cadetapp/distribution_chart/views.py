#-----------------------------------------------------------------------------
# Purpose:     Create views classes to deliver the topic results and
#              instructor results to the viewer.
# Classes:     ChartTopicData, ChartTopicWordData, and ChartInstructorData
#
# proposed JSON structure for controller.views:
#   For ChartTopicWordData Class
#    topic_word_data = {
#          "topic": [
#            {
#              "topic_id": "1",
#              "words": "happy, good, fun, yay, smile"
#            },
#            {
#              "topic_id": "2",
#              "words": "sad, boo, mean, hard, lethal"
#            },
#            {
#              "topic_id": "3",
#              "words": "hub, hubba, buh, duh, huh"
#            },
#            {
#              "topic_id": "4",
#              "words": "foo, baz, exe, why, zee"
#            },
#            {
#              "topic_id": "5",
#              "words": "red, white, blue, yellow, green"
#            }
#          ]
#        }
#-----------------------------------------------------------------------------

from rest_framework.response import Response
from rest_framework.views import APIView
from controller.views import *

# method 1 of delivering json and instance obj data
def get_chart_data(request, *args, **kwargs):
    data = {
        "comments_count": 10,
        "anon_id": 2,
    }
    return JsonResponse(data)

# Manipulate the topic chart
class ChartTopicData(APIView):
    """
    Purpose: call computeTopicResults, parse into proposed json structure to be
    delivered to response data for the api request

    Return: data object in json structure

    How: Populate the topic chart with the number of positive, neutral, and
    negative comments per topic. Data is received from results/views.py
    """
    def get(self, request, format=None):
        # retrieve results from results/views.py
        pos_list = computeTopicResults()[1]
        neu_list = computeTopicResults()[2]
        neg_list = computeTopicResults()[3]  
        
        length = len(pos_list)
        data = {'topic':[]}
        # populate chart
        for x in range(length):
            data['topic'].append({
            "topic_id": x+1,
                "sentiment_count": [
                    {
                    "pos": pos_list[x],
                    "neu": neu_list[x],
                    "neg": neg_list[x]
                    }
                ]
            })
        return Response(data)

# Manipulate the topic word panel below topic chart
class ChartTopicWordData(APIView):
    """
    Purpose: call computeTopicResults, parse into proposed json structure
    for topic-to-word mapping to be delivered to response data for the
    api request

    Return: data object in json structure

    How: Populate the panel below the topic chart with the list of words
    per topic. Data is recieved from results/views.py
    """
    def get(self, request, format=None):
        # retrieve data from results/views.py
        topic_word_list = computeTopicResults()[0]

        length = len(topic_word_list)
        data = {'topic':[]}
        # populate word list panel below topic chart
        for x in range(length):
            data['topic'].append({
            "topic_id": x+1,
            "words": topic_word_list[x]
            })
        return Response(data)

class ChartInstructorData(APIView):
    """
    Purpose: call computeTopicResults, parse into proposed json structure
    for topic-to-word mapping to be delivered to response data for the
    api request

    Return: data object in json structure

    How:Populate the instructor chart with the number of positive, neutral, and
    negative comments per instructor. Data is received from results/views.py
    """

    def get(self, request, format=None):
        # retrieve data from results/views.py
        inst_name_list = computeInstructorResults()[0]
        pos_list = computeInstructorResults()[1]
        neu_list = computeInstructorResults()[2]
        neg_list = computeInstructorResults()[3]  
        
        length = len(pos_list)
        data = {'instructor':[]}
        # populate instructor chart
        for x in range(length):
            data['instructor'].append({
            "instructor_name": inst_name_list[x],
                "sentiment_count": [
                    {
                    "pos": pos_list[x],
                    "neu": neu_list[x],
                    "neg": neg_list[x]
                    }
                ]
            })
        return Response(data)

