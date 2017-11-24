from rest_framework.response import Response
from rest_framework.views import APIView
# Dashboard model dependencies
from dashboard.models import Result

# method 1 of delivering json and instance obj data
def get_chart_data(request, *args, **kwargs):
    data = {
        "comments_count": 10,
        "anon_id": 2,
    }
    return JsonResponse(data) # http response

# refactored class-based way of delivering json withr django rest framework
class ChartTopicData(APIView):
    # here is the class that grabs that converts data from our Django-backend.
    # the models have already been updated with results from the Flask-backend
    # Stub data for now, later instantiate instances from Ashley's models,
    # which will include instance from Results.  Notice the saved data will
    # need to be converted back (again) into JSON format in the final step,
    # since that is compatible with AJAX call for frontend
    def get(self, request, format = None):        
        # hardcoded for now, until we get the updated data from Results model 
        data = {
                "Topic 1": {
                    "positive": "15",
                    "neutral": "2",
                    "negative": "12",
                },
                "Topic 2": {
                   "positive": "9",
                    "neutral": "2",
                    "negative": "37",
                },
                "Topic 3": {
                    "positive": "8",
                    "neutral": "2",
                    "negative": "32",
                },
                "Topic 4": {
                    "positive": "5",
                    "neutral": "8",
                    "negative": "20",
                },
                "Topic 5": {
                    "positive": "5",
                    "neutral": "29",
                    "negative": "2",
                },
        }
        return Response(data)

class ChartTopicWordData(APIView):
    # function return mapping of topic and words associated with that topic
    def get(self, request, format = None):
        topic_word_data = {
            "Topic 1": ["happy, good, fun, yay, smile"],
            "Topic 2": ["sad, boo, mean, hard, lethal"],
            "Topic 3": ["happy, good, fun, yay, smile"],
            "Topic 4": ["happy, good, fun, yay, smile"],
            "Topic 5": ["happy, good, fun, yay, smile"],
        }
        return Response(topic_word_data)

class ChartInstructorData(APIView):
    def get(self, request, format = None):
        instructor_data = {
                "Instructor Full Name 1": {
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
