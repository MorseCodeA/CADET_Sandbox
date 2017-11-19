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


# Django REST API viewsrom rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView

# Models dependencies
from .models import Result

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
    

class DocumentationView(TemplateView):
    def home(request):
        return render(request, 'documentation/doc-home.html')

# method 1 of delivering json and instance obj data
def get_chart_data(request, *args, **kwargs):
    data = {
        "comments_count": 10,
        "anon_id": 2,
    }
    return JsonResponse(data) # http response

# refactored class-based way of delivering json withr django rest framework
class ChartData(APIView):
    # here is the class that grabs that converts data from our Django-backend.
    # the models have already been updated with results from the Flask-backend
    # Stub data for now, later instantiate instances from Ashley's models,
    # which will include instance from Results.  Notice the saved data will
    # need to be converted back (again) into JSON format in the final step,
    # since that is compatible with AJAX call for frontend
    def get(self, request, format = None):
        # hardcoded for now, until we get the updated data from Results model
        topic_labels = ["Topic 1", "Topic 2", "Topic 3", "Topic 4",
                        "Topic 5", "Topic 6"]
        comments_count = [33, 23, 12, 27, 18, 40]
        comments_sentiments_dict  = {}
        positive_comments = {}
        data = {
            "topic_labels": topic_labels,
            "comments_count": comments_count,
        }
        return Response(data)
