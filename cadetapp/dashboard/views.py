import json
import random
import time, datetime

from django.shortcuts import render, get_object_or_404, render_to_response, \
    render, redirect
from django.core.cache import cache
from django.http import HttpResponseRedirect, HttpResponse

from django.urls import reverse
from django.views import generic
from django.template.defaultfilters import register
from django.utils.safestring import mark_safe
from django.conf import settings


from fileupload.forms import DocumentForm
from fileupload.models import Document


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

def multibarchart(request):
    """
    multibarchart test, will be replaced with calls from models later
    this type of graph fits into our topics and instuction distribution view
    """
    nb_element = 10
    xdata = range(nb_element)
    ydata = [random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)
    ydata3 = map(lambda x: x * 3, ydata)
    ydata4 = map(lambda x: x * 4, ydata)

    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}

    chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie,
        'name3': 'series 3', 'y3': ydata3, 'extra3': extra_serie,
        'name4': 'series 4', 'y4': ydata4, 'extra4': extra_serie
    }

    nb_element = 100
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple())
                     * 1000)
    xdata = range(nb_element)
    xdata = map(lambda x: start_time + x * 1000000000, xdata)
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"},
                   "date_format": tooltip_date}

    date_chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie,
    }

    charttype = "multiBarChart"
    chartcontainer = 'multibarchart_container' # container name
    chartcontainer_with_date = 'date_multibarchart_container' # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': True,
        },
        'chartdata_with_date': date_chartdata,
        'chartcontainer_with_date': chartcontainer_with_date,
        'extra_with_date': {
            'name': chartcontainer_with_date,
            'x_is_date': True,
            'x_axis_format': '%d %b %Y',
            'tag_script_js': True,
            'jquery_on_ready': True,
        },
    }
    return render_to_response('dashboard/multibarchart.html', data)

