from pkg_resources import parse_version
import django
from django.conf.urls import url
from . import views
from .views import DashboardView, UploadView, DocumentationView, ChartData, \
    get_chart_data

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

    # documentation urls
    url('documentation', DocumentationView.home, name="doc-home"),

    # test chartjs
    url(r'^api/chart/data/$', ChartData.as_view()),
    url(r'^api/data/$', get_chart_data, name='api-data'),
]
