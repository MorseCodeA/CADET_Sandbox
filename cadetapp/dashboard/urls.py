from django.conf.urls import url
from . import views

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('topic-distribution', views.topic_distribution,
        name='topic-distribution'),
    url('instructor-distribution', views.instructor_distribution,
        name='instructor-distribution'),
    url('upload', views.upload_view, name='upload'),
    url('stopword', views.stopword_view, name='stopword'),
]
