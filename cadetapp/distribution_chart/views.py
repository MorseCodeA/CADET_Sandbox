from rest_framework.response import Response
from rest_framework.views import APIView

# Dashboard model dependencies
from dashboard.models import Comment, Instructor, Course, Topic

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
        topic_word_data = {
            "topic_id": ["happy, good, fun, yay, smile"],
            "topic_id": ["sad, boo, mean, hard, lethal"],
            "topic_id": ["happy, good, fun, yay, smile"],
            "topic_id": ["happy, good, fun, yay, smile"],
            "topic_id": ["happy, good, fun, yay, smile"],
        }
        return Response(topic_word_data)

class ChartInstructorData(APIView):
    def get(self, request, format=None):
        instructor_data = {"Instructor Full Name 1": {
                    "positive": "15",
                    "neutral": "2",
                    "negative": "12",
                },
                "Instructor Full Name 2": {
                    "positive": "9",
                    "neutral": "2",
                    "negative": "37",
                },
                "Instructor Full Name 3": {
                    "positive": "8",
                    "neutral": "2",
                    "negative": "32",
                },
                "Instructor Full Name 4": {
                    "positive": "5",
                    "neutral": "8",
                    "negative": "20",
                },
                "Instructor Full Name 5": {
                    "positive": "5",
                    "neutral": "29",
                    "negative": "2",
                },
        }
        return Response(instructor_data)

