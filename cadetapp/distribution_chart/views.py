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
        # currently it is hard coded, but later I expect to grab Results_Topic instance 
        # data = {}
        # data["topic"] = []
        
        # get data from data layer
#        comment_list = []
#        # organize data and compute comment tones
#        topic_id_list = organizeTopicCommentResults(comment_list)[0]
#        pos_list = organizeTopicCommentResults(comment_list)[1]
#        neu_list = organizeTopicCommentResults(comment_list)[2]
#        neg_list = organizeTopicCommentResults(comment_list)[3] 
#        
#        data = {"topic": []}
#        for t in topic_id_list:
#            data.update({
#                "topic_id": t,
#                "sentiment_count": [
#                    {
#                    "pos": pos_list[t],
#                    "neu": neu_list[t],
#                    "neg": neg_list[t]
#                    }
#                ]
#            })
           
            
                
        data = {
          "topic": [
            {
              "topic_id": "1",
              "sentiment_count": [
                {
                  "pos": "15",
                  "neu": "5",
                  "neg": "14"
                }
              ]
            },
            {
              "topic_id": "2",
              "sentiment_count": [
                {
                  "pos": "11",
                  "neu": "19",
                  "neg": "3"
                }
              ]
            },
            {
              "topic_id": "3",
              "sentiment_count": [
                {
                  "pos": "13",
                  "neu": "6",
                  "neg": "11"
                }
              ]
            },
            {
              "topic_id": "4",
              "sentiment_count": [
                {
                  "pos": "19",
                  "neu": "2",
                  "neg": "8"
                }
              ]
            },
            {
              "topic_id": "5",
              "sentiment_count": [
                {
                  "pos": "7",
                  "neu": "9",
                  "neg": "15"
                }
              ]
            }
          ]
        }
        return Response(data)

class ChartTopicWordData(APIView):
    # function return mapping of topic and words associated with that topic
    def get(self, request, format=None):
        # getting last five topic obj
        # topic_obj = Topic.objects.all().order_by('-id')[:5]
        # topic_word_data {}
        # topic_word_data["topic"] = {}
        # iterate and push the topic data to the same formal as bellow
        
        # get data from data layer
#        topic_list = []
#        # organize data and compute comment tones
#        topic_id_list = organizeTopicWordResults(topic_list)[0]
#        topic_word_list = organizeTopicCommentResults(topic_list)[1]
#        
#        topic_word_data = {"topic": []}
#        for t in topic_id_list:
#            data.update({
#                "topic_id": t,
#                "words": topic_word_list[t]
#            })
        
        topic_word_data = {
          "topic": [
            {
              "topic_id": "1",
              "words": "happy, good, fun, yay, smile"
            },
            {
              "topic_id": "2",
              "words": "sad, boo, mean, hard, lethal"
            },
            {
              "topic_id": "3",
              "words": "hub, hubba, buh, duh, huh"
            },
            {
              "topic_id": "4",
              "words": "foo, baz, exe, why, zee"
            },
            {
              "topic_id": "5",
              "words": "red, white, blue, yellow, green"
            }
          ]
        }
        return Response(topic_word_data)

class ChartInstructorData(APIView):
    def get(self, request, format=None):
        # get data from data layer
#        inst_name_list = []
#        # organize data and compute comment tones
#        topic_id_list = organizeInstructorCommentResults(inst_name_list)[0]
#        pos_list = organizeInstructorCommentResults(inst_name_list)[1]
#        neu_list = organizeInstructorCommentResults(inst_name_list)[2]
#        neg_list = organizeInstructorCommentResults(inst_name_list)[3] 
#        
#        data = {"instructor": []}
#        for t in topic_id_list:
#            data.update({
#                "instructor_name": t,
#                "sentiment_count": [
#                    {
#                    "pos": pos_list[t],
#                    "neu": neu_list[t],
#                    "neg": neg_list[t]
#                    }
#                ]
#            })
        
    
        instructor_data = {
          "instructor": [
            {
              "instructor_name": "joe smoe",
              "sentiment_count": [
                {
                  "pos": "28",
                  "neu": "8",
                  "neg": "2"
                }
              ]
            },
            {
              "instructor_name": "nathalie fozz",
              "sentiment_count": [
                {
                  "pos": "15",
                  "neu": "3",
                  "neg": "7"
                }
              ]
            },
            {
              "instructor_name": "beavis butthead",
              "sentiment_count": [
                {
                  "pos": "38",
                  "neu": "8",
                  "neg": "2"
                }
              ]
            },
            {
              "instructor_name": "boaty boatface",
              "sentiment_count": [
                {
                  "pos": "19",
                  "neu": "2",
                  "neg": "8"
                }
              ]
            },
            {
              "instructor_name": "numbly doo",
              "sentiment_count": [
                {
                  "pos": "7",
                  "neu": "8",
                  "neg": "20"
                }
              ]
            }
          ]
        }
        return Response(instructor_data)
