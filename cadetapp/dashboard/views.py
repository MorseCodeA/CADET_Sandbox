#-----------------------------------------------------------------------------
# Purpose:     Dashboard serves all templates to the user as html pages. The
#              pages correspond to the items on the vertical navigation bar.
#              Pages include index, topic_distribution,
#              instructor_distribution, stopword, about, export,
#              after_upload_options
#-----------------------------------------------------------------------------

# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.views.generic import TemplateView

# Upload dependencies
from fileupload.forms import DocumentForm
from fileupload.models import Document

# Chart dependencies
from distribution_chart.views import ChartTopicData, \
ChartInstructorData

# Documentation depenciences
from documentation.views import DocumentationView

# Controller dependencies
from  controller.views import *

class DashboardView(TemplateView):
    """
    Inherit from TemplateView, which normally is best used for templating
    static html pages.

    Return: none, just route user request on the browser to specific html
    templates at the specified paths
    """
    template_name = 'dashboard/index.html'

    def index(request):
        # which contains comments and topics
        # main dashboard located at http://example/dashboard
        return render(request, 'dashboard/index.html')

    def topic_distribution(request):
        # http://example/dashboard/topic-distribution
        computeTopicResults()
        return render(request, 'dashboard/topic-distribution.html')

    def instructor_distribution(request):
        # http://example/dashboard/instructor-distribution
        computeInstructorResults()
        return render(request, 'dashboard/instructor-distribution.html')

    def stopword_view(request):
        # http://example/dashboard/stopword
        return render(request, 'dashboard/stopword.html')

    def about_view(request):
        # http://example/dashboard/about
        return render(request, 'dashboard/about.html')

    def export_view(request):
        # http://example/dashboard/export
        return render(request, 'dashboard/export.html')

    def after_upload_options(request):
        # http://example/dashboard/options
        return render(request, 'dashboard/options.html')
