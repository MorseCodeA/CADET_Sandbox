from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('r^topic-distribution', views.topic_distribution,
        name='topic_distribution'),
    url('r^instructor-distribution/$', views.instructor_distribution,
        name='instructor_distribution'),
]
