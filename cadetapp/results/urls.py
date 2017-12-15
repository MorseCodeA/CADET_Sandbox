from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^(test)',views.retrieve_test,name='retrieve_test'),
    url(r'^(?P<result_id>[0-9]+)', views.retrieve, name='retrieve'),
]
