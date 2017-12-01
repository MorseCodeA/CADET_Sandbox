# encoding: utf-8
from django.conf.urls import url
from .views import file_upload, upload, upload_progress

urlpatterns = [
    url(r'^$', file_upload, name='upload-new'),
    url(r'^upload/$', upload, name='upload'),
    url(r'^upload_progress$', upload_progress, name="upload_progress"),
]