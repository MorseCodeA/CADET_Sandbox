from django.conf.urls import url
from .views import DocumentationView

urlpatterns = [
    url('/', DocumentationView.home, name="doc-home.html"),
]
