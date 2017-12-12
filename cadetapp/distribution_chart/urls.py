from django.conf.urls import url
from distribution_chart.views import get_chart_data, \
ChartTopicData, ChartInstructorData


urlpatterns = [
	# setting up endpoint for ajax call by using Django REST Framework
	url('chart/topic/data/$', ChartTopicData.as_view()),
	url('chart/instructor/data/$', ChartInstructorData.as_view()),

	# also another way to creating an endpoint to serve json object,
	# but this is just set up as an example without Django REST Framework
	url(r'^data/$', get_chart_data, name='api-data'),
]

