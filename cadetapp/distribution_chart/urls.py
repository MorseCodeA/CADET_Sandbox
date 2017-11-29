from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from distribution_chart.views import get_chart_data, \
ChartTopicData, ChartInstructorData


urlpatterns = [
	# better way of setting up endpoint from backend to frontend
	# by using Django REST Framework
	url('chart/topic/data/$', ChartTopicData.as_view()),
	url('chart/instructor/data/$', ChartInstructorData.as_view()),
	# also another way to creating an endpoint to serve json object
	url(r'^data/$', get_chart_data, name='api-data'),
]

