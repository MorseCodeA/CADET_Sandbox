# Create your views here.

from django.shortcuts import render, redirect

from django.core.cache import cache
import json
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, 'home.html')

def file_upload(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        return redirect('home')
    else:
        return render(request, 'file_upload.html')


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