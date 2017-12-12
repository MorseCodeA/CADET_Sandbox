from django.conf.urls import url, include
from .views import DashboardView, DocumentationView

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', DashboardView.as_view()),
    url('topic-distribution', DashboardView.topic_distribution,
        name='topic-distribution'),
    url('instructor-distribution', DashboardView.instructor_distribution,
        name='instructor-distribution'),

    # file upload urls, fix file_upload error bc of missing dash
    url('file_upload/', include('fileupload.urls')),
    url('about', DashboardView.about_view, name='about'),
    url('stopword', DashboardView.stopword_view, name='stopword'),
    url('export', DashboardView.export_view, name='export'),
    url('options', DashboardView.after_upload_options, name='options'),
]