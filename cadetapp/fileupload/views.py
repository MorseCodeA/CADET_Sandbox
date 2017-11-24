# Create your views here.

from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from django.core.cache import cache
import json
from django.http import HttpResponse
from .forms import DocumentForm
from .models import Document
from django.conf import settings
import os

def upload(request):
    path = settings.MEDIA_ROOT + '/downloads/'
    file_list = os.listdir(path)
    return render_to_response('upload.html', {'file_list': file_list})

def file_upload(request):
    messages.info(request, 'Your file has been successfully uploaded!')
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            for a_file in files:
                Document(file=a_file).save()
                return redirect('upload/')
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