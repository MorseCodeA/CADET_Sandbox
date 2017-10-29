# -*- coding: utf-8 -*-
import json
from django.shortcuts import render, get_object_or_404, render_to_response, \
    render, redirect
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse

# Upload dependencies
from fileupload.forms import DocumentForm
from fileupload.models import Document

# ChartJS dependencies
from random import randint
from random import shuffle, randint
from itertools import islice
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _
from chartjs.views.lines import BaseLineChartView, HighchartPlotLineChartView
from chartjs.views.pie import HighChartPieView, HighChartDonutView
from chartjs.colors import next_color, COLORS
from chartjs.views.columns import BaseColumnsHighChartsView

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

def upload_view(request):
    documents = Document.objects.all()
    return render(request, 'dashboard/upload.html', {'documents':
                                                          documents})
def file_upload(request):
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            for a_file in files:
                Document(file=a_file).save()
            return redirect('dashboard/upload.html')
    else:
        form = DocumentForm()
    return render(request, 'dashboard/file_upload.html', {'form': form})

def upload_progress(request):
    # Uses Ajax calls to return the upload progress and total length values
    if 'X-Progress-ID' in request.GET:
        progress_id = request.GET['X-Progress-ID']
    elif 'X-Progress-ID' in request.META:
        progress_id = request.META['X-Progress-ID']
    else:
        progress_id = None
    if progress_id:
        cache_key = "%s_%s" % (request.META['REMOTE_ADDR'], progress_id)
        data = cache.get(cache_key)
        return HttpResponse(json.dumps(data))

def stopword_view(request):
    return render(request, 'dashboard/stopword.html')

def about_view(request):
    return render(request, 'dashboard/about.html')

def export_view(request):
    return render(request, 'dashboard/export.html')


# CHARTS VIEWS
class LineChartJSONView(BaseLineChartView):
    template_name = 'dashboard/chartdemo.html'

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        xaxis = ["January", "February", "March", "April", "May", "June", "July"]
        return xaxis

    def get_providers(self):
        """Return names of datasets."""
        yaxis = ["Central", "Eastside", "Westside"]
        return yaxis

    def get_data(self):
        """Return 3 datasets to plot."""
        sample = [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]

        return sample


line_chart = TemplateView.as_view(template_name='dashboard/chartdemo.html')
line_chart_json = LineChartJSONView.as_view()