from pkg_resources import parse_version
import django
from django.conf.urls import url
from . import views
from dashboard.views import DashboardView

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', DashboardView.as_view()),
    url('topic-distribution', DashboardView.topic_distribution,
        name='topic-distribution'),
    url('instructor-distribution', DashboardView.instructor_distribution,
        name='instructor-distribution'),
    url('file_upload', DashboardView.file_upload, name='upload-new'),
    url('upload', DashboardView.upload_view, name='upload'),
    url(r'^upload_progress$', DashboardView.upload_progress,
        name='upload_progress'),
    url('about', DashboardView.about_view, name='about'),
    url('file_upload', DashboardView.file_upload, name='file_upload'),
    url('stopword', DashboardView.stopword_view, name='stopword'),
    url('export', DashboardView.export_view, name='export'),
    url('documentation', DashboardView.documentation_view, name="doc-home"),

    # test chartjs
    #url('chartdemo', views.line_chart, name='chartdemo'),
]
