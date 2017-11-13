from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'controller'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
