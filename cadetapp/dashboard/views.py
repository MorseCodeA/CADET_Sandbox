# -*- coding: utf-8 -*-
import json
from django.shortcuts import render, get_object_or_404, render_to_response, \
    render, redirect
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView
from django.urls import reverse

# Upload dependencies
from fileupload.forms import DocumentForm
from fileupload.models import Document
# Importing custom upload handler class
from fileupload.uploadhandler import ProgressBarUploadHandler

# Chart dependencies
from distribution_chart.views import ChartTopicData, \
ChartInstructorData

# Documentation depenciences
from documentation.views import DocumentationView

# Models dependencies
#from .models import Result

class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

    def index(request):
        # later will call instances from Ashley's models,
        # which contains comments and topics
        # main dashboard located at http://example/dashboard
        return render(request, 'dashboard/index.html')

    def topic_distribution(request):
        # http://example/dashboard/topic-distribution
        return render(request, 'dashboard/topic-distribution.html')

    def instructor_distribution(request):
        # http://example/dashboard/instructor-distribution
        return render(request, 'dashboard/instructor-distribution.html')

    def stopword_view(request):
        return render(request, 'dashboard/stopword.html')

    def about_view(request):
        return render(request, 'dashboard/about.html')

    def export_view(request):
        return render(request, 'dashboard/export.html')

    def after_upload_options(request):
        return render(request, 'dashboard/options.html')
