from pkg_resources import parse_version
import django
from django.conf.urls import url
from . import views
from .views import DashboardView, DocumentationView
from distribution_chart.views import get_chart_data, \
ChartTopicData, ChartInstructorData

from fileupload.views import UploadView

# Importing custom upload handler class
from fileupload.uploadhandler import ProgressBarUploadHandler

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', DashboardView.as_view()),
    url('topic-distribution', DashboardView.topic_distribution,
        name='topic-distribution'),
    url('instructor-distribution', DashboardView.instructor_distribution,
        name='instructor-distribution'),
    url('file_upload', UploadView.file_upload, name='upload-new'),
    url('upload', UploadView.upload_view, name='upload'),
    url(r'^upload_progress$', UploadView.upload_progress,
        name='upload_progress'),
    url('about', DashboardView.about_view, name='about'),
    url('file_upload', UploadView.file_upload, name='file_upload'),
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
