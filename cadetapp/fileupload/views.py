# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.cache import cache
import json
from django.http import HttpResponse
from .forms import DocumentForm, JsonForm
from .models import Document
from django.conf import settings
from .DataConversion import CSVfiletoJSONobj
import os

def option_view(request):
    if request.method == 'POST':
        form = JsonForm(request.POST)
        if form.is_valid():
            media_path = settings.MEDIA_ROOT + '/downloads/'
            comments = form.cleaned_data['comments']
            topics = form.cleaned_data['topics']
            iterations = form.cleaned_data['iterations']
            JSONinput = CSVfiletoJSONobj
            JSONinput._init_(JSONinput)
            JSONinput.set_input_path(JSONinput, form.cleaned_data['files'])
            JSONinput.set_output_path(JSONinput, media_path + str('cadet-file-to-json.json'))
            JSONinput.CSVtoJSON_Obj(JSONinput)
            messages.info(request, 'The JSON file has been successfully created!')
            return redirect(request.path_info)
    else:
        form = JsonForm()
    return render(request, 'options.html', {'form': form})

def upload_view(request):
    media_path = settings.MEDIA_ROOT + '/downloads/'
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            for a_file in files:
                Document(file=a_file).save()
            return redirect('options.html')
    else:
        form = DocumentForm()
    return render(request, 'file_upload.html', {'form': form})

def upload_progress(request):
    #Uses Ajax calls to return the upload progress and total length values
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