from pkg_resources import parse_version
import django
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


app_name = 'dashboard'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('topic-distribution', views.topic_distribution,
        name='topic-distribution'),
    url('instructor-distribution', views.instructor_distribution,
        name='instructor-distribution'),
    url('file_upload', views.file_upload, name='upload-new'),
    url('upload', views.upload_view, name='upload'),
    url(r'^upload_progress$', views.upload_progress,
        name='upload_progress'),
    url('about', views.about_view, name='about'),
    url('file_upload', views.file_upload, name='file_upload'),
    url('stopword', views.stopword_view, name='stopword'),
    url('export', views.export_view, name='export'),

    # test chartjs
    url('chartdemo', views.line_chart, name='chartdemo.html')
]

