# -*- coding: utf-8 -*-
import json
from django.shortcuts import render, get_object_or_404, render_to_response, \
    render, redirect
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView

# Upload dependencies
from fileupload.forms import DocumentForm
from fileupload.models import Document
from fileupload.uploadhandler import ProgressBarUploadHandler

# Importing custom upload handler class
from django.core.cache import cache
from django.core.files.uploadhandler import TemporaryFileUploadHandler

from fileupload.DataConversion import CSVfiletoJSONobj


class UploadView(View):
    def upload_view(request):
        documents = Document.objects.all()
        return render(request, 'upload.html', {'documents': documents})
    def file_upload(request):
        if request.method == 'POST':
            files = request.FILES.getlist('file')
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                for a_file in files:
                    Document(file=a_file).save()
                    JSONinput = CSVfiletoJSONobj
                    JSONinput._init_(JSONinput)
                    JSONinput.set_input_path(JSONinput, '/home/hartnerk/CADET_Sandbox/cadetapp/media/downloads/'+str(a_file))
                    #JSONinput.set_input_path(JSONinput, '/../media/downloads/'+str(a_file))                
                    JSONinput.set_output_path(JSONinput, '/home/hartnerk/CADET_Sandbox/cadetapp/media/downloads/cadet-test-a.json')
                    #JSONinput.set_output_path(JSONinput, '../media/downloads/'+str(a_file))
                     #JSONinput.set_fieldnames(JSONinput, "anon id","Program","Modality","Course Number/ Section ID","Instructor Last Name", "Instructor First Name", "Course comments","Instructor comments","[Additional comments, if available]")
                    JSONinput.CSVtoJSON_Obj(JSONinput)
                return redirect('upload.html')
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