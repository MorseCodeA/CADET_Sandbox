from django.conf.urls import url, include
from .views import DashboardView, DocumentationView
from distribution_chart.views import get_chart_data, \
ChartTopicData, ChartInstructorData

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', DashboardView.as_view()),
    url('topic-distribution', DashboardView.topic_distribution,
        name='topic-distribution'),
    url('instructor-distribution', DashboardView.instructor_distribution,
        name='instructor-distribution'),

    # file upload urls
    # fix file_upload error bc of missing dash
    url('file_upload/', include('fileupload.urls')),
    url('about', DashboardView.about_view, name='about'),
    url('stopword', DashboardView.stopword_view, name='stopword'),
    url('export', DashboardView.export_view, name='export'),
    url('options', DashboardView.after_upload_options, name='options'),

    # documentation urls
    url('documentation', DocumentationView.home, name="doc-home"),
    # better way of setting up endpoint from backend to frontend
    # by using Django REST Framework
    url(r'^api/chart/topic/data/$', ChartTopicData.as_view()),
    url(r'^api/chart/instructor/data/$', ChartInstructorData.as_view()),
    # also another way to creating an endpoint to serve json object
    url(r'^api/data/$', get_chart_data, name='api-data'),

]

