# encoding: utf-8
from django.conf.urls import url
from .views import upload_view, option_view, upload_progress

urlpatterns = [
    url(r'^$', upload_view, name='upload-new'),
    url(r'^options.html$', option_view, name='options'),
    url(r'^upload_progress$', upload_progress, name="upload_progress"),
]