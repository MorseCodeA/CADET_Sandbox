from rest_framework.response import Response
from rest_framework.views import APIView
# Dashboard model dependencies
#from dashboard.models import Result

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
        topic_labels = ["Topic 1", "Topic 2", "Topic 3", "Topic 4",
                        "Topic 5", "Topic 6"]
        #comments_count = [33, 23, 12, 27, 18, 40]
        data = {
            "topic_labels": topic_labels,
            "comment_sentiments": {
                "positive": {},
                "neutral": {},
                "negative": {},
            }
        }
        return Response(data)


class ChartInstructorData(APIView):
    def get(self, request, format = None):
        # hardcoded for now, until we get the updated data from Results model
        instructor_names = ["Joe Smoe", "Louis XIV", "Ludwig Wiggtenstein"]
        comments_sentiments_dict  = {}
        data = {
            "instructor_names": instructor_names,
            "comments_count": comments_count,
        }
        return Response(data)
