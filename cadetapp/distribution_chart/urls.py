from django.conf.urls import url
from distribution_chart.views import get_chart_data, \
ChartTopicData, ChartInstructorData, ChartTopicWordData

urlpatterns = [
	# better way of setting up endpoint from backend to frontend
	# by using Django REST Framework
    url(r'^chart/topic/data/$', ChartTopicData.as_view()),
    url(r'^chart/instructor/data/$', ChartInstructorData.as_view()),
    url(r'^chart/topic/word/all/$', ChartTopicWordData.as_view()),
    # also another way to creating an endpoint to serve json object
    url(r'^data/$', get_chart_data, name='api-data'),
]
