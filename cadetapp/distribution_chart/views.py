from rest_framework.response import Response
from rest_framework.views import APIView
from controller.views import *

# Dashboard model dependencies
#from dashboard.models import Result


# method 1 of delivering json and instance obj data
def get_chart_data(request, *args, **kwargs):
    data = {
        "comments_count": 10,
        "anon_id": 2,
    }
    return JsonResponse(data)

# refactored class-based way of delivering json withr django rest framework
class ChartTopicData(APIView):
    # here is the class that converts data from our Django-backend.
    # the models have already been updated with results from the Flask-backend
    # Stub data for now, later instantiate instances from Ashley's models

    def get(self, request, format=None):
        # this is the structure of my expected nested json result object        
        pos_list = computeTopicResults()[1]
        neu_list = computeTopicResults()[2]
        neg_list = computeTopicResults()[3]  
        
        length = len(pos_list)
        data = {'topic':[]}
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

class ChartTopicWordData(APIView):
    # function return mapping of topic and words associated with that topic
    def get(self, request, format=None):
        topic_word_list = computeTopicResults()[0]

        length = len(topic_word_list)
        data = {'topic':[]}
        for x in range(length):
            data['topic'].append({
            "topic_id": x+1,
            "words": topic_word_list[x]
            })
        
#        topic_word_data = {
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
        return Response(data)

class ChartInstructorData(APIView):
    def get(self, request, format=None):
        inst_name_list = computeInstructorResults()[0]
        pos_list = computeInstructorResults()[1]
        neu_list = computeInstructorResults()[2]
        neg_list = computeInstructorResults()[3]  
        
        length = len(pos_list)
        data = {'instructor':[]}
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
